'''#variables and data types#'''

a=8827566139;
b="Harry";
c=None;
d=complex(2,4);
e=True;

print("the type of a and b is =",type(a),type(b));
print("the type of c,d and e is =",type(c),type(d),type(e))

list=[1,2,3,[2,3,4],["paras","harry"]]; #list are immutable in nature
print(list);

tuple=((45,546),("paras","harry")); #tuple are immutable in nature
print(tuple);

dict={   #dict are mutable in nature
    "name":"harry",
    "age":20
    };
print(dict);   