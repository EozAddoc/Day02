"""Exercice 12 : Gestion d’un tournoi de sport**

**Objectif** : Utiliser des concepts avancés comme les listes et les boucles dans OOP.

1. Crée une classe `Equipe` avec :
    - Les attributs : `nom`, `score`.
    - Une méthode `marquer_point` qui augmente le score.
2. Crée une classe `Match` avec :
    - Les attributs : `equipe1`, `equipe2`, `score_equipe1`, `score_equipe2`.
    - Une méthode `jouer` qui génère un score aléatoire pour les deux équipes.
    - Une méthode `afficher_resultat` pour afficher le vainqueur.
3. Crée une classe `Tournoi` qui gère une liste d'équipes et organise un tournoi en plusieurs matchs.
4. Simule un tournoi avec plusieurs équipes et déclare le vainqueur final."""

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0
    
    def marquer_point(self):
        self.score += 1

class Match:
    def __init__(self, equipe1, equipe2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.score_equipe1 = 0
        self.score_equipe2 = 0  