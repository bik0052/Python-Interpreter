from os import walk
from os.path import join, abspath
from Validation.Validator import Validator
from Validation.Pep8Formatter import Pep8Formatter


class FileReader:
    # Created by Bikrant
    @staticmethod
    def read_from_file(path):
        if FileReader.__is_a_python_file(path):
            return FileReader.__try_read_data(path)
        else:
            return ''

    @staticmethod
    def __try_read_data(path):
        valid_functions = {
            'ok': FileReader.read, 'f': Pep8Formatter.format_pep8
        }

        valid = Validator.validate(path)
        if valid not in valid_functions.keys():
            print(f'Not a valid Python code in {abspath(path)} '
                  f'Extraction process has been stopped! '
                  f'Fix the file and try again')
            return ''

        return FileReader.__get_pep8_formatted_data(path,
                                                    valid_functions[valid])

    @staticmethod
    def __get_pep8_formatted_data(path, get_data):
        raw_data = get_data(path)
        if Validator.contains_multiple_class(raw_data) is not False:
            return raw_data
        else:
            print(f'Data Extraction has stopped as more than 1 class '
                  f'definition was found in \n{abspath(path)}')
            return ''

    @staticmethod
    def __is_a_python_file(file):
        return file.endswith('.py')

    @staticmethod
    def __get_all_file_paths_from(path):
        for root, dirs, files in walk(path):
            for file in filter(FileReader.__is_a_python_file, files):
                yield join(root, file)

    # Created by Jignesh
    @staticmethod
    def read_from_folder(path):
        data = []
        for a_file_path in FileReader.__get_all_file_paths_from(path):
            primary_data = FileReader.__try_read_data(a_file_path)
            if primary_data is '':
                data.clear()
                break
            data.append(primary_data)
        return data

    # Created by Suman
    @staticmethod
    def read(path):
        data = ""
        # Created By suman
        try:
            with open(path, 'r') as file:
                for aLine in file:
                    data += aLine
        except FileNotFoundError:
            print(path, ' was not found')
        except PermissionError:
            print("Access Denied for the specified file " + path)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        finally:
            return data
