'''#multithreading#'''

import threading
import time
from concurrent.futures import ThreadPoolExecutor

#indicate some task being done
def func(sec):
    print(f"sleeping for {sec} seconds")
    time.sleep(sec);
    return "Paras";

#Normal code
# func(1);
# func(2);
# func(3);

#code using threads

def main():
    t1=threading.Thread(target=func, args=[2]);
    t2=threading.Thread(target=func, args=[2]);
    t3=threading.Thread(target=func, args=[2]);

    t1.start();
    # t1.join();
    t2.start();
    # t2.join();
    t3.start();
    # t2.join();

def pooling():
    with ThreadPoolExecutor() as executor:
        # future1=executor.submit(func, 3);
        # future2=executor.submit(func, 2);
        # future3=executor.submit(func, 3);
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l=[3,5,1,2];
        result=executor.map(func, l);
        for i in result:
            print(i);
pooling();