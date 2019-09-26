from .InterpreterCreator import InterpreterCreator
from .Interpreter import Interpreter


class DatabaseInterpreterCreator(InterpreterCreator):

    def create_interpreter(self, options):
        if self.__is_a_valid_directory(options[2]) and \
                self.__is_a_valid_database(options[3]):
            return Interpreter(options[1], options[2], options[3])
