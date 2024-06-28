from time import *
import random as r
def mistake(parTest,userTest):
    error=0
    for i in range(len(parTest)):
        try:
            if parTest[i]!=userTest[i]:
                error=error+1
        except:
            error=error+1
    return error
def speed_time(time_start,time_end,userinput):
    time_delay=time_end-time_start
    time_round=round(time_delay,2)
    speed=len(userinput)/time_round
    return round(speed)
test=["python is a high-level programming language","python was first released in 1991","python interpreter are available for many operating system","python is free to use"]
test1=r.choice(test)
print("       *******Typing  speed*******   ")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter:")
time_2=time()
print("Speed:",speed_time(time_1,time_2,testinput),"w/sec")
print("Error:",mistake(test1,testinput))