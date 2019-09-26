from abc import ABCMeta, abstractmethod
from os.path import isdir, isfile


class InterpreterCreator(metaclass=ABCMeta):

    @staticmethod
    def __is_a_valid_directory(path):
        result = False
        if isdir(path):
            result = True
        else:
            print(f'Please provide a valid path'
                  f' to a directory and try again!!!')
        return result

    @staticmethod
    def __is_a_valid_database(db_name):
        result = False
        if isfile(f'./Database/{db_name}.db'):
            result = True
        else:
            print(f'Database {db_name} not found!!! Try again')
        return result

    @abstractmethod
    def create_interpreter(self, options):
        pass
