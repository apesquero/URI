# -*- coding: utf-8 -*-

lista = []

while True:
    password = int(input())
    lista.append(password)
    if password == 2002:
        break

for password in lista:
    if password == 2002:
        print("Acesso Permitido")
    else:
        print("Senha Invalida")
