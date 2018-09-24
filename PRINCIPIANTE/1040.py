# -*- coding: utf-8 -*-

values = input().split(" ")
n1, n2, n3, n4 = values

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
media = round(media, 1)

print("Media: %.1f" % media)
if media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    nExame = float(input())
    print("Nota do exame: %.1f" % nExame)
    final = (media + nExame) / 2
    if final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % final)
elif media > 7.0:
    print("Aluno aprovado.")
