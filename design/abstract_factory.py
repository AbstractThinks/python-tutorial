"""
抽象工厂模式
"""

import random

class PetShop:

    def __init__(self, aninal_factory=None):

        self.pet_factory = animal_factory

    def show_pet(self):

        pet = self.pet_factory.get_pet()
        food = self.pet_factory.get_food()
        print("this is a lovely", pet)
        print("It says ", pet.speak())
        print("It eats", food)


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "miaomiao"
    def __str__(self)
        return "Cat"



class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"

class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "cat food"


def get_factory():
    return random.choice([DogFactory, CatFactory])()

if __name__ == "__main__":
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)



