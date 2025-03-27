'''
Actividad 3:
Escribir programa
que calcule el salrio neto 
de un trabajador
despues de descuentos
y bonificaciones
=> INICIALMENTE, el programa
dbe solicitar un tipo de
trabajor entre los siguientes:
a - Contrato a termino indefinido
b - Contrato por prestacion de 
    servicios
c - Contrato de aprendizaje
d - Jornal
=> Jornal:
   Se debe solicitar:
   - el tipo de unidad a pagar
   - el numero de unidades hechas
   - el valor de la unidad
   el salario se calcula como
   el valor_unidad * numero_unidades
   si el numero de unidades es mayor a 100
   si le da una bonificacion del 10%
=> Contrato de aprendizaje:
   Se debe solicitar  el salario minimo
   el salario neto es
   el 75% del salario minimo
=> Contrato por prestacion de servicios:
   Se debe solicitar:
   - el valor del contacto
   - el numero de meses trabajados
   - antiguedad en la empresa 
   Se calcula el dividendo el valor del contrato 
   entre el numero de meses trabajados
=> Bonificaciones
   - Si la antiguedad es menor a 2 años
     se le aumenta el 2% al salario mensual 
   - Si la antiguedad esta entre 2 y 5 años
     se le aumenta el 5% al salario mensual
   - Si la antiguedad es mayor a 5 años
     se le aumenta el 10% al salario mensual
   Descuentos de ley
   - 8% de salud
   - 10% de pension 
   - 1% de caja de compensacion
   => contrato a termino indefinido
   el salario mensual se calcula
   con base en la siguiente tabla
   de escalafones o grados:
   - 1: 1.5 veces el SMLV 
   - 2: 1.7 veces el SMLV
   - 3: 2 veces el SMLV
   - 4: 2.5 veces el SMLV
   - 5: 3 veces el SMLV
   el programa debe solicitar
   el escalafon o grado
   del empleado 
   - las bonificaciones y 
   descuentos de ley son las mismas 
   que en el caso b
'''
#variable global:
#variable que puede ser reconocida
#y asignada en cualquier parte del
#programa
#NOTA: se recomienda inicializar
#definir y dar valor inicial a las 
#variables globales al principio
#del programa
#Ejemplo de esto son las variables
#para  almacenar resultados finales 

salario_neto = 0

tipo_empleado = input("Ingrese el tipo de empleado (a, b, c, d): ")
if tipo_empleado == "a":
    print("Ha ingresado contrato a término indefinido")
    SMLV = int(input("Ingrese SMLV:"))
    escalafon = int(input("Ingrese el escalafón:"))
    if escalafon == 1:
        salario_mensual = 1.5 * SMLV 
    elif escalafon == 2: 
        salario_mensual = 1.7 * SMLV 
    elif escalafon == 3:
        salario_mensual = 2 * SMLV 
    elif escalafon == 4:
        salario_mensual = 2.5 * SMLV 
    elif escalafon == 5:
        salario_mensual = 3 * SMLV 
    salario_neto = salario_mensual
    antiguedad = int(input("Ingrese la antigüedad en la empresa: "))
    bonificacion = 0
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif antiguedad >= 2 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    elif antiguedad > 5:
        bonificacion = salario_mensual * 0.10
    salario_mensual += bonificacion
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja = salario_mensual * 0.01
    salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja + bonificacion

elif tipo_empleado == "b":
    print("Ha ingresado prestación de servicios")
    valor_contrato = int (input("Ingrese el valor del contrato: "))
    numero_meses = int (input("Ingrese el numero de meses trabajados: "))
    antiguedad = int (input("Ingrese la antiguedad en la empresa: "))
    salario_mensual = valor_contrato / numero_meses
    #bonificaciones : elif anidados
    bonificacion = 0 
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif antiguedad >= 2 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    elif antiguedad > 5:
        bonificacion = salario_mensual * 0.10
    #Refactorizacion
        salario_mensual = salario_mensual + bonificacion
    #Descuentos
        descuento_salud = salario_mensual * 0.08
        descuento_pension = salario_mensual * 0.10
        descuento_caja = salario_mensual * 0.01
        salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja + bonificacion
        
elif tipo_empleado == "c":
    print("Ha ingresado contrato de aprendizaje")
    salario_minimo = int(input("Ingrese el salario minimo: "))
    descuento = salario_minimo * 0.25
    salario_neto = salario_minimo - descuento
    
elif tipo_empleado == "d":
    print("Ha ingresado jornal")
    #variables locales
    #variables que solo pueden ser
    #reconocidas y asignadas en un bloque
    #de codigo especifico
    tipo_unidad = input("Ingrese el tipo de unidad ")
    numero_unidades = int(input("Ingrese el numero de " + tipo_unidad + " hechas: "))
    valor_unidad = int(input("Ingrese el valor de: "+ tipo_unidad ))
    salario_neto = numero_unidades * valor_unidad
else:
    print("Tipo e empleado no valido")
#mostar salario neto
print("El salario neto es: ", salario_neto)
print("Fin del programa")