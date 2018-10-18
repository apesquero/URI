# -*- coding: utf-8 -*-

inter = 0
gremio = 0
empates = 0

grenais = 0

while True:
    grenais += 1
    valores = [int(x) for x in input().split(" ")]
    gInter, gGremio = valores
    if gInter > gGremio:
        inter += 1
    elif gInter < gGremio:
        gremio += 1
    else:
        empates += 1
    print("Novo grenal (1-sim 2-nao)")
    option = int(input())
    if option == 2:
        break

print("%d grenais" % grenais)
print("Inter:%d" % inter)
print("Gremio:%d" % gremio)
print("Empates:%d" % empates)

if inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
