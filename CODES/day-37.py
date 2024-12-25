'''#finally keyword#'''

# try:
#     l=[1,2,3]
#     i=int(input("enter the index: "))
#     print(l[i]);
# except:
#     print("An error occurred");
# finally:
#     print("I will always exicuted");


def func():
    try:
        l=[1,2,3]
        i=int(input("enter the index: "))
        print(l[i]);
        return 1;
    except:
        print("An error occurred");
        return 0;
    finally:
        print("I will always exicuted");

    print("I will exicute");
print(func());
