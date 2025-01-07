"""Exercice 7 : Calculateur de salaire (Abstraction et OOP avancée)**

**Objectif** : Travailler avec des classes abstraites.

1. Crée une classe abstraite `Employe` avec :
    - Les attributs : `nom`, `salaire_base`.
    - Une méthode abstraite `calculer_salaire` (à définir dans les sous-classes).
2. Crée deux sous-classes :
    - `EmployeMensuel` : Son salaire est égal à son `salaire_base`.
    - `EmployeHoraire` : Son salaire est égal à son `salaire_base` multiplié par un nombre d'heures travaillées.
3. Crée une classe `Entreprise` qui gère une liste d'employés et peut afficher la masse salariale totale.
4. Instancie une entreprise avec différents types d'employés et calcule la masse salariale."""

from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    @abstractmethod
    def calculer_salaire(self):
        pass

class EmployeMensuel(Employe):
    def calculer_salaire(self):
        salaire = self.salaire_base
        print(f"le salaire de l'employé mensuel {self.nom} est de {salaire} euros")
        return salaire

class EmployeHoraire(Employe):
    def __init__(self, nom, salaire_base, nombre_heures_travaillees):
        super().__init__(nom, salaire_base)
        self.nombre_heures_travaillees = nombre_heures_travaillees
    
    def calculer_salaire(self):
        salaire =self.salaire_base * self.nombre_heures_travaillees
        print(f"le salaire de l'employé horaire {self.nom} est de {salaire} euros")
        return salaire

class Entreprise:
    def __init__(self):
        self.employes = []
    
    def ajouter_employe(self, employe):
        self.employes.append(employe)
    
    def afficher_masse_salariale_totale(self):
        masse_salariale_totale = sum(employe.calculer_salaire() for employe in self.employes)
        print(f"Masse salariale totale de l'entreprise : {masse_salariale_totale} ")


entreprise = Entreprise()
employe_mensuel = EmployeMensuel("James Bond", 4000)
employe_horaire = EmployeHoraire("Maggie Smith", 150, 30)
entreprise.ajouter_employe(employe_mensuel)
entreprise.ajouter_employe(employe_horaire)
entreprise.afficher_masse_salariale_totale()