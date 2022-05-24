# Generador

El presente proyecto esta hecho principalmente para generar contraseñas con diferentes carácteres y un PIN de 4 números.
Adicional, realicé un descifrador de PIN de 4 números, la cantidad de números puede aumentar pero esta enfocado en sólo 4.

## Tecnologías
Es bueno saber la versión que se usó cuando el código funcionaba exactamente como debía. 

* Python 3.10
```python
import random
import string
import time
```

¿Por qué? En primer lugar, será útil cuando se inicie el código, import random nos ayuda a generar un numero aleatorio, import string genera cadenas de carácteres, como letras del abecedario en mayúsculas y minúsculas.


## Cómo usar

```python
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
```

El código inicia con un menú, cada opción lleva a diferente código, si se desea generar una contraseña difucultosa, un PIN de 4 números y una opción para poder descifrar un PIN generado o creado por el usuario.

