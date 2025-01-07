"""Exercice 8 : Système de réservation**

**Objectif** : Réunir tous les concepts appris.

1. Crée une classe `Reservation` avec :
    - Les attributs : `id`, `client`, `date`, `place`.
    - Une méthode `confirmer` qui change le statut de la réservation à "confirmée".
2. Crée une classe `Client` avec :
    - Les attributs : `nom`, `email`, `reservations`.
    - Une méthode `effectuer_reservation` qui ajoute une réservation à la liste.
3. Crée une classe `SystemeDeReservation` qui gère toutes les réservations et offre les fonctionnalités suivantes :
    - `ajouter_reservation` : Crée une nouvelle réservation.
    - `annuler_reservation` : Annule une réservation donnée.
    - `afficher_reservations` : Affiche toutes les réservations.
4. Simule un système complet de gestion des réservations pour un événement avec plusieurs clients."""

class Reservation:
    def __init__(self, id, client, date, place):
        self.id = id
        self.client = client
        self.date = date
        self.place = place
        self.statut = "dispo"

    def confirmer(self):
        self.statut = "confirmée"
    def attente(self):
        self.statut = "attente"

    def annuler(self):
        self.statut = "dispo"

    def afficher_res(self):
        print(f"ID: {self.id}, Client: {self.client.nom}, Date: {self.date}, Place: {self.place}, Statut: {self.statut}")


class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.reservations = []

    def effectuer_reservation(self, reservation):
        self.reservations.append(reservation)

class SystemeDeReservation:
    def __init__(self):
        self.reservations = []
        self.ids = 0

    def ajouter_reservation(self, client, date, place):
        for reservation in self.reservations:
            if reservation.date == date and reservation.place == place and reservation.statut == "confirmée":
                print(f"dsl {client.nom} la {place}' est deja reservee le {date}.")
                return
        
        self.ids += 1
        reservation = Reservation(self.ids, client, date, place)
        reservation.confirmer()
        self.reservations.append(reservation)
        client.effectuer_reservation(reservation)
    
    
    def annuler_reservation(self, client, date):
        for reservation in self.reservations:
            if reservation.client == client and reservation.date == date and reservation.statut == "confirmée":
                reservation.annuler()
                self.reservations.remove(reservation)
                break

    def afficher_reservations(self):
        for reservation in self.reservations:
            reservation.afficher_res()



sys = SystemeDeReservation()
client1 = Client("John Hampshire", "john@example.com")
client2 = Client("Jane Goodal", "jane@example.com")
client3 = Client("Jack Nicholson", "jack@example.com")

sys.ajouter_reservation(client1, "2022-12-15", "Salle A")
sys.ajouter_reservation(client2, "2022-12-15", "Salle B")
sys.ajouter_reservation(client3, "2022-12-15", "Salle A")

sys.afficher_reservations()

sys.annuler_reservation(client1, "2022-12-15")
print("")
print("apres que client1(john) est annule sa reservation voyons si client 3(Jack) peut")
sys.ajouter_reservation(client3, "2022-12-15", "Salle A")
sys.afficher_reservations()
