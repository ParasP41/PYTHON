'''#class methods#'''

class Empolyee:
    company="Apple";
    def show(self):
        print(f"the name of the employee is {self.name} and the company name is {self.company}")
    
    @classmethod # this class method will chnage the company(class variable) name Apple to google without this method class variable can never be change
    def changecompany(cls,newcompany):
        cls.company=newcompany;

emp1=Empolyee();
emp1.name="Paras";
emp1.show();
emp1.changecompany("google");
emp1.show();
print(emp1.company);