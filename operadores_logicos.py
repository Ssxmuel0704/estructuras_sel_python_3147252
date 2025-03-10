'''
Operadores Logicos

Aquellos que operan unicamente
con valores booleanos (V F)
Acorde a las tablas de Verdad
'''
#Ejemplo 1: operador not:
y = not True
print ("El resultado de operar con not es" , y)

#Ejemplo 2: operador and:
y = False and True
print("El resultado de operar con and es" , y)


#ejemplo 3: Operador or
y = False or True
print("El resultado de operar con or es" , y)

'''
Jerarquía de predencia
1.          ()
2.          **
3.      *, /, %,
4.          +, -
5.    >, <, >=, <=, != , ==
6.          not
7.          and
8.          or
9.           =
'''
#ejemplo 4: Jerarquía de operadores:
y = False and not True or False
print ("El resultado de operar con jerarquía de operadores es" ,y)

#ejemplo 5: Operadores relacionales y logicos:
y = not 3 > 4 and 4 == 4 or 3 < 2
