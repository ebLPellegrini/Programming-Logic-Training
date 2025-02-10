hours = input().split(" ")

start_Hour, start_Minute, final_Hour, final_Minute = hours

start_Hour = int(start_Hour)
start_Minute = int(start_Minute)
final_Hour = int(final_Hour)
final_Minute = int(final_Minute)

total_Time_Hour = 0
total_Time_Minute = 0

if start_Hour <= final_Hour and start_Minute <= final_Minute:
    total_Time_Hour = final_Hour - start_Hour
    total_Time_Minute = final_Minute - start_Minute
elif start_Hour < final_Hour and start_Minute > final_Minute:
    total_Time_Hour = final_Hour - start_Hour - 1
    total_Time_Minute = (final_Minute - start_Minute) + 60
elif start_Hour >= final_Hour and start_Minute <= final_Minute:
    total_Time_Hour = final_Hour - start_Hour + 24
    total_Time_Minute = final_Minute - start_Minute
elif start_Hour >= final_Hour and start_Minute >= final_Minute:
    total_Time_Hour = final_Hour - start_Hour + 23
    total_Time_Minute = (final_Minute - start_Minute) + 60
elif start_Hour < final_Hour and start_Minute == final_Minute:
    total_Time_Hour = final_Hour - start_Hour
    total_Time_Minute = 0
    
if start_Hour == final_Hour and start_Minute == final_Minute:
    total_Time_Hour = 24
    total_Time_Minute = 0
    
print('THE GAME LAST %i HOUR(S) AND %i MINUTE(S)' %(total_Time_Hour, total_Time_Minute))