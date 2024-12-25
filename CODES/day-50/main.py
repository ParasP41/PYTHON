'''#read(),readlines() and other methods#'''

# f=open("file.txt", "a");
# f.write("i am appended")
# f.close();

# f=open("file.txt", "r") 
# while True:
#     line=f.readline() # to read a file line by line
#     if not line:
#         break;
#     print(line);

# f=open("marks.txt", "r")
# while True:
#     line=f.readline();
#     if not line:
#         break;
#     m1=int(line.split(",")[0]);
#     print(m1);
#     m2=line.split(",")[1];
#     print(m2);
#     m3=line.split(",")[2];
#     print(m3);


f=open("myfile.txt","w");
line=["line1\n", "line2\n", "line3\n"]
f.writelines(line); 
f.close();