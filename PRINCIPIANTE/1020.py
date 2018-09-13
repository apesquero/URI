# -*- coding: utf-8 -*-

dias = int(input())

anos = dias / 365
diasRestantes = dias % 365
meses = diasRestantes / 30
diasRestantes = diasRestantes % 30

print("%d ano(s)" % anos)
print("%d mes(es)" % meses)
print("%d dia(s)" % diasRestantes)
