hours = input().split(" ")

start, end = hours

start = int(start)
end = int(end)
total_Time = 0

if start > end:
    total_Time = (24 - start) + end
elif start < end:
    total_Time = abs(end - start)
elif start == end:
    total_Time = 24
    
print('THE GAME LAST %i HOUR(S)' %(total_Time))