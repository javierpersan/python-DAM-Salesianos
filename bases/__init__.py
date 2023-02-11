def opcion1():
    print("opc1")

def opcion2():
    print("opc2")
def opcion3():
    print("opc3")
def opcion4():
    print("opc4")
def opcion5():
    print("opc5")
def opcion6():
    print("saliendo")

opc=0
opciones ={
    1:opcion1,
    2:opcion2,
    3:opcion3,
    4:opcion4,
    5:opcion5,
    6:opcion6
}
while opc!=6:
    opc=int(input("inserta la opcion"))
    opciones[opc]()
