# import time;
# '''get the current time in seconds since the epoch'''
# seconds = time.time();
# # print("Seconds since epoch =", seconds)	 
# '''convert the time in seconds since the epoch to a readable format'''
# local_time = time.ctime(seconds);
# '''# print("Local time:", local_time,len(local_time),type(local_time))'''

# str_time=local_time[11:13];
# int_time=int(str_time);
# if(int_time<=12):
#     print("Good Morning!");
# elif(int_time>=12 and int_time<17):
#     print("Good Afernoon!");
# else:
#     print("Good Evening!");

# /////////////////////////////////////////////////////////

import time;
time=time.strftime('%H:%M:%S')
# print(time);
time_in_hour=time[0:2];
time_int=int(time_in_hour);
if(time_int<=12):
    print("Good Morning!");
elif(time_int>=12 and time_int<17):
    print("Good Afernoon!");
else:
    print("Good Evening!");