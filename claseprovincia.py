class Provincia:
    __nombre = ''
    __capital = ''
    __habitantes = 0
    __cantDepartamentos = 0
    def __init__(self, nombre, capital, habitantes, cantDeptos):
        self.__nombre = self.requerido(nombre, 'Es requerido un Nombre')
        self.__capital = self.requerido(capital, 'Es requerido una Capital')
        self.__habitantes = self.requerido(habitantes, 'Es requerido num de Habitantes')
        self.__cantDepartamentos = self.requerido(cantDeptos, 'Es requerido una Cantidad de departamentos')

    def getnom(self):
        return self.__nombre
    def getcapi(self):
        return self.__capital
    def getcanthabi(self):
        return self.__habitantes
    def getcandepa(self):
        return self.__cantDepartamentos
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                habitantes=self.__habitantes,
                cantDeptos=self.__cantDepartamentos
            )
        )
        return d