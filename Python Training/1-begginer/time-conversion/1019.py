import math

seconds = int(input())
hours = 0
minutes = 0

if seconds < 60 and seconds >= 0:
    print("0:0:%i" %(seconds))
else:
    minutes = math.trunc(seconds / 60)
    seconds = math.fmod(seconds, 60)
    
    if minutes < 60 and minutes >= 1:
        print("0:%i:%i" %(minutes, seconds))
    else:
        hours = math.trunc(minutes / 60)
        minutes = math.fmod(minutes, 60)
        print("%i:%i:%i" %(hours, minutes, seconds))