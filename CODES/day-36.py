'''#exception handling#'''

# a=input("enter the value of a = ");
# print(f"multiplication table of {a} is:")


# try:
#     for i in range(1,11):
#         print(f"{a} * {i} = {int(a)*i}");
# # except Exception as e: 
# #     print("Error occurred: ", e);
# except:
#     print("invalid input");

# print("paras");



# try:
#     a=int(input("enter the number a "));
# except ValueError:
#     print("Invalid input for a. Please enter a valid integer.");


try:
    num=int(input("enter the num "));
    a=[2,3];
    print(a[num]);
except IndexError:
    print("Invalid input for a. Please enter a number between 1 and 10.");