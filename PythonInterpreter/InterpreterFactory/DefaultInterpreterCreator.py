from .InterpreterCreator import InterpreterCreator
from .Interpreter import Interpreter


class DefaultInterpreterCreator(InterpreterCreator):

    def create_interpreter(self, options):
        return Interpreter(options[1])
