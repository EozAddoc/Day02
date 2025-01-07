"""Exercice 14 : Gestion de tâches**

**Objectif** : Travailler sur un projet structuré avec des listes et des interactions.

1. Crée une classe `Tache` avec :
    - Les attributs : `titre`, `description`, `statut` (à faire, en cours, terminé).
    - Une méthode `changer_statut` pour mettre à jour le statut.
2. Crée une classe `Utilisateur` avec :
    - Les attributs : `nom`, `taches` (liste de tâches).
    - Une méthode `ajouter_tache` pour ajouter une tâche à l’utilisateur.
    - Une méthode `afficher_taches` pour afficher les tâches avec leur statut.
3. Crée une classe `GestionnaireDeTaches` avec :
    - Une liste d’utilisateurs.
    - Une méthode `attribuer_tache` pour attribuer une tâche à un utilisateur.
    - Une méthode `afficher_toutes_taches` pour afficher les tâches de tous les utilisateurs.
4. Simule un gestionnaire de tâches avec plusieurs utilisateurs et tâches."""

class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.taches = []
    
    def ajouter_tache(self, tache):
        self.taches.append(tache)
    
    def afficher_taches(self):
        for tache in self.taches:
            print(f" la tache {tache.titre}  de description {tache.description} est {tache.statut}")

class GestionnaireDeTaches:
    def __init__(self):
        self.utilisateurs = []

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)
    
    def attribuer_tache(self, utilisateur, tache):
        utilisateur.ajouter_tache(tache)
    
    def afficher_toutes_taches(self):
        for utilisateur in self.utilisateurs:
            print(f"Les tâches de l'utilisateur {utilisateur.nom} sont:")
            utilisateur.afficher_taches()

tache1 = Tache("Vaisselle", "laver, savon, secher, ranger")
tache2 = Tache("Devoir(codeeee)", "fiche de revision, revision, code, finis, commentaire")
tache3 = Tache("chat", "litiere, eau, nourrire, jouer")

utilisateur1 = Utilisateur("Zoe Codda")
utilisateur2 = Utilisateur("Madeleine Ravanas")

gestionnaire = GestionnaireDeTaches()
gestionnaire.ajouter_utilisateur(utilisateur1)
gestionnaire.ajouter_utilisateur(utilisateur2)
gestionnaire.attribuer_tache(utilisateur1, tache1)
gestionnaire.attribuer_tache(utilisateur1, tache2)
gestionnaire.attribuer_tache(utilisateur2, tache3)

gestionnaire.afficher_toutes_taches()
tache2.changer_statut("terminé")
gestionnaire.afficher_toutes_taches()
