import ast


class DataExtractor:
    def __init__(self, raw_data):
        self.data = ast.parse(raw_data)
        self.class_name = self.get_class_name()
        if self.class_name is not None:
            self.instance_attributes = self.get_instance_attributes()
            self.instance_methods = self.get_instance_method_names()
            self.inheritance = self.get_inheritance()
            self.association = self.get_association()

    # Created By Bikrant
    def get_class_name(self):
        for aNode in ast.walk(self.data):
            if isinstance(aNode, ast.ClassDef):
                return aNode.name

    # Created By Jignesh
    def get_instance_attributes(self):
        instance_attribute = []
        for node in ast.walk(self.data):
            if isinstance(node, ast.Assign):
                if hasattr(node, 'targets'):
                    if isinstance(node.targets[0], ast.Attribute):
                        if hasattr(node.targets[0], 'value'):
                            if isinstance(node.targets[0].value, ast.Name):
                                if node.targets[0].value.id == 'self':
                                    if node.targets[0].attr not in \
                                            instance_attribute:
                                        instance_attribute. \
                                            append(node.targets[0].attr)
        return instance_attribute

    # Created By Suman
    def get_instance_method_names(self):
        instance_method = [node.name for node in ast.walk(self.data)
                           if isinstance(node, ast.FunctionDef)]
        return instance_method

    # Created By Jignesh
    def get_inheritance(self):
        inheritance = []
        for a_node in ast.walk(self.data):
            if isinstance(a_node, ast.ClassDef):
                for a_class in a_node.bases:
                    if isinstance(a_class, ast.Name):
                        inheritance.append(a_class.id)
        return inheritance

    # Created By Jignesh
    def get_association(self):
        association = []
        [association.append(self.__get_name_object_id(a_node))
         for a_node in ast.walk(self.data) if isinstance(a_node, ast.Call) and
         self.__is_a_valid_class(self.__get_name_object_id(a_node),
                                 association)]
        return association

    def __get_name_object_id(self, node):
        if isinstance(node.func, ast.Name):
            return node.func.id
        if isinstance(node.func.value, ast.Name):
            return node.func.value.id
        return None

    def __is_a_valid_class(self, node, name_array):
        return node is not None and node not in name_array and node[
            0].isupper() \
               and node != self.class_name and node not in self.inheritance
