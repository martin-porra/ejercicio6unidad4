import requests

class clima:
    __url = None
    __clima = None

    def __init__(self):
        self.__url = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=564c4c901948a8f08a60d25f7a11040a'

    def conectar(self, prov, capi):
        self.__extraer = requests.get(self.__url.format(prov))
        self.__clima = self.__extraer.json()
        if self.__clima['cod'] == '404':
            self.__extraer = requests.get(self.__url.format(capi))
            self.__clima = self.__extraer.json()

    def temp(self):
        temperatura = ''
        if self.__clima != None:
            temperatura = self.__clima['main']['temp']
        return temperatura

    def termica(self):
        termica = ''
        if self.__clima != None:
            termica = self.__clima['main']['feels_like']
        return termica

    def humedad(self):
        humedad = ''
        if self.__clima != None:
            humedad = self.__clima['main']['humidity']
        return humedad