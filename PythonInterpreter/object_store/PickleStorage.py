from object_store.Storage import Storage
import pickle
from os import path


class PickleStorage(Storage):
    def _open(self, permission=None):
        if permission is not None:
            self.db = open('./object_store/storage.pickle', permission)

    def _store(self, key, new_data):
        if self._storage_is_empty():
            self._store_new_data(key, new_data)
        else:
            self._append_to_existing(key, new_data)

    def _append_to_existing(self, key, new_data):
        self._open('rb')
        data = pickle.load(self.db)
        if key in data.keys():
            data[key] = new_data
        else:
            data.update({key: new_data})
        self._close()
        self._open('wb')
        pickle.dump(data, self.db)

    def _store_new_data(self, key, new_data):
        self._open('wb')
        pickle.dump({key: new_data}, self.db)

    @staticmethod
    def _storage_is_empty():
        result = True
        if path.isfile('./object_store/storage.pickle'):
            result = path.getsize('./object_store/storage.pickle') < 0
        return result

    def _get_data(self, key):
        self._open('rb')
        data = pickle.load(self.db)
        try:
            return data[key]
        except KeyError:
            print('Key Not Found')
