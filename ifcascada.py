'''
if en cascada:
Estructura de control que permite 
evaluar varias condiciones en
cascada, es decir, si la primera
condicion no se cumple,
se evalua la siguiente
y así sucesivamente
'''
# ejemplo1:
# Modificar si el programa de votacion
# Para que considere la edad de 17
# años

edad = int(input("Ingresa tu edad: "))
if edad >=18:
    print("Puedes votar")
elif edad ==17:
    print("Puedes votar el proximo año")
elif edad < 17:
    print(" No puedes votar aun")
print ("Fin del programa")