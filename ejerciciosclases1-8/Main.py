from Alumno import Alumno
def sacarmedia(notasalumno):
    suma=0
    for i in notasalumno:
        suma+=i
    return suma/3
def imprimir(alumos, alumnos=None):
    f= open("alumnosconmedia.txt",'w')
    llaves = alumnos.keys()
    for i in alumos:
        f.write(i.getkey(),sacarmedia(i.value()))
    f.close()
def opc1():
    alumnos ={}
    resp=str(input("desea introducir alumnos?")).Upper()
    while resp=="SI":
        alum=Alumno()
        alumnos[alum.nombre]=alum.notas
        resp = str(input("desea introducir mas alumnos?")).Upper()
    imprimir(alumnos)


def opc2():
    print("opc2")

def opc3():
    print("Saliendo...")
res=1
opciones={1:opc1,2:opc2,3:opc3}
while res!=3:
    res=int(input("escribe la opcion "
                  "1 ejercicio con listas de alumnos y generar fichero con media"
                  "2 ejercicio universidad con base de datos "
                  "3 salir"))
    opciones[res]()
