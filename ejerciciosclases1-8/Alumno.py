
class Alumno():
    __nombre=""
    __notas=["",""]
    def __init__(self):
        self.__nombre=(input("introduce el nombre del alumno"))
        self.__notas.clear()
        for i in range (1,4):
            nota=-1
            interruptor= True
            while  nota<0 or nota>10 or interruptor:
                try:
                    nota = float(input("introduce nota "))
                    interruptor=False
                except:
                    interruptor= True

            self.__notas.append(nota)

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, value):
        self.__notas=value
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre=value
        pass
