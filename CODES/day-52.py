'''#lambda function#'''

# def double(x):
#     return x * 2


#lambda function
# double=lambda x:x*2;
# avg=lambda x,y: x+y;
# print(double(5));
# print(avg(5,3));

def apply(fx,value):
    return 6+fx(value);

cube=lambda x: x*x*x;
print(apply(cube,2));
