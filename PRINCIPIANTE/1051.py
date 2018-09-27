# -*- coding: utf-8 -*-

salario = float(input())

if salario > 2000:
    if 2000.01 <= salario <= 3000:
        resto = salario - 2000
        taxes = resto * 0.08
    if 3000.01 <= salario <= 4500:
        resto = salario - 3000
        taxes = 80 + (resto * 0.18)
    if salario > 4500:
        resto = salario - 4500
        taxes = 350 + (resto * 0.28)
    print("R$ %.2f" % taxes)
else:
    print("Isento")
