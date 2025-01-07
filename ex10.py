"""Exercice 10 : Modélisation d’un restaurant**

**Objectif** : Concevoir un système complet pour un restaurant.

1. Crée une classe `Plat` avec :
    - Les attributs : `nom`, `prix`, `temps_preparation`.
    - Une méthode `afficher_details` pour afficher ses informations.
2. Crée une classe `Serveur` avec :
    - Les attributs : `nom`, `commandes_prises` (liste des plats commandés).
    - Une méthode `prendre_commande` pour ajouter des plats à une commande.
3. Crée une classe `Restaurant` avec :
    - Une liste de plats disponibles et de serveurs.
    - Une méthode `afficher_menu` pour lister tous les plats.
    - Une méthode `gerer_commandes` qui affecte des commandes à des serveurs.
4. Simule un restaurant avec plusieurs clients, plats, et serveurs."""

class Plat:
    def __init__(self, nom, prix, temps_preparation):
        self.nom = nom
        self.prix = prix
        self.temps_preparation = temps_preparation

    def afficher_details(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}, Temps de préparation: {self.temps_preparation} minutes")

class Serveur:
    def __init__(self, nom):
        self.nom = nom
        self.commandes_prises = []
    
    def prendre_commande(self, plat):
        self.commandes_prises.append(plat)

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.commandes_commander = []
    
    def commander(self, plat):
        self.commandes_commander(plat)

class Restaurant:
    def __init__(self):
        self.plats_disponibles = []
        self.serveurs = []

    def afficher_menu(self):
        for plat in self.plats_disponibles:
            plat.afficher_details()
    
    def gerer_commandes(self):
        for serveur in self.serveurs:
            if serveur.commandes_prises:
                commande = serveur.commandes_prises.pop(0)
                print(f"{serveur.nom} a pris la commande de {commande.nom}")

restaurant = Restaurant()

plat1 = Plat("Burger", 5, 10)
plat2 = Plat("Pizza", 8, 15)
plat3 = Plat("Frites", 3, 5)
restaurant.plats_disponibles.extend([plat1, plat2, plat3])

serveur1 = Serveur("Hagrid")
serveur2 = Serveur("Voldemort")
restaurant.serveurs.extend([serveur1, serveur2])
restaurant.afficher_menu()

restaurant.gerer_commandes()
serveur1.prendre_commande(plat2)
restaurant.gerer_commandes()
