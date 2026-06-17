
class Student:
    name="sree"
    age=12
    salary=200000
s1=Student()
print(s1.name,s1.age,s1.salary)
----------
class Student:
    def __init__(self,name):
        self.name=name
s1=Student("priya")
print(s1.name)
--------
using method:-
class Student:
    def __init__(self,name):
       self.name=name
    def show(self):
       print(self.name)
s1=Student("sree")
s1.show()
-------