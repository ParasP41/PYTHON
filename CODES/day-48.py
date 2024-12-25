'''#local and global variables#'''

x=10; # global variable

def myfunc():
    global x
    x=9;
    y=5; # local variable
    print(x);
myfunc();
print(x); 
# print(y); #this will cause an error beacuse y is a local variable and is not accessible outside of the functions