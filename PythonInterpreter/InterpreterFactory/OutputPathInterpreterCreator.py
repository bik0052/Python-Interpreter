from .InterpreterCreator import InterpreterCreator
from .Interpreter import Interpreter


class OutputPathInterpreterCreator(InterpreterCreator):

    def create_interpreter(self, options):
        if self.__is_a_valid_directory(options[2]):
            return Interpreter(options[1], options[2])
