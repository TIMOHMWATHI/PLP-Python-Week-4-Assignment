class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello my name is {self.name} ,I identify as a {self.gender} and I am {self.age} years old.")


if __name__ == '__main__':
    p1 = Person("Allan", 13, "Male")
    p1.introduce()