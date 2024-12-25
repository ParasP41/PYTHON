'''#map,filter and reduce#'''

# l=[1,2,3,4,5,6,7,8];
# map function applies a change on every element of the given (list, tuple etc.)
# def cube(x):
#     return x*x*x;
# print(cube(3));

# newl=list(map(cube,l));
# print(newl);

# newl=list(map(lambda x:x*x*x,l));
# print(newl);


# filter function returns a new list with elements that satisfy the given condition
# def filter_fxn(x):
#     # return x%2==0;
#     return x>=3;
# new_newl=list(filter(filter_fxn,l));
# print(new_newl);

# new_newl=list(filter(lambda x:x>3,l));
# print(new_newl);


#reduce an list to a single value by adding the hole list etc.


from functools import reduce;
numbers =[1,2,3,4,5,6,7];
# # sum=reduce(lambda x,y:x+y,numbers);
# # print(sum);


def red(x, y):
    return x + y 
# total = [(reduce(red, numbers))];
total = (reduce(red, numbers));
print(total);
