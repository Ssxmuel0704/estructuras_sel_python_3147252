'''
Estructura de control if:
Se utiliza para tomar decisiones
basadas en expresiones condicionales
'''
#ejemplo 1: if SIMPLE
edad = int(input("Ingresa tu edad: "))
documento = input("Tienes documento?(si/no): ")
#condicional: si la edad es mayor 
if edad >= 18 and documento=='si':
    #codigo para cuando es mayor a 18
    print("Eres mayor de edad, puedes votar")
else:
    #codigo para cuando es menor a 18
    print("Eres menor de edad o no tienes documento, no puedes votar")
#codigo que se ejecuta siempre
print("Fin del programa")