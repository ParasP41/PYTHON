'''#method overriding#'''

class shape:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;

    def area(self):
        return self.x*self.y;

class circle(shape):
    def __init__(self, r):
        self.r=r;
        super().__init__(r,r)

    # def area(self):
    #     return self.r*self.r*3.14;

# rec=shape(2,3);
# print(rec.area());
cir=circle(6);
print(cir.area());