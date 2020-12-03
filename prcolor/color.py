GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
ENDC = '\033[0m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'

WHITE = '\033[97m'
MAGENTA = '\033[95m'
GREY = '\033[90m'
BLACK = '\033[90m'
DEFAULT = '\033[99m'


class Color:
    def success(self, text):
        self.green(text)

    def error(self, text):
        self.red(text)

    def warn(self, text):
        self.yellow(text)

    def green(self, text):
        color = GREEN
        self.__colorize(text, color)

    def red(self, text):
        color = RED
        self.__colorize(text, color)

    def blue(self, text):
        color = BLUE
        self.__colorize(text, color)

    def yellow(self, text):
        color = YELLOW
        self.__colorize(text, color)

    def default(self, text):
        color = DEFAULT
        self.__colorize(text, color)

    def white(self, text):
        color = WHITE
        self.__colorize(text, color)

    def magenta(self, text):
        color = MAGENTA
        self.__colorize(text, color)

    def grey(self, text):
        color = GREY
        self.__colorize(text, color)

    def black(self, text):
        color = BLACK
        self.__colorize(text, color)

    def __colorize(self, text, color):
        normal_text = self.__normalize_text(text)
        print(f'{color} {normal_text} {ENDC}')

    def __normalize_text(self, text):
        text = self.__replace_underline(text)
        text = self.__replace_bold(text)
        return text

    @staticmethod
    def __replace_underline(text):
        text = text.replace('<u>', UNDERLINE)
        text = text.replace('</u>', ENDC)
        return text

    @staticmethod
    def __replace_bold(text):
        text = text.replace('<b>', BOLD)
        text = text.replace('</b>', ENDC)
        return text
