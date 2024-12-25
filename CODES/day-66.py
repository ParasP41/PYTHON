'''#instance variables vs class variables#'''


#compiler always find first instance variable then class variable. so in emp1.show() it will print "Apple variable" instead of "Apple"

class Employee:
    companyName="Apple"; #class variable
    noofemployee=0;
    def __init__(self,name):
        self.name = name #instance variable
        self.raise_amount = 0.02 #instance variable
        self.noofemployee+=1;
    def show(self):
        print(f"the name of the employee is {self.name} and the raise value is {self.raise_amount} in company {self.companyName} and {self.noofemployee}");
    
# Employee.show(emp1);
emp1 = Employee("John"); 
emp1.companyName="Apple India";
emp1.show();

emp2 = Employee("adarsh"); 
emp2.raise_amount=0.09;
# emp2.companyName="google";
emp2.show();

