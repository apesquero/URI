# -*- coding: utf-8 -*-

valor_1 = input().split(" ")
valor_2 = input().split(" ")

code_1, und_1, price_1 = valor_1
code_2, und_2, price_2 = valor_2

code_1 = int(code_1)
und_1 = int(und_1)
price_1 = float(price_1)

code_2 = int(code_2)
und_2 = int(und_2)
price_2 = float(price_2)

total_price = (und_1 * price_1) + (und_2 * price_2)

print("VALOR A PAGAR: R$ %.2f" % total_price)
