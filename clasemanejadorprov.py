from claseprovincia import Provincia
class ManejadorProvincias:
    __provincias = []
    def __init__(self):
        self.__provincias = []

    def añadirprov(self, provincia):
        self.__provincias.append(provincia)

    def listaprov(self):
        return self.__provincias

    def indiceprov(self, provincia):
        bandera = False
        i = 0
        while i < len(self.__provincias) and not bandera:
            if provincia == self.__provincias[i]:
                bandera = True
            else:
                i += i
        return i

    def toJSON(self):
        provincias = [provincia.toJSON() for provincia in self.__provincias]
        return provincias

    def decodificarLista(self, lista):
        for provincia in lista:
            class_name = provincia['__class__']
            class_ = eval(class_name)
            atributos = provincia['__atributos__']
            nuevaprov = class_(**atributos)
            self.añadirprov(nuevaprov)