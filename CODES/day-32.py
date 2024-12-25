'''#set methods#'''

s1={1,2,3,4,5};
s2={4,5,6,7};
# print(s1.union(s2)); #union of two sets
# s1.update(s2); 
# print(s1,s2)

# print(s1.intersection(s2));  #intersection of two sets
# s1.intersection_update(s2);
# print(s1,s2);

# print(s1.difference(s2)); #like a oposite of the intersection print those values which are not common

# city={"khajuraho","mumbai","bhopal"}
# city2={"indore","chharturpur"};
# print(city.isdisjoint(city2)) #when both sets have not contain any similar values

# set1 = {'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia'}
# set2 = {'London', 'Paris', 'Berlin','Vienna', 'Lisbon', 'Zurich','tokyo','delhi'}
# print(set1.issuperset(set2));
# set3 = {'Tokyo', 'Seoul', 'Beijing', 'Bangkok', 'Singapore','Jakarta', 'Delhi'}
# print(set1.issuperset(set3));
# print(set2.issubset(set3));

# set={1,2,3,4,5};
# set.add(10);
# print(set);
# set.remove(2);
# print(set);
# # set.remove(8);
# # print(set); #error beacause 8 does not present in the set 
# set.discard(8);
# print(set); #but discard method do not throw error

# print(set.pop()); #pull the random value from the set

# del set;
# print(set);

# vity={"Paras","adarsh","nikhil"};
# # print("Paras" in vity);
# if "Paras" in vity:
#     print("present in the set");
# else:
#     print("not present");