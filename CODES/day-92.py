'''#function caching#'''

import  functools
import time

@functools.lru_cache(maxsize=None)
def fxn(n):
    time.sleep(1);
    return n;

print(fxn(20));
print(fxn("done for 20"));

print(fxn(30));
print(fxn("done for 30"));

print(fxn(30));
print(fxn("done for 30"));

print(fxn(20));
print(fxn("done for 20"));

print(fxn(30));
print(fxn("done for 30"));

print(fxn(30));
print(fxn("done for 30"));
