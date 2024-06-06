from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, species, carnivore, skin, venemous=None):
        self.name = name
        self.species = species
        self.carnivore = carnivore
        self.skin = skin
        self.venemous = venemous
        
    @abstractmethod
    def speak(self):
        pass
        #if speak == True:
        #    print("can speak")


class Mammal(Animal):

    def __init__(self, name, species ,carnivore):
        super().__init__(name,species,carnivore)
        skin = "hair"

    def get_skin(self):
        pass

    def herbivore_or_carnivore(self):
        if self.carnivore == True:
            return "your animal eats meat and other animals"
        elif self.carnivore == not True:
            return "your animal eats plants"

class Reptile(Animal):
    def __init__(self,name,species,carnivore,skin):
        super().__init__(name,species,carnivore,skin)
        skin = "scale"
    
    def herbivore_or_carnivore(self):
        if self.carnivore == True:
            return "your animal eats meat and other animals"
        elif self.carnivore == not True:
            return "your animal eats plants"

    def venemous_bite(self):
        if self.venemous == True:
            return "your reptile is venemous"
        else:
            return "your reptile does not have a venemous bite"
    

class Bird(Animal):
    
    def __init__(self,name,species,carnivore,skin):
        super().__init__(name,species,carnivore,skin)
        skin = "scale"
    
    def herbivore_or_carnivore(self):
        if self.carnivore == True:
            return "your animal eats meat and other animals"
        elif self.carnivore == not True:
            return "your animal eats plants"


