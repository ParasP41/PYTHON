'''#static methods#'''

#static methods do not belong to the instance and class

class Math:

    def __init__(self,num):
        self.num=num;

    def add(self,n):
        self.num+=n;
        print(self.num);
    
    @staticmethod 
    def static_add(a,b):
        return a+b;

# result=Math.static_add(2,4);
# print(result);
a=Math(5);
# print(a.num);
# a.add(2);
# print(a.num);
print(a.static_add(2,4));

