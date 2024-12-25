'''#time module#'''

import time
# def usingwhile():
#     i=0;
#     while i<500:
#         i=i+1;
#         print(i);

# def usingfor():
#     for i in range(500):
#         print(i);

# init=time.time()
# usingfor();
# t1=time.time()-init;
# init=time.time()
# usingwhile();
# print(time.time()-init);
# print(t1);


# print(4);
# time.sleep(3);
# print("i am here after 3 seconds");

t=time.localtime();
print(t);
formated_time=time.strftime("%Y-%m-%d %H:%M:%S %Z",t);
print(formated_time);
