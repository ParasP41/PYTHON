'''#file io#'''

# f=open("myfile.txt","r"); # "r" to read the file
# # print(f);
# text=f.read();
# print(text);
# f.close();

# f=open("file.txt","w"); # "w" to write the file
# text=f.write("I am file.txt");
# print(text);
# f.close();

# f=open("file.txt","a"); # "a" to append the text 
# text=f.write(" and i am good");
# print(text);
# f.close();

# f=open("file.txt","rb"); # "rb to read the file in binary format"
# text=f.read();
# print(text);
# f.close();

# f=open("file.txt","wb"); # "wb to write the file in binary format"
# text=f.write(b"I am file.txt in binary format");
# print(text);
# f.close();

#another syntext to handel the files

with open("file.txt", "a") as f:
    f.write("I am file.txt in binary format");