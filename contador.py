from contBin import *
from contOctal import *
from contHexa import *


    
    
               


def main():
    print("¿En qué sistema deseas contar?")
    print("1. Binario")
    print("2. Octal")
    print("3. Hexadecimal")
    
    opcion = input("Selecciona una opción (1/2/3): ")
    numero = int(input("Hasta qué número deseas contar: "))
    
    if opcion == '1':
        x= Binario
        return x.contar_en_binario(numero)
    elif opcion == '2':
        x= Octal
        return x.contar_en_octal(numero)
    elif opcion == '3':
       x= Hexadecimal
       return x.contar_en_hexadecimal(numero)
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()




