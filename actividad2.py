'''
'''
estado_civil = input("Ingresa tu estado civil:(soltera/casada/comprometida)")
edad = int(input("Ingresa tu edad: "))
temperamento = input("Ingresa tu temperamento:(buena persona/mala persona)")
fisico = input("Ingresa tu fisico:(linda/a/fea)")

if estado_civil == "casada" or estado_civil =="comprometida":
    print("No puedes acercarte a esa persona")
elif edad < 18:
    print("No puedes acercarte a esa persona, porque no tiene la edad suficiente")
elif temperamento == "mala persona":
    print ("No puedes acercarte a esa persona, porque te generaria stress")
elif fisico == "fea":
    print("No puedes acercarte a esa persona, porque no le atraes fisicamente")
else:
    print("Puedes acercarte a esa persona")
print("Fin del programa")    