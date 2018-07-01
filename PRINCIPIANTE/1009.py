# -*- coding: utf-8 -*-

COMISION = float(15)

name_saler = input()
salary = float(input())
total_sales = float(input())

total_salary = salary + (total_sales * (COMISION/100))

print("TOTAL = R$ %.2f" % total_salary)
