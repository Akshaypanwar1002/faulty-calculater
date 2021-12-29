class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18
P1=Person("Akshay","Panwar",21)
P2=Person("yash","Pandey",19)
print(P1.full_name())
print(P1.is_above_18())