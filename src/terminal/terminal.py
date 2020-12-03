import os
import sys
import threading
from enum import Enum
from time import sleep

import pyte


from src.terminal.shortcuts import replace_shortcuts


class TerminalState(Enum):
    CLOSED = 0
    OPEN = 1
    FROZEN = 2
    BROKEN = 3


class Terminal:
    def __init__(self, name: str,
                 sh_path: str, su_path: str = None,
                 login: str = None, password: str = None,
                 on_change=None):
        self.name = name
        self.sh_path = sh_path
        self.su_path = su_path
        self.login = login
        self.password = password
        self.on_change = on_change

        self.controls = {}
        self.interactive = False
        self.auto_submit = True

        self.state: TerminalState = TerminalState.CLOSED
        self.screen = pyte.Screen(80, 24)
        self.stream = pyte.ByteStream(self.screen)

        self.fd = None
        self.content = None
        self.content_update = False

    def open(self):
        pid, self.fd = os.forkpty()

        if pid == 0:
            if self.login:
                os.execv(self.su_path, [self.su_path, "-", self.login, "-s", self.sh_path])
            else:
                os.execv(self.sh_path, [self.sh_path, ])

            sys.exit(0)
        else:
            self.state = TerminalState.OPEN

            pty_watcher = threading.Thread(target=self.monitor_pty)
            # pty_watcher.daemon = True
            pty_watcher.start()

    def close(self):
        self.state = TerminalState.CLOSED
        if self.on_change:
            self.refresh()
        os.close(self.fd)

    def refresh(self):
        self.on_change(self, self.content)

    def input(self, data: str):
        if self.state != TerminalState.OPEN:
            return

        data = replace_shortcuts(data)

        try:
            os.write(self.fd, data.encode("utf-8"))
        except OSError:
            self.state = TerminalState.BROKEN

    def monitor_pty(self):
        try:
            output = os.read(self.fd, 1024)

            if self.login:
                self.input(self.password + '\n')

            self.input('export TERM=linux\nclear\n')

            while output:
                self.stream.feed(output)
                self.content = '\n'.join(self.screen.display)
                self.content_update = True

                if self.on_change:
                    self.refresh()

                output = os.read(self.fd, 1024)
        except OSError:
            self.state = TerminalState.BROKEN
            return


# TODO fix monitor_pty behavior in multi threading (or not)

if __name__ == '__main__':

    name = "test"
    sh_path = "/bin/bash"
    su_path = "/bin/su"

    t = Terminal(name=name, sh_path=sh_path, su_path=su_path, on_change=print)
    t.open()

    sleep(1)
    t.input("nano\n")
    print(t.content)
    t.close()

