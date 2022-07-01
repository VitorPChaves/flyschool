import pickle
from abc import ABC

class abstractDAO(ABC):
    def __init__(self, datapath):
        self._datapath = 'C:/Users/Vitor/Documents/UFSC/APS/Fabiane/FlySchoolPy/src/model/database/' + datapath
        self._temp = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__save()

    def __save(self):
        file = open(self._datapath, 'wb')
        pickle.dump(self._temp, file)
        file.close()
    
    def __load(self):
        file = open(self._datapath, 'rb')
        self._temp = pickle.load(file)

    def add(self, key, objeto):
        self._temp[key] = objeto
        self.__salva()

        print(objeto.cpf) #apenas pra teste retirar apos

    def remove(self, key):
        try:
            self._temp.pop(key)
            self.__save()
        except:
            raise KeyError

    def capture(self, key):
        try:
            print(self._temp[key].cpf) #apenas pra teste retirar apos

            return self._temp[key]
        except:
            raise KeyError

    def list(self):
        print(self._temp.values()) #apenas pra teste retirar apos

        return self._temp.values()
