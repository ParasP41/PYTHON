'''#multiple inheritance#'''

class employee:
    def __init__(self,name):
        self.name = name;
    
    def show(self):
        print(f"the name of the employee is {self.name}");

class dancer:
    def __init__(self,dance):
        self.dance = dance;

    
    def show(self):
        print(f"the dance he/she perform is {self.dance}");

class dancer_employee(employee,dancer):
# class dancer_employee(dancer,employee):
    def __init__(self,name,dance):
        self.name=name;
        self.dance=dance;

a=dancer_employee("Paras","hip hop");
a.show();
print(a.name);
print(a.dance);
print(dancer_employee.mro());