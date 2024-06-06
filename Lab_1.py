
#Oppgave 1

class Person:

    def __init__(self, navn):
        self.navn= navn

    def greets(self, navn):
        print("Hello,", navn,"!")


alice = Person("Alice")
bob = Person("Bob")
alice.greets(bob.navn)


#Oppgave 2

class Employee:
        
        def __init__(self, firstname, lastname, salary=1000):
                
                self.firstname = firstname
                self.lastname = lastname
                self.salary = salary
        
        def get_fullname(self):
                return self.firstname, self.lastname
        
        def print_email(self):
                print(f"{self.firstname}.{self.lastname}@company.com")

        def increase_salary(self, rate):
               self.rate = rate

person = Employee("Emil", "Sandvold")
print(person.print_email())