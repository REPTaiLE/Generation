#!/usr/bin/env python3

print("Bienvenido al comparador de números! \nPara jugar ingresa tres números")
print("----------------------------------------------------------------------")

n1 = int(input("Ingresa tu primer número: "))
n2 = int(input("Ingresa tu segundo número: "))
n3 = int(input("Ingresa tu tercer número: "))

orden = [n1, n2, n3]
orden.sort()

print("De mayor a menor: ", orden[2], " | ", orden[1],  " | ", orden[0])
print("De mayor a menor: ", orden[0], " | ", orden[1],  " | ", orden[2])

if (n1 == n2) and (n2 != n3):
    print(f"{n1} es igual a {n2}")
elif (n1 == n3) and (n1 != n2):
    print(f"{n1} es igual a {n3}")
elif (n2 == n3) and (n1 != n2):
    print(f"{n2} es igual a {n3}")
elif n1 == n2 == n3:
    print("Todos los números ingresados son iguales!")

