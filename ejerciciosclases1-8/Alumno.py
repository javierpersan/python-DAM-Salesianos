
class Alumno():
    __nombre=""
    __notas=["",""]
    def __init__(self):
        self.__nombre=str(input("introduce el nombre del alumno"))
        self.__notas.clear()
        for i in range (1,4):
            nota=0
            while nota<0 and nota>10:
                nota = float(input("introduce nota ",i))

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