#comment one line
'''
    Author: miguel
    Date: 20/01/2023
'''
print("hellow from main.py")

#initialize variables
user_name = "miguel"
age = 19
gender = "m"
Is_active= True
height = 1.79
pets = ['Cats',"Niña","Luna"]

#Conditionals 
#shift tab arreglar la tabulacion (devolver la tavulacion)
if age > 17:
    print("Es Mayor de edad")
else:
    print("Es menor de edad")

#-------------------------

if gender == "M" or gender == "m":
    print("Masculino")
elif gender == "F" or gender == "f":
    print("Femenino")
elif gender == "NB" or gender == "nb" or gender == "Nb" or gender == "nB":
    print("No Binario")
elif gender == "SE" or gender == "se" or gender == "Se" or gender == "sE":
    print("Sin Espesificar")
else:
    print(">>> Obcion Invalida <<<")

'''
    Funciones con Texto: texto.lower() texto.upper() texto.capitalize()
        lower(): Convierte todo el texto en minuscula
        upper(): Convierte todo el texto en MAYUSCULA
        capitalize(): Primer caracter en MAYUSCULA y el resto en minuscula
'''
print(user_name)
print(user_name.lower())
print(user_name.upper())
print(user_name.capitalize())

#-------------------- code implements upper() function

if gender.upper() == "M":
    print("Masculino")
elif gender.upper() == "F":
    print("Femenino")
elif gender.upper() == "NB":
    print("No Binario")
elif gender.upper() == "SE":
    print("Sin Espesificar")
else:
    print(">>> Obcion Invalida <<<")

# Show list content
print(pets)
# Show list length, use the function len(lista)
print(len(pets))
# Interpolacion de mensajes 
    #concatenar texto f"" dentro de las comillas {} para variables
print(f"{user_name} tiene {age} años")
# Show content of specific index in list
print(pets[0])
print(pets[1])
print(pets[2])

#--------------------------- For Cicle -----------------------------

#iterar 10 veces
print("for 1:")
for i in range(0,10):
    print(i)
print("for 2:")
for i in range(10):
    print(i)
print("for 3:")
for i in range(1,11):
    print(i)

#--------------------------- While ---------------------------------

#iterar 10 veces
print("while 1:")
i = 0
while i<10:
    print(i)
    i+=1