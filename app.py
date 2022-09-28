from operator import truediv
import os
import math

#operaciones
def suma(numero1, numero2):
    return numero1 + numero2
    
def resta(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2
    
def division(numero1, numero2):
    return numero1 / numero2

def primo(numero1):
    for numeros in range(2,numero1):
        if (numero1%numeros) == 0:
            return False
    return True

def palindromo(palabra):
    if str(palabra) == str(palabra)[::-1] :
        print("Palindrome")
    else:
        print("Not Palindrome")

input()
os.system('cls')
while True:
    #Se imprime el menu en consola
    print("Calculadora")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Verificar si es primo")
    print("6 - Verificar si es palindromo")
    opcion = input("Ingrese el numero de la operacion a realizar: ")

    #Funcion de Suma
    if opcion =="1":
        numero1 = float(input("numero 1 : "))
        numero2 = float(input("numero 2 : "))

        print("")
        print("El resultado es ",suma(numero1, numero2))
        print("")

    #Funcion de Resta
    if opcion =="2":
        numero1 = float(input("numero 1 : "))
        numero2 = float(input("numero 2 : "))

        print("")
        print("El resultado es ",resta(numero1, numero2))
        print("")

    #Funcion de Multiplicar
    if opcion =="3":
        numero1 = float(input("numero 1 : "))
        numero2 = float(input("numero 2 : "))

        print("")
        print("El resultado es ",multiplicar(numero1, numero2))
        print("")

    #Funcion de Division
    if opcion =="4":
        numero1 = float(input("numero 1 : "))
        numero2 = float(input("numero 2 : "))

        print("")
        print("El resultado es ",division(numero1, numero2))
        print("")

    #Funcion de verificar si es primo
    if opcion =="5":
        numero1 = int(input("numero 1 : "))
        if primo(numero1):
            print("Es primo")
        else:
            print("No es primo")

     #Funcion de Palindromo
    if opcion =="6":
        palabra = input("Numero : ")
        palindromo(palabra)