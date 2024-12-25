'''#match case statements#'''

# x=int(input("Enter a number: "))
# match x:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _:
#         print("Invalid input")


y=int(input("Enter a number: "))
match y:
    case 1:
        print("One")
    case _ if y > 10:
        print("Greater than 10")
    case _ if y < 10:
        print("Less than 10")
    case _:
        print("Invalid input");


