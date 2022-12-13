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

#import unittest


# def trouver_index(liste, valeur):
#     for i, elem in enumerate(liste):
#         if elem == valeur:
#             return i
#
# print(trouver_index([], 42))
#
# class MonTest(unittest.TestCase):
#     def setUp(self):
#         self.valeur = 42 # La valeur à trouver
#         self.liste_present_debut = [self.valeur, 69, 0xDEAD, 9000]
#         self.liste_present_milieu = [69, 0xDEAD, self.valeur, 9000, 0xB00]
#         self.index_present_milieu = 2
#         self.liste_absent = [0xC0FFEE, 0xBABE, 0xBADBEEF]
#
#     def test_present_debut(self):
#         # TODO: Tester la fonction avec une liste dans laquelle la valeur
#         #       se trouve au premier élément.
#         self.assertEqual(0, trouver_index(self.liste_present_debut, self.valeur))
#
#     def test_present_milieu(self):
#         # TODO: Tester la fonction avec une liste dans laquelle la valeur
#         #       se trouve au milieu.
#         self.assertEqual(self.index_present_milieu, trouver_index(self.liste_present_milieu, self.valeur))
#
#     def test_absent(self):
#         # TODO: Tester la fonction avec une liste dans laquelle la valeur
#         #       est absente.
#         self.assertEqual(-1, trouver_index(self.liste_absent, self.valeur))
#
#     def test_vide(self):
#         # TODO: Tester la fonction avec une liste vide.
#         self.assertEqual(-1, trouver_index([], self.valeur))


# class Point:
#     def __init__(self, x=30, y=40):
#         self.x = x
#         self.y = y
#
#     def __sub__(self, other):
#         self.x -= other.x
#         self.y -= other.y
#
#     # def __str__(self):
#     #     return str(self.x) + str(self.y)
#
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"
#
# point1 = Point()
# point2 = Point(10, 20)
# point3 = point1 - point2
#
# print(point1)
# print(point3)

# import unittest
#
#
# def est_premier(nombre):
#     for i in range(2, int(round(nombre/2)) + 1):
#         if nombre % i == 0:
#             return False
#     return True
#
#
# class TestEstPremier(unittest.TestCase):
#     def setUp(self):
#         # Des valeurs de nombres premiers et non-premiers à utiliser dans les tests.
#         self.nombres_negatifs = [-1, -2, -4, -69]
#         self.nombres_premiers = [2, 3, 421]
#         self.nombres_non_premiers = [4, 6, 69]
#
#     # TODO: Méthode test_zero_un
#     #       Tester que 0 et 1 ne sont pas premiers (est_premier retourne false)
#     def test_zero_un(self):
#         self.assertFalse(est_premier(0))
#         self.assertFalse(est_premier(1))
#
#     # TODO: Fonction test_negatifs
#     #       Tester que les nombres négatifs ne sont pas premiers. Utilisez l'attribut nombres_negatifs
#     def test_negatifs(self):
#         for i in self.nombres_negatifs:
#             self.assertFalse(est_premier(i))
#
#     # TODO: Fonction test_premiers
#     #       Tester que les nombres premiers sont bien premiers. Utilisez l'attribut nombres_premiers.
#     def test_premiers(self):
#         for i in self.nombres_premiers:
#             self.assertTrue(est_premier(i))
#
#     # TODO: Fonction test_non_premiers
#     #       Tester que les nombres non-premiers ne sont pas premiers. Utilisez l'attribut nombres_non_premiers.
#     def test_non_premiers(self):
#         for i in self.nombres_non_premiers:
#             self.assertFalse(est_premier(i))

from math import sqrt


class ErreurDimension(ValueError):  # TODO: Hériter de ValueError
    # Rien à faire ici, on laisse la classe vide pour simplicité.
    pass


class Vecteur:
# TODO: Fonction d'initialisation qui prend en paramètre la liste des données du vecteur et crée un attribut data.
#       Si la liste est vide, alors on lève ErreurDimension.
    def __init__(self, data):
        if data == []:
            raise ErreurDimension()
        else:
            self.data = data

# TODO: Une propriété norme qui calcule la norme du vecteur. On la veut seulement en lecture seule (pas de setter).
    @property
    def norme(self):
        return sqrt(sum(i**2 for i in self.data))

# TODO: L'opérateur d'accès en lecture qui prend un indice et retourne l'élément correspondant dans data.
    def __getitem__(self, item):
        return self.data[item]

# TODO: L'opérateur d'accès en écriture  qui prend un indice et une valeur et change l'élément correspondant dans data.
    def __setitem__(self, key, value):
        self.data[key] = value
        return self

# TODO: La méthode produit_scalaire qui prend en paramètre un autre vecteur de même dimension et retourne le résultat de l'opération.
#       Si l'autre vecteur n'a pas la même dimension que le vecteur courant, on lève ErreurDimension.
    def produit_scalaire(self, vecteur):
        if len(self.data) != len(vecteur.data):
            raise ErreurDimension()
        else:
            return sum(self.data[i]*vecteur.data[i] for i in range(len(self.data)))

v1 = Vecteur([1, 2, 3])
print(v1.data)

v1 = Vecteur([1, 2, 3])
try:
    v1.norme = 42
except AttributeError:
    print("Vecteur.norme en lecture seule OK")

v1 = Vecteur([0, 2])
v2 = Vecteur([10, 10, 5])
print(v1.norme)
print(v2.norme)

v1 = Vecteur([10, 20, 30, 40])
print(v1[2])
v1[2] = 1337
print(v1[2])

v1 = Vecteur([2, 4, 6, 8])
v2 = Vecteur([10, 20, 30, 40])
print(v1.produit_scalaire(v2))

a = Vecteur()