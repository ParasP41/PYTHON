# import math
# import random
# chose=input("snake water or gun : ");
# c=["snake","water","gun"]
# ran=math.floor(random.uniform(0,3));
# if(chose=="water" or chose=="gun" or chose=="snake"): 
#     print("computer chose : ",c[ran]);
#     if(c[ran]=="snake"):
#         if(chose=="water"):
#             print("you lose");
#         elif(chose=="gun"):
#             print("you win");
#         else:
#             print("it's a tie");
#     elif(c[ran]=="water"):
#         if(chose=="gun"):
#             print("you lose");
#         elif(chose=="snake"):
#             print("you win");
#         else:
#             print("it's a tie");
#     elif(c[ran]=="gun"):
#         if(chose=="snake"):
#             print("you lose");
#         elif(chose=="water"):
#             print("you win");
#         else:
#             print("it's a tie");
# else:
#     print("invalid choise")

#////////////////////////////////////////

import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")