'''#class methods as alternative constructor#'''

class Employee:
    def __init__(self, name,salary):
        self.name = name;
        self.salary=salary;
    
    @classmethod   #It is a alternative constructor work same as constructor
    def display_details(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]));

a=Employee("Paras",12000);
print(a.name);
print(a.salary);
str="Harry-12000";
b=Employee.display_details(str);
# b=Employee(str.split("-")[0],str.split("-")[1]);
print(b.name);
print(b.salary);



class Person:
    def __init__(self, name, age):
        self.name=name;
        self.age=age;
    
    @classmethod
    def from_string(cls,string):
        name,age=string.split(",")
        return cls(name,int(age))
    
person=Person.from_string("john Doe, 30")
print(person.name);
print(person.age);