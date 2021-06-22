from claseprovincia import Provincia
from clasemanejadorprov import ManejadorProvincias
from claseobjet import ObjectEncoder

class repositorio:
    __conn = None
    __manejador = None

    def __init__(self, conn):
        self.__conn = conn
        lista = self.__conn.leerJSONArchivo()
        self.__manejador = ManejadorProvincias()
        self.__manejador.decodificarLista(lista)

    def agregarprov(self, provincia):
        self.__manejador.añadirprov(provincia)
        return provincia


    def obtenerlist(self):
        return self.__manejador.listaprov()

    def grabar(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())