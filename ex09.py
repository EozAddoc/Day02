"""Exercice 9 : Gestion de stock (Interaction entre objets)**

**Objectif** : Travailler avec des relations entre plusieurs classes.

1. Crée une classe `Article` avec :
    - Les attributs : `nom`, `prix`, `quantite_en_stock`.
    - Une méthode `retirer_stock` qui réduit la quantité en stock si possible.
2. Crée une classe `Commande` avec :
    - Les attributs : `client`, `articles_commandes` (liste d'articles et quantités).
    - Une méthode `calculer_total` qui retourne le montant total de la commande.
3. Simule une interaction entre un client qui commande plusieurs articles, en mettant à jour les stocks des articles concernés."""

class Article:
    def __init__(self, nom, prix, quantite_en_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_en_stock = quantite_en_stock

    def retirer_stock(self, quantite):
        if self.quantite_en_stock >= quantite:
            self.quantite_en_stock -= quantite
        else:
            print("pas assez de stock dsl")
    
class Commande:
    def __init__(self, client):
        self.client = client
        self.articles_commandes = []
    
    def calculer_total(self):
        total = 0
        for x,y in self.articles_commandes:
            prix = x.prix * y 
            total += prix
        print(f"le totale a payer pour tous ça est de {total} euros")
        return total
    
    def ajouter_article(self, article, quantite):
        if quantite <= article.quantite_en_stock:
            self.articles_commandes.append((article, quantite))
            article.retirer_stock(quantite)
    
    def afficher_stock(self):
        for x,y in self.articles_commandes:
            print(f'la quantite de {x.nom} est de {x.quantite_en_stock} et vous avez achetez {y} ')



ordinateurs = Article("Ordinateur", 1000, 30)
telephone = Article("Telephone", 700, 54)

commandeKitty = Commande("Hello Kitty")
commandeDoggy = Commande("Hello Dog")

commandeKitty.ajouter_article(ordinateurs, 3)
commandeKitty.ajouter_article(telephone, 200)
commandeKitty.calculer_total()
commandeKitty.afficher_stock()
print("")
commandeDoggy.ajouter_article(ordinateurs, 8)
commandeDoggy.ajouter_article(telephone, 20)
commandeDoggy.calculer_total()
commandeDoggy.afficher_stock()
