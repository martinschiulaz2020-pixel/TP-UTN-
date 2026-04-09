

# Random / Aleatorio
# Imports arriba de todo el archivo.
import random


# PERMITIDO
# Funciones
# print()
# input()
# id()

# Cuasi funciones 
# type()
# int()
# str()
# bool()
# float()
# Python: snake_case
# nota_aleatoria = random.randint(1, 10) # Genero un numero entre 1 y 10 INCLUSIVE.
# print(nota_aleatoria)
# nota_1 = 10
# nota_uno = 7


# PROHIBIDO PARA EL PRIMER EXAMEN PARCIAL!!!!!!!!!! METODOS y Algunas funciones genericas de Python
# .lower()
# .cualquiercosa()
# min()
# max()
# JavaScript / Java: lowerCamelCase 
# costoConsumoMaximo = 5
# PascalCase
# CostoConsumoMaximo = 10





# if valor_inicial:
#     print("Entro")
# else:
#     print("Else")



# break: ROMPE el bucle mas proximo.

# suma_notas = 0
# seguir = "S"

# while True:
#     # Bloque de codigo del bucle while.
#     nota_ingresada = int(input("Ingrese la nota de un alumno: "))
#     suma_notas += nota_ingresada
#     seguir = input("Desea seguir ingresando notas? S/N: ")
#     if seguir == "N":
#         break

# while seguir != "N": # seguir == "S"
#     # Bloque de codigo del bucle while.
#     nota_ingresada = int(input("Ingrese la nota de un alumno: "))
#     suma_notas += nota_ingresada
#     seguir = input("Desea seguir ingresando notas? S/N: ")

# print("Suma de notas: ", suma_notas)

# while True:
#     while True:
#         if True:
#             print("Entro")
#             match seguir:
#                 case "N":
#                     while True:
#                         break
#         else:
#             print("No entro")
#             break
#     break




# continue: se saltea una iteracion. (Sirve para cualquier bucle)

# contador = 0

# while contador < 10:
#     contador += 1 # 5
#     if contador % 2 == 0: # El contador es par?
#         continue
#     print(contador) # 1, 3, 5
    






# Calcular la nota promedio de un curso de 10 alumnos.

# nota_uno = int(input("Ingrese la nota del 1° alumno: "))
# nota_dos = int(input("Ingrese la nota del 2° alumno: "))
# nota_tres = int(input("Ingrese la nota del 3° alumno: "))
# nota_cuatro = int(input("Ingrese la nota del 4° alumno: "))
# nota_cinco = int(input("Ingrese la nota del 5° alumno: "))
# nota_seis = int(input("Ingrese la nota del 6° alumno: "))
# nota_siete = int(input("Ingrese la nota del 7° alumno: "))
# nota_ocho = int(input("Ingrese la nota del 8° alumno: "))
# nota_nueve = int(input("Ingrese la nota del 9° alumno: "))
# nota_diez = int(input("Ingrese la nota del 10° alumno: "))


# suma_notas = nota_uno + nota_dos + nota_tres + nota_cuatro + nota_cinco + nota_seis + nota_siete + nota_ocho + nota_nueve + nota_diez

# promedio = suma_notas / 10

# print(f"La nota promedio del curso es de {promedio}")


# PROMEDIOS
# cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
# notas_ingresadas = 0
# suma_notas = 0

# while notas_ingresadas < cantidad_alumnos:   #      5 + 1
#     # nota = int(input(f"Ingrese la nota del {notas_ingresadas + 1}° alumno: "))
#     notas_ingresadas += 1
#     nota = int(input(f"Ingrese la nota del {notas_ingresadas}° alumno: "))
#     suma_notas += nota

# if cantidad_alumnos != 0:
#     promedio = suma_notas / cantidad_alumnos
#     print(f"La nota promedio del curso es de {promedio}")
# else:
#     print("Error, no hay alumnos.")





# PORCENTAJES
# Determinar que porcentaje de alumnos aprobo la materia, sobre el total de alumnos.

# aprobados = 3
# desaprobados = 4
# total_alumnos = aprobados + desaprobados
# procentaje_aprobados = aprobados * 100 / total_alumnos

# #                                                          varible:.cant de decimales f
# print(f"El porcentaje de alumnos aprobados fue de {procentaje_aprobados:.2f}%.")
# varible:.0f  -> Ocultamos todos los digitos despues del punto.
# varible:.4f  -> Mostramos los primeros 4 dititos despues del punto.
# Tambien podriamos castear el resultado a entero.
# O podriamos utilizar la // para obtener el valor entero.

# Aplicar un porcentaje sobre un valor.
# precio = 1000
# iva = 1.21 # 0 - 1, 21% 
# precio_con_iva = precio * (1 + iva)
# precio_con_iva = precio * iva






# Validaciones. TODOS los valores provenientes del input(), tienen que ser VALIDADOS!
# SIEMPRE CON BUCLE WHILE.

# cant_alumnos = 5 # HardCode 
# cant_alumnos_ingresado = int(input("Ingrese la cantidad de alumnos: "))

# Ingresar al sistema con una contraseña.
# contrasenia = "UTN750" # qkjdhquiqwbdhuTAdwq21312djqwdqwd_123dhdbquy1g2_
# mensaje = "Ingrese la contraseña: "

# contrasenia_ingresada = input(mensaje)
# # En las validaciones se esta buscando el ERROR
# while contrasenia_ingresada != contrasenia:
#     contrasenia_ingresada = input(f"Error, re{mensaje}")

# contrasenia_ingresada = ""
# # En las validaciones se esta buscando el ERROR
# while contrasenia_ingresada != contrasenia:
#     contrasenia_ingresada = input(mensaje)





# Validacion de Rangos numericos.
# Validar la nota ingresada (entre 1 y 10).
nota_ingresada = int(input("Ingrese una nota: "))
# if nota_ingresada > 1 and nota_ingresada < 10:
#     print("Nota correcta")
# else:
#     print("Nota invalida")

# while not (nota_ingresada > 1 and nota_ingresada < 10):
while nota_ingresada < 1 or nota_ingresada > 10:
    nota_ingresada = int(input("Error, reingrese una nota entre 1 y 10: "))



print("Bienvenido al programa.", nota_ingresada)


