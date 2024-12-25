import os

folder = os .listdir("data") #list all files
print(folder);
print(os.getcwd()) # Get the directory
os.chdir("/Users") #change the directory
print(os.getcwd())


# for folder in folder:
#     print(folder);
#     print(os.listdir(f"data/{folder}"));
