# -*- coding: utf-8 -*-

entradaDiaInicio = input().split("Dia ")
diaInicio = int(entradaDiaInicio[1])
horaInicio = [int(x) for x in input().split(" : ")]
entradaDiaFin = input().split("Dia ")
diaFin = int(entradaDiaFin[1])
horaFin = [int(x) for x in input().split(" : ")]

nDias = diaFin - diaInicio
nHoras = horaFin[0] - horaInicio[0]
if nHoras < 0:
    nHoras += 24
    nDias -= 1
nMinutos = horaFin[1] - horaInicio[1]
if nMinutos < 0:
    nMinutos += 60
    nHoras -= 1
nSegundos = horaFin[2] - horaInicio[2]
if nSegundos < 0:
    nSegundos += 60
    nMinutos -= 1

print("%d dia(s)" % nDias)
print("%d hora(s)" % nHoras)
print("%d minuto(s)" % nMinutos)
print("%d segundo(s)" % nSegundos)
