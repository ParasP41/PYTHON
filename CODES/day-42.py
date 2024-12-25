'''#enumerate function#'''

# lst = [12,56,32,67,45,90];
# for i in range(len(lst)):
#     # print(lst[i]);
#     if (lst[i] ==67):
#         print(f"Harry got a higgest score of {lst[i]}");

lst = [12,56,32,67,45,90];
#It returns pairs of index and value, making it easier to access both the position and the item itself during iteration.
for index,marks in enumerate(lst,start=1):
    print(index,marks);
    if (index == 3):
        print("harry awesome!");

