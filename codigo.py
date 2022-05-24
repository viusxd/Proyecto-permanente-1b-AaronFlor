import random
import string
import time


def minusculas():
    return random.choice(string.ascii_lowercase)


def mayusculas():
    return random.choice(string.ascii_uppercase)


def simbolos():
    sim = ["@", "!", "$", "&", "."]
    return str(random.choice(sim))


def nums():
    return str(random.randint(1, 20))


def nums19():
    return str(random.randint(1, 9))


def menu():
    texto1 = "Bienvenido al generador de contraseñas"
    longi = len(texto1) * "-"

    print(longi)
    print(texto1)
    print(longi)

def st():
    return time.sleep(0.5)


def bucleopc():
    opc = None

    while opc == None:

        print("Elija la acción a realizar:"
              "\n 1. Generar contraseña aleatoria"
              "\n 2. Generar PIN de 4 números"
              "\n 3. Descifrar"
              "\n 4. Salir")
        opc = input("Opción: ")
        if opc == "1":
            Fcontra()
            st()
            print("¿Qué desea hacer?")
            st()
            bucleopc()
        elif opc == "2":
            print("Tu pin de 4 números es: {}".format(PIN4()))
            st()
            print("¿Que desea hacer?")
            st()
            bucleopc()

        elif opc == "3":
            st()
            des_num()

        elif opc == "4":
            print("Hasta luego.")
            st()
            print(":(")
            break

        else:
            print("No es un opción válida")
            opc = None


longitud_pss = random.randint(7, 11)


def Fcontra():
    global longitud_pss
    contra = []
    cont_final = []

    for i in range(longitud_pss):
        defs = [minusculas, mayusculas, simbolos, nums19]
        d_index = random.randint(0, 3)
        contra.append(defs[d_index]())
        cont_final = "".join(contra)

    st()
    return print("Tu contraseña es: {}".format(cont_final))


def PIN4():
    pin4 = []
    p4f = []
    for i in range(4):
        pin4.append(nums19())
        p4f = "".join(pin4)
    return p4f

def det_num():

    pinD = 0
    numdes = 0
    while numdes == 0:
        print("Desea crear o generar un PIN"
                       "\n1. Crear"
                       "\n2. Generar")
        numdes = input("Opción: ")

        while numdes == "1":
            try:
                pinD = int(input("Introduzca su PIN: "))
                tam_pinD = len(str(pinD))
            except ValueError:
                print("El PIN debe contener sólo numeros.")
                continue

            if tam_pinD >= 5 or tam_pinD <= 3:
                print("El PIN debe ser de 4 cifras")
                numdes = "1"
            elif tam_pinD <= 4:
                print("Tu PIN es: "+ str(pinD))
                return pinD

        if numdes == "2":
            pinD = PIN4()
            print("Tu PIN es: " + str(pinD))
            return str(pinD)

        else:
            print("No es una opcíon válida.")
            numdes = 0
            time.sleep(1)

def des_num():
    numE = int(det_num())
    Fnum = 0

    print("El numero es "+ str(numE))
    time.sleep(2)

    while Fnum != numE:
        Fnum = random.randint(1000, 9999)
        print(Fnum)
    print("Tu PIN es "+ str(numE))

menu()
time.sleep(1)
bucleopc()
