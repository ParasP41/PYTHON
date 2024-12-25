'''#inheritance#'''

class Employee():
    def __init__(self,name,id):
        self.name = name;
        self.id = id;

    def show(self):
        print(f"the name of the employee is {self.name} and its id is {self.id}")

class programmer(Employee):
    def showlanguages(self):
        print("the languages of the employee is python");

obj=programmer("nikhil",745);
obj.showlanguages();
obj.show();

# ob=Employee("Paras",80);
# ob.show();
# ob2=Employee("Harry",82);
# ob2.show();