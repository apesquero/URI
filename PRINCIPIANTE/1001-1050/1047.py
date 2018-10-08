# -*- coding: utf-8 -*-

values = input().split(" ")
a, b, c, d = values

a = int(a)
b = int(b)
c = int(c)
d = int(d)

horas = c - a
minutos = d - b

if horas < 0:
    horas += 24

if minutos < 0:
    minutos += 60
    horas -= 1

if horas == minutos == 0:
    horas = 24
    minutos = 0

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas, minutos))
