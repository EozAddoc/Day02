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
            print("Solde negatif")
class Banque:
    def __init__(self):
        self.comptes = []
    
    def ajouter_compte(self, compte):
        self.comptes.append(compte)
    
    def afficher_comptes(self):
        for compte in self.comptes:
            print(f"Compte de {compte.titulaire}: Solde : {compte.solde}")
    
    def transferer(self, compte_quiDemande, compte_quiRecoit, montant):
        if montant <= compte_quiDemande.solde:
            compte_quiDemande.retirer(montant)
            compte_quiRecoit.deposer(montant)
            print(f"Transfert de {montant} euros effectué de {compte_quiDemande.titulaire} à {compte_quiRecoit.titulaire}")
        else:
            print("Solde trops grand")

banque = Banque()
compte1 = CompteBancaire("Artemis")
compte2 = CompteBancaire("Zeus")
banque.ajouter_compte(compte1)
banque.ajouter_compte(compte2)
banque.transferer(compte1, compte2, 50)
compte1.deposer(1000)
compte2.deposer(500)
banque.afficher_comptes()
banque.transferer(compte2, compte1, 100)
compte2.deposer(73)
banque.afficher_comptes()
compte1.retirer(280)
banque.afficher_comptes()

