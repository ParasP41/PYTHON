'''#'is' vs '=='#'''

# a=(1,3); #tuple is immutable
# b=(1,3); #tuple is immutable

a=[1,2,3] #list is mutable
b=[1,2,3] #list is mutable


print(a==b); # "==" it compairs the value of the object
print(a is b); # "is" it compairs the exact location of the object in memory
