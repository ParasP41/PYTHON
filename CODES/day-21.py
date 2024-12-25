'''#function arguments#'''

'''required arguments'''
# def avg(a,b): 
#     print("This function takes no arguments",(a+b)/2);
# avg(10,20);

'''default arguments'''
# def avg(a=9,b=1): 
#     print("This function takes no arguments",(a+b)/2);
# avg();
# # avg(10,20); #it has move priority over default arguments
# avg(3);
# avg(b=3);

# def name(name1,name2="batman",name3="superman"):
#     print("Hello!",name1,name2,name3);
# name("Ironman","Hulk");

'''keyword arguments'''
# avg(b=10,a=20);

'''variable length arguments'''
# def sum_numbers(a,b=6): #it is compulsory to pass the value of a in the function call
#     sum=a+b;
#     print(sum);
# sum_numbers(20);


# def avg(*numbers): #tuple
#     print(type(numbers));
#     for i in numbers:
#      sum=0;
#      sum+=i;
#      print(sum);
# avg(10,20,30,40,50);


def name(**name): #dictionary 
    print(type(name));
    print(name);
name(name1="Ironman",name2="Hulk",name3="robin");


def sum(a,b):  
    return a+b; #one first is readed by the function other all ignored
    return 4;
b=sum(10,20);
print(b)
