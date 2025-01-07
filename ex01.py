""" **Exercice 1 : Classe de base et manipulation d'attributs**

Objectif** : Comprendre les bases de la classe, des attributs et des méthodes.

1. Crée une classe `Voiture` avec :
    - Les attributs suivants : `marque`, `modele`, `annee`, `kilometrage`.
    - Une méthode `afficher_details` qui affiche toutes les informations de la voiture.
2. Ajoute une méthode `augmenter_kilometrage` qui augmente le kilométrage d'un certain nombre de kilomètres, avec une validation pour s'assurer que le kilométrage ajouté est positif.
3. Instancie plusieurs objets `Voiture` et affiche leurs détails après avoir modifié leur kilométrage.
"""
# Voiture class
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher_details(self):
        print(f'la voiture est une {self.marque} de modele {self.modele} sortie en {self.annee} de {self.kilometrage} kilometrage ')

    def augementer_kilometrage(self, kilometrage_to_add):
        if(kilometrage_to_add >= 0):
            self.kilometrage += kilometrage_to_add



voiture1 = Voiture("Toyota", "Corolla", 2015, 85009)
voiture2 = Voiture("Ford", "Focus", 2018, 45021)
voiture3 = Voiture("Tesla", "Model S", 2022, 15050)

print("Avant d'augmeneter le kilometrage : ")
print("")
voiture1.afficher_details()
voiture2.afficher_details()
voiture3.afficher_details()

voiture1.augementer_kilometrage(1200)
voiture2.augementer_kilometrage(200)
voiture3.augementer_kilometrage(2900)
print("")

print("Apres avoir augmeneter le kilometrage")
print("")

voiture1.afficher_details()
voiture2.afficher_details()
voiture3.afficher_details()

