from InterpreterFactory.DefaultInterpreterCreator import \
        DefaultInterpreterCreator
from InterpreterFactory.OutputPathInterpreterCreator import \
    OutputPathInterpreterCreator
from InterpreterFactory.DatabaseInterpreterCreator import \
    DatabaseInterpreterCreator
from sys import argv

if __name__ == "__main__":

    interpreter_creators = {2: DefaultInterpreterCreator,
                            3: OutputPathInterpreterCreator,
                            4: DatabaseInterpreterCreator}
    interpreter = None
    if len(argv) in interpreter_creators:
        interpreter_factory = interpreter_creators[len(argv)]()
        interpreter = interpreter_factory.create_interpreter(argv)
    else:
        print('Please use the command "python main.py your name"')

    if interpreter is not None:
        interpreter.cmdloop()
