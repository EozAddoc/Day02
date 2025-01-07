"""Exercice 11 : Système de messagerie avec horodatage

**Objectif** : Construire une application simple de messagerie en intégrant un horodatage précis pour chaque message.

1. Crée une classe `Message` avec :
    - Les attributs suivants :
        - `expediteur` : Le nom de l'utilisateur qui envoie le message.
        - `destinataire` : Le nom de l'utilisateur qui reçoit le message.
        - `contenu` : Le contenu du message.
        - `date_envoi` : La date et l'heure exactes d'envoi du message (format : `YYYY-MM-DD HH:MM:SS`).
    - Une méthode `afficher_message` qui affiche :
        
        ```
        De: {expediteur} | À: {destinataire} | Date: {date_envoi}
        Contenu: {contenu}
        ```
        
2. Crée une classe `Utilisateur` avec :
    - Les attributs suivants :
        - `nom` : Le nom de l'utilisateur.
        - `messages_envoyes` : Une liste de messages envoyés.
        - `messages_recus` : Une liste de messages reçus.
    - Une méthode `envoyer_message` qui :
        - Crée un message avec un horodatage automatique.
        - Ajoute le message à la liste des messages envoyés de l'expéditeur et à celle des messages reçus du destinataire.
        - Affiche un message de confirmation.
    - Une méthode `lire_boite_reception` qui affiche tous les messages reçus avec leur contenu et leur horodatage.
3. Simule une interaction entre plusieurs utilisateurs :
    - Crée deux ou trois utilisateurs.
    - Envoie des messages entre eux.
    - Affiche les boîtes de réception de chaque utilisateur."""
from datetime import datetime
class Message:
    def __init__(self, expediteur, destinataire, contenu):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.contenu = contenu
        # found on stack overflow https://stackoverflow.com/questions/16286991/converting-yyyy-mm-dd-hhmmss-date-time
        self.date_envoi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def afficher_message(self):
        print(f"De: {self.expediteur} | : {self.destinataire} | Date: {self.date_envoi}")
        print(f"Contenu: {self.contenu}")
    

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.messages_envoyes = []
        self.messages_recus = []
    
    def envoyer_message(self, destinataire, contenu):
        message = Message(self.nom, destinataire.nom, contenu)
        self.messages_envoyes.append(message)
        destinataire.messages_recus.append(message)
        print(f"Message envoyé à {destinataire.nom}")
    
    def lire_boite_reception(self):
        for message in self.messages_recus:
            message.afficher_message()

hera =Utilisateur("Hera")
gromit =Utilisateur("Gromit")
wallis =Utilisateur("Wallis")

hera.envoyer_message(gromit, "Salut Bob!")
gromit.envoyer_message(hera, "Bonjour Hera!")
wallis.envoyer_message(gromit, "lol?")

hera.lire_boite_reception()
gromit.lire_boite_reception()
wallis.lire_boite_reception()

