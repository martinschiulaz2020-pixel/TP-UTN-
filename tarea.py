

""" 
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota
 es ...
"""
# primer punto
"""
altura_minima = 160
altura = float(input( "ingrese su altura: "))

if altura <= 160:
    print("usted juega de base")

elif altura > 160 and altura < 179:
    print("usted juega de escolta")

elif altura >= 180:
    print("usted juega de Pivot")
"""
# segundo punto
"""
import random

# Generar nota aleatoria entre 1 y 10
nota = random.randint(1, 10)

# Evaluar la nota
if nota >= 6:
    print(f"Promoción directa, la nota es {nota}")
elif nota >= 4:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")
"""



# tercer punto
"""
estacion = input("que estacion desea viajar, verano, otoño, primavera, invierno: ")
match estacion:
    case "verano":
        print("se viaja a Mar del plata y Cataratas.")
    case "invierno":
        print("solo se viaja a Bariloche.")
    case "otoño":
        print("se viaja a todos los lugares.")
    case "primavera":
        print("se viaja a todos los lugares menos Bariloche.")
    case _:
        print("no elegio ninguna estacion.")
"""

# cuarto punto

"""
tarifa_base = 7000
metro_cubico = int(input("ingrese la cantidad de metros cubicos usados: "))
tipo_cliente = input("ingrese su tipo de cliente, residencial, inustrial, comercial: ")

match tipo_cliente:
    case "residencial":
        if metro_cubico < 30:
            consumo_total = metro_cubico * 200
            bonificacion = (consumo_total * 10 ) / 100
            print("se le aplicara la siguiente bonificacion $", bonificacion)
            consumo_bonificado = consumo_total - bonificacion
            print("su total bonificado es de:$", consumo_bonificado)
            total_abonar = consumo_bonificado + tarifa_base
            print("total abonar (con consumo fijo) es:$", (total_abonar * 5) / 100)
        elif metro_cubico > 80:
            consumo_total = metro_cubico * 200
            recargo = (consumo_total * 15 ) / 100
            print("se le aplicara el siguiente recargo $", recargo)
            consumo_recargo = consumo_total + recargo
            print("su total con recargo es de:$", consumo_recargo)
            total_abonar = consumo_recargo + tarifa_base
            print("total abonar es :$", (total_abonar * 5) / 100)
    case "comercial":
        if metro_cubico > 150:
            consumo_total = metro_cubico * 200
            bonificacion = (consumo_total * 8) / 100
            print("se le aplicara la siguiente bonificacion $", bonificacion)
            consumo_bonificado = consumo_total - bonificacion
            print("su total bonificado es de:$", consumo_bonificado)
            total_abonar = consumo_bonificado + tarifa_base
            print("total abonar (con consumo fijo) es:$", total_abonar)
        elif metro_cubico > 300:
            consumo_total = metro_cubico * 200
            bonificacion = (consumo_total * 12 ) / 100
            print("se le aplicara la siguiente bonificacion $", bonificacion)
            consumo_bonificado = consumo_total - bonificacion
            print("su total bonificado es de:$", consumo_bonificado)
            total_abonar = consumo_bonificado + tarifa_base
            print("total abonar (con consumo fijo) es:$", total_abonar)
        elif metro_cubico < 50:
            consumo_total = metro_cubico * 200
            recargo = (consumo_total * 5 ) / 100
            print("se le aplicara el siguiente recargo $", recargo)
            consumo_recargo = consumo_total + recargo
            print("su total con recargo es de:$", consumo_recargo)
            total_abonar = consumo_recargo + tarifa_base
            print("total abonar es :$", total_abonar)
    case "industrial":
        if metro_cubico > 500:
            consumo_total = metro_cubico * 200
            bonificacion = (consumo_total * 20 ) / 100
            print("se le aplicara la siguiente bonificacion $", bonificacion)
            consumo_bonificado = consumo_total - bonificacion
            print("su total bonificado es de:$", consumo_bonificado)
            total_abonar = consumo_bonificado + tarifa_base
            print("total abonar (con consumo fijo) es:$", total_abonar)
        elif metro_cubico > 1000:
            consumo_total = metro_cubico * 200
            bonificacion = (consumo_total * 30) / 100
            print("se le aplicara la siguiente bonificacion $", bonificacion)
            consumo_bonificado = consumo_total - bonificacion
            print("su total bonificado es de:$", consumo_bonificado)
            total_abonar = consumo_bonificado + tarifa_base
            print("total abonar (con consumo fijo) es:$", total_abonar)
        elif metro_cubico < 200:
            consumo_total = metro_cubico * 200
            recargo = (consumo_total * 10 ) / 100
            print("se le aplicara el siguiente recargo $", recargo)
            consumo_recargo = consumo_total + recargo
            print("su total con recargo es de:$", consumo_recargo)
            total_abonar = consumo_recargo + tarifa_base
            print("total abonar es :$", total_abonar)
"""


