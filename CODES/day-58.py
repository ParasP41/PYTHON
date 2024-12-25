'''#constructor#'''

class Person:
    def __init__(self,n,o):
        print("I am a person");
        self.name=n;
        self.occupation=o;
    # name="Paras";
    # occupation="developer";
    def info(self):
        print(f"{self.name} is a {self.occupation}");
        # print(f"{self.name} is a {self.occupation}");
a=Person("harry","tester");
b=Person("nikhil","hr");
c=Person(1,3);
c.info();
a.info();
b.info();
# print(a.name);
# a.name="nikhil";
# a.occupation="HR";
# a.info();