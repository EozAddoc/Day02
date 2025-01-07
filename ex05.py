"""Exercice 5 : Jeu de rôle (Concepts avancés d'OOP)**

**Objectif** : Travailler sur un projet plus long combinant plusieurs concepts.

1. Crée une classe `Personnage` avec :
    - Les attributs : `nom`, `points_de_vie`, `force`.
    - Une méthode `attaquer` qui réduit les points de vie d'un autre personnage en fonction de la force.
2. Crée deux sous-classes : `Guerrier` et `Mage` :
    - `Guerrier` a un bonus de force.
    - `Mage` peut utiliser un sort pour infliger des dégâts supplémentaires.
3. Crée une classe `Combat` qui gère un combat entre deux personnages, avec une méthode `lancer_combat` qui continue jusqu'à ce qu'un personnage n'ait plus de points de vie.
4. Simule un combat entre deux personnages."""


class Personnage:
    def __init__(self, nom, points_de_vie, force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force

    def attaquer(self, attackedPerson):
        attackedPerson.points_de_vie -= self.force

class Guerrier(Personnage):
    def __init__(self, nom, points_de_vie, force, bonus_force):
        super().__init__(nom, points_de_vie, force)
        self.bonus_force = bonus_force
    
    def attaquer(self, attackedPerson):
        attackedPerson.points_de_vie -= (self.bonus_force  + self.force)

class Mage(Personnage):
    def __init__(self, nom, points_de_vie, force, puissance):
        super().__init__(nom, points_de_vie, force)
        self.puissance = puissance
    
    def attaquer(self, attackedPerson):
        attackedPerson.points_de_vie -= self.force * self.puissance

class Combat:
    def lancer_combat(self, combattant1, combattant2):
        winner = None
        while combattant1.points_de_vie > 0 and combattant2.points_de_vie > 0:
            combattant1.attaquer(combattant2)
            if combattant2.points_de_vie <= 0:
                print(f"{combattant1.nom} a gagné!")
                break
            combattant2.attaquer(combattant1)
            if combattant1.points_de_vie <= 0:
                print(f"{combattant2.nom} a gagné!")
                break
            print(f"{combattant1.nom} a {combattant1.points_de_vie} points de vie  et {combattant2.nom} a {combattant2.points_de_vie} points de vie ")
     



combat = Combat()
player1 = Guerrier("Guerrier ", 200, 20, 15)
player2 = Mage("Mage ", 150, 25, 2)
combat.lancer_combat(player1, player2)
print(f"{player1.nom} a {player1.points_de_vie} points de vie  et {player2.nom} a {player2.points_de_vie} points de vie ")
