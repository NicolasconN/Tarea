# -*- coding: utf-8 -*-
"""5.2.- Tarea.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jt6nS6-oN4N7jtEca4frfrHtop6kH0K1
"""

# Tarea 1
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

import string


p_payasos =  112
p_muñecas = 75

c_payasos = input("Ingrese la cantidad de payasos comprados: ")
c_muñecas = input("Ingrese la cantidad de muñecas compradas: ")

if((c_payasos) == 0 and int(c_muñecas) == 0):
 print ("No se realizaron ventas de payasos ni de muñecas")
elif ((c_payasos) > 0 and (c_muñecas) => 0 or (c_muñecas) > 0 and (c_payasos) => 0):
PesoTotal = (int(c_payasos) * p_payasos) + (int(c_muñecas) * p_muñecas))
PesoTotal = str(PesoTotal)
 print ("Se vendio la cantidad de " + c_payasos + " payasos y "+ c_muñecas +" muñecas, con un peso total de "+ PesoTotal+" gramos")



# Tarea 2
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


peso = float(input("Ingrese su peso medido en kilogramos: "))
altura = float(input("Ingrese su altura medido en metros: "))

if(peso <= 0):
    print("Su peso no es valido")
elif(altura <= 0):
    print("Su altura no es valida")
else:
    imc = (peso / pow(altura,2))
    imc = round(imc, 2)

print("Tu índice de masa corporal es " + str(imc))

"""# Sección nueva"""

