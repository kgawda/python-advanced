class Dog:
    def sound(self):
        return "Woof"

class Husky(Dog):
    def sound(self):
        return "(" + super().sound().lower() + ")"

class Puppy(Dog):
    def sound(self):
        return super().sound() + "ie!"

class HuskyPuppy(Husky, Puppy):
    pass


if __name__ == "__main__":
    print(f"{Dog().sound() = }")
    print(f"{Husky().sound() = }")
    print(f"{Puppy().sound() = }")
    print(f"{HuskyPuppy().sound() = }")
