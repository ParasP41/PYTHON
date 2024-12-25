'''#seek(),tell() and other function#'''

# with open("file.txt", "r") as f:
#     print(type(f));
#     #move to the 10 the byte in the file
#     f.seek(2);

#     #read the next five byte
#     print(f.tell());
#     #tell where the reading of the file starts in seek() method
#     data=f.read(5);
#     print(data);


with open("sample.txt", "w") as f:
    f.write("Hello, world!\n");
    f.truncate(5);

with open("sample.txt", "r") as f:
    print(f.read());

