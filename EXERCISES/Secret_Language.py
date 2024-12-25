# str=input("Please enter the message : ");
# coded="";
# if(len(str)>=3):
#     r1="dhb";
#     r2="jdf";        
#     str=r1+str[1:]+str[0]+r2;
#     i=len(str)-1;
#     while(i>=0):
#             coded+=str[i];
#             i=i-1;
#     print("coded message is : ",coded);
# else:
#     print("your code is to short to length");

# newstr=coded;
# a=len(newstr)-1;
# str2="";
# while(a>=0):
#     str2+=newstr[a];
#     a=a-1;

# str2=str2[3:];
# str2=str2[0:len(str2)-3];
# str2=str2[len(str2)-1]+str2;
# str2=str2[0:len(str2)-1]

# print("decoded message is : ",str2);

#////////////////////////////////////////////////////////

st = input("Enter message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))