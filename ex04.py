"""Exercice 4 : Gestion d'un magasin (Collection d'objets)**

**Objectif** : Créer et manipuler une collection d'objets.

1. Crée une classe `Produit` avec :
    - Les attributs : `nom`, `prix`, `quantite`.
    - Une méthode `afficher_produit` qui affiche les informations du produit.
2. Crée une classe `Magasin` avec une liste de produits et les méthodes suivantes :
    - `ajouter_produit` : Ajoute un produit au magasin.
    - `rechercher_produit` : Recherche un produit par nom et retourne ses détails.
    - `afficher_inventaire` : Affiche tous les produits en stock.
    - `vendre_produit` : Réduit la quantité d'un produit lorsqu'il est vendu, ou indique qu'il est en rupture de stock.
3. Instancie un magasin, ajoute plusieurs produits et simule des ventes.
"""

class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def afficher_produit(self):
        print(f'le produit {self.nom} de prix {self.prix} euros a un stock de {self.quantite}  ')

class Magasin:
    def __init__(self):
        self.liste_produits = []

    def ajouter_produit(self,produit):
        self.liste_produits.append(produit)

    def rechercher_produit(self, nom):
        if nom in self.liste_produits :
            nom.afficher_produit()
        else:
            ("le produit nest pas dans notre magasin")
    
    def afficher_inventaire(self):
        print("tous les produits en stock sont :")
        for i in self.liste_produits:
            i.afficher_produit()
    
    def vendre_produit(self, quantityBought,nom):
        if(quantityBought > 0 and nom.quantite > quantityBought):
           nom.quantite -= quantityBought
        else: 
            print("Rupture de stock ou quantité demandée trop grande")


banana = Produit("banane",2.50, 56)
mouchoir = Produit("mouchoir",3.78, 156)
jambon = Produit("jambon",5.50, 24)

magasin = Magasin()
magasin.ajouter_produit(banana)
magasin.ajouter_produit(mouchoir)
magasin.ajouter_produit(jambon)

magasin.rechercher_produit(banana)

print("")
magasin.afficher_inventaire()

print(" ")
magasin.vendre_produit(6,banana)
magasin.rechercher_produit(banana)
