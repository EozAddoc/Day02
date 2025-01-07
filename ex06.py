"""Exercice 6 : Gestion d’une bibliothèque (Mini-projet)**

**Objectif** : Revoir tous les concepts en réalisant un projet plus complexe.

1. Crée une classe `Livre` avec :
    - Les attributs : `titre`, `auteur`, `disponible` (booléen).
    - Une méthode `emprunter` qui change la disponibilité du livre si possible.
    - Une méthode `rendre` pour rendre le livre disponible.
2. Crée une classe `Utilisateur` avec :
    - Les attributs : `nom`, `livres_empruntes` (liste de livres).
    - Une méthode `emprunter_livre` pour ajouter un livre à la liste de l'utilisateur.
    - Une méthode `rendre_livre` pour retirer un livre de la liste.
3. Crée une classe `Bibliotheque` avec une liste de livres et les méthodes suivantes :
    - `ajouter_livre` : Ajoute un livre à la bibliothèque.
    - `afficher_livres` : Affiche tous les livres avec leur disponibilité.
    - `gerer_emprunt` : Permet à un utilisateur d'emprunter ou de rendre un livre.
4. Simule plusieurs utilisateurs empruntant et rendant des livres.
"""

class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print("Livre emprunté avec succès ")
            return True
        else:
            print("livre nest pas disponible ")
            return False
    def rendre(self):
        self.disponible = True

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)
    
    def rendre_livre(self, livre):
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)
            livre.rendre()

class Bibliotheque:
    def __init__(self):
        self.livres = []
        
    def ajouter_livre(self, livre):
        self.livres.append(livre)
    
    def afficher_livres(self):
        for livre in self.livres:
            print(f"{livre.titre} par {livre.auteur}, disponible : {livre.disponible}")

bibliotheque = Bibliotheque()
# jai utilise chat pour me donner les livres
livre1 = Livre("To Kill a Mockingbird", "Harper Lee", True)
livre2 = Livre("1984", "George Orwell", True)
livre3 = Livre("Pride and Prejudice", "Jane Austen", True)
livre4 = Livre("The Great Gatsby", "F. Scott Fitzgerald", True)

print("")
print("Avant que Alice emprunte un livre:")
print("")
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
alice = Utilisateur("Alice")
bob = Utilisateur("Bob")
bibliotheque.afficher_livres()
print("")
print("Apres que Alice emprunte un livre:")
print("")
alice.emprunter_livre(livre1)
bibliotheque.afficher_livres()
print("")
print("Bob essaie demprunter le meme livre:")
bob.emprunter_livre(livre1)
alice.rendre_livre(livre1)
print("Alice rends Bob essaie de remprunter le meme livre:")
bob.emprunter_livre(livre1)
