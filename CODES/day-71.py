'''#dir,__dict__ and help method#'''

#these type of methods are used to get the info of the unknwon object,class or method

# x=[1,2,3];
# x=(1,2,3);
# print(dir(x));
# print(x.__add__);

class demon:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        self.version =2.0;

a=demon("Paras",19);
print(a.__dict__);

print(help(demon));