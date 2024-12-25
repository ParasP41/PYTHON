'''#classes and objects#'''

class person:
    name="harry";
    occuaptions="Software developer";
    networth=10000;
    def info(self): #self keyword is used to access the varible that belong to the class
        print(f"{self.name} is a {self.occuaptions} and its networth is {self.networth}");
a=person();
b=person();
a.info();
a.name="Paras";
a.occuaptions="Software tester";
b.name="nikhil";
b.occuaptions="harware developer";

# a.occuaptions="Software tester";
# print(a.occuaptions);
# print(a.name);
# print(a.networth);
a.info();
b.info();