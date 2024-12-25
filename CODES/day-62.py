'''#access modifiers#'''

# class Employee:
#     def __init__(self):
#         self.__name = 'Paras'

# a=Employee();
# # print(a.__name); #cannot be accessed directly
# print(a._Employee__name); # but can be accessed indirectly
# print(a.__dir__());

class student:
    def __init__(self):
        self._name = "Paras";
    def _funname(self):
        return "cwh";

class child(student):
    pass

obj=student();
obj1=child();
print(obj.__dir__());
print(obj1.__dir__());
print(obj._name);
print(obj._funname());
print(obj1._name);
print(obj1._funname());