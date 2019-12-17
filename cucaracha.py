import os

def menu():
    os.system('clear')
print ("Seleccione una opcion")
print ("1-reproducir")
print ("2-aplastar")
print ("3-rociar")
print("salir")

class cucaracha: 

def __init__(self, cantidad, reproducir, aplastar, rociar):
    self.cantidad   = cantidad
    self.reproducir = reproducir 
    self.aplastar   = aplastar
    self.rociar     = rociar 

accion =  cucaracha()
accion.cantidad = 5 

def repr(self):
    self.reproducir = self.cantidad +  input("cuanto desea reproducir" )

def apl(self):
    self.aplastar = self.cantidad - 1 

def roc(self):
    self.rociar = input("cantidad que desea rociar"  - self.cantidad)


while true:

menu()

    opcion =input("eliga una opcion ") 

if opcion == "1":
    print("reproducion" accion.repr())
if opcion == "2":
    
    print("aplastar" accion.apl())

if opcion == "3":

print("rociar" accion.roc())

if opcion == "4":
    break 
else: 
    print("")
    input("no se eligio ninguna opcion")
    



 
