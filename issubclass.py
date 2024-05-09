class Animal:
    ...

class Dog(Animal):
    ...

class Vehicle:
    ...

class BMW(Vehicle):
    ...

if __name__ == "__main__":
    print(issubclass(Dog, Animal))
    print(issubclass(Animal, Animal))
    print(issubclass(BMW, Animal))