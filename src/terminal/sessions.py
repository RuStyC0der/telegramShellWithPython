from src.terminal.factory import SingletonDecorator
from src.terminal.settings import settings
from src.terminal.terminal import Terminal
from src.terminal.utils import execute_async, parse_template, block_escape


class Session(object):
    def __init__(self, owner_uid, terminal, name="default"):
        self.owner_uid = owner_uid
        self.terminal = terminal
        self.id = name


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create(self, owner_uid):
        pass

    def get_by_user_name(self, user_name: str) -> Terminal or None:
        pass

    def get_or_create(self, user_name: str) -> Terminal:
        pass




if __name__ == '__main__':
    sessions = SingletonDecorator(SessionManager)
