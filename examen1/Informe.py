class Informe:
    def __init__(self):
        self.nombre=""
        self.__correo = ""
        self.__numeros =[]
        self.__complementario =0
        self.__reintegro =""
        self.__ganadora =""
        self.__dni=""
    def meternumeros(self,numero):
        self.__numeros.append(numero)

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, value):
        self.__correo = value
        pass
    @property
    def numeros(self):
        return self.__numeros

    @numeros.setter
    def numeros(self, value):
        self.__numeros =value
        pass
    @property
    def complementario(self):
        return self.__complementario

    @complementario.setter
    def complementario(self, value):
        self.__complementario=value
        pass
    @property
    def reintegro(self):
        return self.__reintegro

    @reintegro.setter
    def reintegro(self, value):
        self.__reintegro=value
        pass
    @property
    def ganadora(self):
        return self.__ganadora


    @ganadora.setter
    def ganadora(self, value):
        self.__ganadora=value
        pass
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni=value
        pass