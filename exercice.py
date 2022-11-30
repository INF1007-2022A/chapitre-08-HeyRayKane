#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def compare_fichier(fichier_1:str, fichier_2:str):

    f = open(fichier_1, "r", encoding='utf-8')
    g = open(fichier_2, "r", encoding='utf-8')
    compteur = 0
    for ligne in f:
        compteur +=1
    print(compteur)
    for i in range(compteur):
        a=f.read(1)
        b=g.read(1)
        if a != b:
            print(f"Les fichiers diffèrent à la ligne {i+1}")
    f.close()
    g.close()

def exercice_2(fichier_copier:str, fichier_coller:str):
    with open(fichier_copier, "r", encoding="utf-8") as f1, open(fichier_coller, "w", encoding="utf-8") as f2:
        for count, line in enumerate(f1):
            liste = line.split(" ")
            for word in liste:
                f2.write(word)
                f2.write("   ")
    f1.close()
    f2.close()
    return

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #compare_fichier("exemple.txt", "exemple.txt")
    exercice_2("exemple.txt", "etudiant.txt")
