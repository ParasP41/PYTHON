'''#decorators#'''

def greet(fxn):
    def mfx(*args, **kwargs):
        print("good morning");
        fxn(*args, **kwargs);
        print("thanks for using this program");
    return mfx;


@greet
def hello():
    print("hello world!");

@greet
def add(a,b):
    print(a+b);

#greet(hello)();
hello()
#greet(add)(2,3);
add(2,3);
