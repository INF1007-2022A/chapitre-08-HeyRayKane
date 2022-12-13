# import os
# import json
# import csv

# def ecrire1(nom_fichier, donnees: str):
#     with open(nom_fichier, "w", encoding="UTF-8") as f:
#         print(donnees, file=f, end="")
#
# ecrire1("etudiant.txt", "je suis la meilleure personnes ever, lol\n pas toi")

# def ecrire2(nom_fichier, donnees: str):
#     with open(nom_fichier, "wb") as f:
#         f.write(bytes(donnees.replace("\n", os.linesep), encoding="UTF-8"))
#
# ecrire2("etudiant.txt", "je suis la meilleure personnes ever, lol\n pas toi")

# def division():
#     try:
#         "2" / "0"
#     except ZeroDivisionError:
#         print("impossible")
#     except Exception:
#         print("lol")
#     except TypeError:
#         print("erreur")
#     except ArithmeticError:
#         print("arith")
#     except:
#         print("elle est ici")
#     finally:
#         print('fini')
#
# division()

# class Dual:
#     def __init__(self, a, b=0):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         if self.b != 0:
#             return str(self.a) + ' + ' + str(self.b) + ' e'
#         else:
#             return str(self.a)
#
#     def __add__(self, autre):
#         return Dual(self.a + autre.a, self.b + autre.b)
#
#     def __sub__(self, autre):
#         return Dual(self.a - autre.a, self.b - autre.b)
#
#     def __mul__(self, autre):
#         return Dual(self.a * autre.a, self.a * autre.b + self.b * autre.a)
#
#     def __truediv__(self, autre):
#         return Dual(self.a / self.a, ((self.b * autre.a) - (self.a * autre.b)) / (autre.a ** 2))
#
# k = Dual(1, 2)
# m = Dual(1, -2)
# print(k + m)
# print(k/m)
# print(k-m)

# with open("fichier", 'r') as f:
#     donnees = json.load(f)
#
# with open("fichier.csv", "w", newline="") as g: #attention au nom du fichier
#     ecriture_nombre = csv.writer(g, delimiter=',') # lineterminator="" pour coller tout
#     ecriture_nombre.writerow(["reel", "imaginaire"])
#     for nombre_complexe in donnees:
#         ecriture_nombre.writerow(nombre_complexe)
#
#
# with open('data.json', 'r') as f1, open('data.csv', 'w') as f2:
#     data = json.load(f1)
#     writer = csv.writer(f2, delimiter=',')
#     writer.writerow(['reel', 'imaginaire'])
#     for d in data:
#         writer.writerow(d)

# import matplotlib.pyplot as plt
# import numpy as np


# def create_plot():
#     x = np.arange(15)
#     y1 = x
#     y2 = x ** 2
#
#     plt.plot(x, y1)
#     plt.plot(x, y2)
#     plt.scatter(x, y1)
#     plt.show()
#
# create_plot()

# def write_something(file="some_file.txt"):
#     with open(file, "w", encoding="utf-8") as f:
#         f.write("Pas besoin de chance quand on a étudié!")
#         f.write("Mais merci quand même!")
# write_something("fichier")

# class Personnage:
#     def __init__(self, nom, niveau, force):
#         self.nom = nom
#         self.niveau = niveau
#         self.force = force
#
#
# goku = Personnage(**json.load(open("fichier", "r"))[1])

# def charger_pokemons_csv(nom_fichier):
#     # TODO: Lire le fichier CSV et mettre les données dans un dictionnaire où
#     #       la clé est le nom du Pokémon et la valeur est la liste de ses
#     #       stats (toutes les colonnes qui suivent le nom). Il faut que les stats
#     #       soient des entiers dans la liste (il faut faire la conversion si nécessaire).
#     dictionnaire = dict()
#     with open(nom_fichier) as fichier_csv:
#         lecteur_csv = csv.reader(fichier_csv, delimiter=",")
#         for ligne in lecteur_csv:
#             dictionnaire[ligne[0]] = [int(i) for i in ligne[1:]]
#     return dictionnaire
#
# pkmn = charger_pokemons_csv("fichier.csv")
# print(isinstance(pkmn, dict))
# print(isinstance(pkmn["Pikachu"], list))
# print(isinstance(pkmn["Pikachu"][0], int))
# for nom, stats in pkmn.items():
#     print(f"{nom}: {stats}")

import unittest


def trouver_index(liste, valeur):
    for i, elem in enumerate(liste):
        if elem == valeur:
            return i

print(trouver_index([], 42))

class MonTest(unittest.TestCase):
    def setUp(self):
        self.valeur = 42 # La valeur à trouver
        self.liste_present_debut = [self.valeur, 69, 0xDEAD, 9000]
        self.liste_present_milieu = [69, 0xDEAD, self.valeur, 9000, 0xB00]
        self.index_present_milieu = 2
        self.liste_absent = [0xC0FFEE, 0xBABE, 0xBADBEEF]

    def test_present_debut(self):
        # TODO: Tester la fonction avec une liste dans laquelle la valeur
        #       se trouve au premier élément.
        self.assertEqual(0, trouver_index(self.liste_present_debut, self.valeur))

    def test_present_milieu(self):
        # TODO: Tester la fonction avec une liste dans laquelle la valeur
        #       se trouve au milieu.
        self.assertEqual(self.index_present_milieu, trouver_index(self.liste_present_milieu, self.valeur))

    def test_absent(self):
        # TODO: Tester la fonction avec une liste dans laquelle la valeur
        #       est absente.
        self.assertEqual(-1, trouver_index(self.liste_absent, self.valeur))

    def test_vide(self):
        # TODO: Tester la fonction avec une liste vide.
        self.assertEqual(-1, trouver_index([], self.valeur))
