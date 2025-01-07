"""Exercice 13 : Simulation d’un système bancaire**

**Objectif** : Appliquer des concepts avancés à un problème réel.

1. Crée une classe `CompteBancaire` avec :
    - Les attributs : `titulaire`, `solde`.
    - Une méthode `deposer` pour ajouter de l'argent.
    - Une méthode `retirer` pour retirer de l'argent, avec une vérification pour éviter un solde négatif.
2. Crée une classe `Banque` qui gère plusieurs comptes et offre les fonctionnalités suivantes :
    - `ajouter_compte` : Ajoute un nouveau compte.
    - `afficher_comptes` : Affiche tous les comptes avec leur solde.
    - `transferer` : Transfère de l'argent d'un compte à un autre.
3. Simule une banque avec plusieurs comptes et des transferts d'argent entre eux"""

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Solde insuffisant")