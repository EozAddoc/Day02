"""**Exercice 2 : Constructeurs avancés et calculs**

**Objectif** : Utiliser un constructeur et intégrer des calculs dans les méthodes.

1. Modifie la classe `Voiture` pour ajouter un constructeur qui initialise les attributs.
2. Ajoute une méthode `calculer_age` qui retourne l'âge de la voiture en fonction de l'année actuelle.
3. Ajoute une méthode `est_vieille` qui retourne `True` si la voiture a plus de 10 ans, sinon `False`.
4. Teste ces méthodes avec plusieurs voitures."""
import datetime

# Voiture class
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher_details(self):
        print(f'la voiture est une {self.marque} de modele {self.modele} sortie en {self.annee} de {self.kilometrage} kilometrage ')

    def augementer_kilometrage(self, kilometrage_to_add:int):
        if(kilometrage_to_add > 0):
            self.kilometrage += kilometrage_to_add
    
    def calculer_age(self):
        today = datetime.date.today()
        year = today.year
        age = year - self.annee
        print(f"la voiture a {age} ans")
        return age

    def est_vieille(self,age):
        if(age > 10):
            return True
        else:
            return False



voiture1 = Voiture("Toyota", "Corolla", 2005, 85009)
voiture2 = Voiture("Ford", "Focus", 2018, 45021)
voiture3 = Voiture("Tesla", "Model S", 2022, 15050)


print(f" cest {voiture1.est_vieille(voiture1.calculer_age())} que la voiture est vieille pour la voiture1 ")
print(f" cest {voiture2.est_vieille(voiture2.calculer_age())} que la voiture est vieille pour la voiture2 ")
print(f" cest {voiture3.est_vieille(voiture3.calculer_age())} que la voiture est vieille pour la voiture3 ")