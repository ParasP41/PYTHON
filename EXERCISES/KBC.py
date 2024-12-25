question=["1.Who painted the famous artwork “Mona Lisa”?","2.What is the name of the Dutch painter who created “The Starry Night”?","3.Which artist is known for his melting clocks in the painting “The Persistence of Memory”?","4.Who sculpted the famous statue of David?","5.Who painted the ceiling of the Sistine Chapel in Vatican City?"];
answer=[["a. Pablo Picasso",
"b. Leonardo da Vinci",
"c. Vincent van Gogh",
"d. Michelangelo"],
["a. Vincent van Gogh"
"b. Claude Monet"
"c. Pablo Picasso"
"d. Rembrandt"],
["a. Salvador Dalí",
"b. Pablo Picasso",
"c. Jackson Pollock,"
"d. Andy Warhol,"],
["a. Michelangelo",
"b. Donatello",
"c. Leonardo da Vinci",
"d. Raphael,"],
["a. Leonardo da Vinci",
"b. Michelangelo",
"c. Raphael",
"d. Botticelli,"]
];
price=["1000","10000","100000","500000","1000000"]
options=["b","a","c","d","a"];


for i in range(len(question)):
    print(f"questiopn for the RS {price[i]}");
    print(question[i]);
    print(answer[i]);
    ans=input("enter the answer of the questiion : ");
    print(ans);
    if(ans==options[i]):
        print(f"congrats you won the RS {price[i]}");
    elif(ans!=options[i]):
        print(f"the final money you won is {price[i]}");
        break;



#//////////////////////////////////////////////////////////////

# questions = [
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
# ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
  
#   question = questions[i]
#   print(f"\n\nQuestion for Rs. {levels[i]}")
#   print(f"a. {question[1]}          b. {question[2]} ")
#   print(f"c. {question[3]}          d. {question[4]} ")
#   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
#   if (reply == 0):
#     money = levels[i-1]
#     break
#   if(reply == question[-1]):
#     print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(i == 4):
#       money = 10000
#     elif(i == 9):
#       money = 320000
#     elif(i == 14):
#       money = 10000000
#   else:
#     print("Wrong answer!")
#     break 

# print(f"Your take home money is {money}")



