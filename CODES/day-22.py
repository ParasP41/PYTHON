'''#introduction to lists#'''

# l=[3,4,7,6,8,"Paras"];
# print(type(l));
# print(len(l))
# print(l);
# print(l[0]);
# print(l[4]);
# print(type(l[4]));
# print(l[-3])

# if 7 in l:
#     print("7 is present in the list")
# else:
#     print("7 is not present in the list")

'''same thing applies to strings'''
# if "arr" in "harry":
#     print("arr is present in the string")
# else:
#     print("arr is not present in the string")


'''list comprehension'''

list=[i for i in range(10)];
print(list);
list=[i for i in range(10) if i%2==0];
print(list);