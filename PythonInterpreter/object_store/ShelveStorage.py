from object_store.Storage import Storage
import shelve


class ShelveStorage(Storage):

    def _open(self, permission=None):
        self.db = shelve.open('./object_store'
                              '/storage.shelf', 'c')

    def _store(self, key, new_data):
        if isinstance(self.db, shelve.DbfilenameShelf):
            self.db[key] = new_data

    def _get_data(self, key):
        if isinstance(self.db, shelve.DbfilenameShelf):
            try:
                return self.db[key]
            except KeyError:
                print('Key Not Found')
