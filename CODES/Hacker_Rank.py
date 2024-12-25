# s="AABCAAADA";
# k=3;
# x=int(len(s)/k);
# for i in range(x):
#     s2=s[k*i:(i+1)*k];
#     print(s2);


m="AAAB"
x=""
for i in range(1,len(m)):
    a=0
    if m[i]==m[a]:
        x+=m[i];
    elif m[i]!=m[a]:
        x=m[i];
    a+=1;
    print(x, end="");
    
