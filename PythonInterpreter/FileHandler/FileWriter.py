from os.path import abspath


class FileWriter:
    # Created by Bikrant & Suman
    inheritance = ' --|> '
    association = ' --> '

    @staticmethod
    def write(class_data):
        try:
            with open(abspath('./rawUml.txt'), 'w') as file:
                file.write('@startuml \n')
                for a_class_data in class_data:
                    for a_attribute in a_class_data.instance_attributes:
                        file.write(f"{a_class_data.class_name}"
                                   f" : {a_attribute}\n")
                    for a_method in a_class_data.instance_methods:
                        file.write(f"{a_class_data.class_name}"
                                   f" : {a_method}()\n")
                    if len(a_class_data.inheritance) != 0:
                        for a_class in a_class_data.inheritance:
                            file.write(f"{a_class_data.class_name}"
                                       f" {FileWriter.inheritance} {a_class}\n")
                    if len(a_class_data.association) != 0:
                        for a_class in a_class_data.association:
                            file.write(f"{a_class_data.class_name}"
                                       f" {FileWriter.association} {a_class}\n")
                file.write('@enduml')

        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
