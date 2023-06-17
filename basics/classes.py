class Person:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job

    def presentation(self):
        print(f"Hi, my name is {self.name} and i am {str(self.age)} year old.")

brahim = Person('Brahim', 47, 'developer')
brahim.presentation()


# class definitions cannot be empty, but if you for some reason 
# have a class definition with no content, put in the pass statement 
# to avoid getting an error.
class Empty():
    pass


# Inheritance
class Sabine(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age, job)
        self.married = True

b2 = Sabine('Sabine', 44, 'yoga teacher')
b2.presentation()
print(b2.married)