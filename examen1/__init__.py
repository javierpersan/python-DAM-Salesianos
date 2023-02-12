from Conexion import Conexion
import random
from datetime import datetime
from Informe import Informe
import sys
def creararchivo(arrayd):
    print("opcion crear fichero")
    global informes
    informes=[]
    fp=open("Boletos.txt","r")
    for line in fp:
        inf = Informe()
        linead=line.split(" ")
        inf.dni=linead[0]
        for i in range (1,7):
            inf.meternumeros(linead[i])
        n1= int(linead[7])
        inf.complementario=n1
        inf.reintegro=linead[8]
        informes.append(inf)
    fp.close()
    for j in informes:
        users=open("clientes.txt","r")
        for linea in users:
            if j.dni in linea:
                lineadiv=linea.split(" ")
                j.correo=lineadiv[1]
        users.close()
        fi= open("Envios.txt","w")
        fi.write("Fichero de envios \n")
        fi.close()
    for z in informes:
        f=open("Envios.txt","a")
        numeros1= ' '.join(str(x) for x in arrayd[1:6])
        print(numeros1)
        numeros2=" ".join(str(x) for x in z.numeros)
        f.write(z.correo+"\n participa con los numeros:"+numeros2+"\n Complementario:"+str(z.complementario)+"\n reintegro:"+str(z.reintegro)+"\n Combinacion ganadora: "+numeros1)
        f.close()






def imprimirganadores(arrad):
    print("Imprimieendo...")
def salir(arrayd):
    print("saliendo")
def menu(arrayd):
    opc=0
    opciones={
        1:creararchivo,
        2:imprimirganadores,
        3:salir
    }
    while (opc!=3):
        opc=int(input("inserte opcion que desea ejecutar"))
        opciones[opc](arrayd)





print("sacando combinacion ganadora...")
arraybd =[]
d=datetime.now()
fecha=d.strftime("%Y-%m-%d")
print(fecha)
arraybd.append(fecha)
for i in range(1,8):
    arraybd.append(random.randint(1,49))
arraybd.append(random.randint(1,9))
c=Conexion("insert into ganadora values ('%s',%s,%s,%s,%s,%s,%s,%s,%s)" %tuple(arraybd))
menu(arraybd)




