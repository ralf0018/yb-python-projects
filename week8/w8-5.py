class Animal:  # Parent class
    
    def make_sound(self):
        print("Animal makes sound")

class Dog(Animal):  # Child class

    def bark(self):
        print("Woof!")

class Cat(Animal):  # Another child class
    def meow(self):
        print("Meow!")

if __name__ == "__main__":
    dog = Dog()
    dog.make_sound()  # Inherited method
    dog.bark()  # Dog-specific method

    cat = Cat()
    cat.make_sound()  # Inherited method
    cat.meow()  # Cat-specific method