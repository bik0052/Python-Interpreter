from abc import ABCMeta, abstractmethod


class Storage(metaclass=ABCMeta):

    def __init__(self):
        self.db = None

    def set_data(self, key, data):
        self._open()
        self._store(key.lower(), data)
        self._close()

    def get_data(self, key):
        self._open()
        data = self._get_data(key.lower())
        self._close()
        return data

    @abstractmethod
    def _open(self, permission=None):
        pass

    @abstractmethod
    def _store(self, key, new_data):
        pass

    @abstractmethod
    def _get_data(self, key):
        pass

    def _close(self):
        self.db.close()

# # Created By Jignesh
# class Storage:
#     db = None
#
#     @staticmethod
#     def open_storage():
#         Storage.db = shelve.open('./object_store'
#                                  '/storage.shelf', 'c')
#
#     @staticmethod
#     def store(key, new_data):
#         if isinstance(Storage.db, shelve.DbfilenameShelf):
#             Storage.db[key] = new_data
#
#     @staticmethod
#     def get_data(key):
#         if isinstance(Storage.db, shelve.DbfilenameShelf):
#             try:
#                 return Storage.db[key]
#             except KeyError as e:
#                 print('Key Not Found')
#
#     @staticmethod
#     def close():
#         Storage.db.close()
