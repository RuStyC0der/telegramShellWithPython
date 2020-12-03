

class ArgumentFormatException(Exception):
    def __init__(self, message):
        self.message = message


class SessionDontExistException(Exception):
    def __init__(self):
        self.message = 'You need to have open terminal to use this command'


class TerminalNotFoundException(Exception):
    def __init__(self):
        self.message = 'Could not find requested terminal'
