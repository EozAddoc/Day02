"""Exercice 3 : Gestion d'un zoo (Héritage et polymorphisme)**

**Objectif** : Introduire l’héritage et le polymorphisme.

1. Crée une classe `Animal` avec :
    - Les attributs : `nom` et `espece`.
    - Une méthode `parler` qui retourne *"Je suis un animal."*
2. Crée deux sous-classes : `Chien` et `Chat` :
    - Redéfinis la méthode `parler` pour qu'elle retourne *"Wouf"* pour un chien et *"Miaou"*pour un chat.
3. Crée une classe `Zoo` avec une liste d'animaux et les méthodes suivantes :
    - `ajouter_animal` : Ajoute un animal au zoo.
    - `faire_parler_tout_le_monde` : Parcourt tous les animaux du zoo et affiche ce qu'ils disent.
4. Crée un zoo avec plusieurs animaux et appelle la méthode `faire_parler_tout_le_monde`."""

class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def parler(self):
        print("Je suis un animal")

class Chien(Animal):
    def __init__(self, nom, espece):
        super().__init__(nom, espece)
    
    def parler(self):
        print("Wouf")

class Chat(Animal):
    def __init__(self, nom, espece):
        super().__init__(nom, espece)
    
    def parler(self):
        print("Miaou")

class Zoo:
    def __init__(self):
        self.liste_animaux = ["tigre"]
    
    def ajouter_animal(self,animal):
        self.liste_animaux.append(animal)
    
    def faire_parler_tout_le_monde(self):
        for i in self.liste_animaux:
            i.parler()

animal = Animal("bob","chameau")
animal.parler()


animal2 = Animal("sara","chat")
animal2.parler()

animal2 = Chat("sara", "chat")
animal2.parler()

animal3 = Chien("mark", "chien")
animal3.parler()

zoo = Zoo()
zoo.ajouter_animal(animal2)
zoo.ajouter_animal(animal)
zoo.ajouter_animal(animal3)

print(zoo.liste_animaux)
zoo.faire_parler_tout_le_monde()