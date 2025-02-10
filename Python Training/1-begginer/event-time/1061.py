import datetime
import math

def main():
    initialDay = input()
    for word in initialDay.split():
        if word.isdigit():
            initialDay = int(word)
       
    initialTime = input().split(" : ")
    initialHour, initialMinute, initialSecond = initialTime
    initialHour = int(initialHour)
    initialMinute = int(initialMinute)
    initialSecond = int(initialSecond)

    beginning = datetime.datetime(year=2025, month=4, day=initialDay, hour=initialHour, minute=initialMinute, second=initialSecond)
    
    finalDay = input()
    for word in finalDay.split():
        if word.isdigit():
            finalDay = int(word)
        
    finalTime = input().split(" : ")
    finalHour, finalMinute, finalSecond = finalTime
    finalHour = int(finalHour)
    finalMinute = int(finalMinute)
    finalSecond = int(finalSecond)
    
    end = datetime.datetime(year=2025, month=4, day=finalDay, hour=finalHour, minute=finalMinute, second=finalSecond)
    
    interval = end - beginning
    totalSeconds = interval.total_seconds()
    
    totalDays = 0
    if totalSeconds > 0:
        totalDays = math.trunc(totalSeconds/86400)
        totalSeconds = math.fmod(totalSeconds, 86400)
    
    totalHours = 0
    if totalSeconds > 0:
        totalHours = math.trunc(totalSeconds/3600)
        totalSeconds = math.fmod(totalSeconds, 3600)
    
    totalMinutes = 0
    if totalSeconds > 0:
        totalMinutes = math.trunc(totalSeconds/60)
        totalSeconds = math.fmod(totalSeconds, 60)
    
    print('%.0f dia(s)' %(totalDays))
    print('%.0f hora(s)' %(totalHours))
    print('%.0f minuto(s)' %(totalMinutes))
    print('%.0f segundo(s)' %(totalSeconds))

main()