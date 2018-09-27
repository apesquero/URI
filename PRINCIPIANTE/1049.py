# -*- coding: utf-8 -*-

nivel1 = str(input())
nivel2 = str(input())
nivel3 = str(input())

nivelA = {"vertebrado": 100, "invertebrado": 200}
nivelB = {"ave": 10, "mamifero": 20, "inseto": 30, "anelideo": 40}
nivelC = {"carnivoro": 1, "onivoro": 2, "herbivoro": 3, "hematofago": 4}

animal = {111: "aguia", 112: "pomba", 122: "homem", 123: "vaca",
             234: "pulga", 233: "lagarta", 244: "sanguessuga", 242: "minhoca"}

valorAnimal = nivelA[nivel1] + nivelB[nivel2] + nivelC[nivel3]

print(animal[valorAnimal])
