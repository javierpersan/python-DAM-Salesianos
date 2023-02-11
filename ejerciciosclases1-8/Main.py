from Alumno import Alumno
def sacarmedia(notasalumno):
    suma=0
    for i in notasalumno:
        suma+=i
    return suma/3
def imprimir(alumos):
    f= open("alumnosconmedia.txt",'a')
    llaves = alumos.keys()
    for i in llaves:
        f.write(i+"\n")
        f.write(str(sacarmedia(alumos[i]))+"\n")
    f.close()
def opc1():
    alumnos ={}
    resp=str(input("desea introducir alumnos?")).upper()
    while resp=="SI":
        alum=Alumno()
        alumnos[alum.nombre]=alum.notas
        resp = str(input("desea introducir mas alumnos?")).upper()
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

