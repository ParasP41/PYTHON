'''#hybrid and hierarchical inheritance#'''

#hybrid inheritance

class base:
    pass

class derived1(base):
    pass

class derived2(base):
    pass

class derived3(derived1,derived2): 
    pass