'''#super keyword#'''

#super keyword is used to access the methods of parent class from child class

# class Parent_Class:
#     def parent_method(self):
#         print("This is a parent method");

# class Child_Class(Parent_Class):
#     def parent_method(self):
#         print("This is a child parent method");
#         super().parent_method();
#     def child_method(self):
#         print("This is a child method");
#         super().parent_method();


# obj = Child_Class();
# obj.child_method();
# obj.parent_method();

class employee:
    def __init__(self, name, id):
        self.name = name;
        self.id = id;

class programmer(employee):
    def __init__(self, name, id,lang):
        # self.name = name;
        # self.id = id;
        super().__init__(name,id);
        self.lang = lang;

# roban=employee("ROHAN","3433");
robin=programmer("ROBIN","3433","Java");

print(robin.name);
print(robin.id);
print(robin.lang);