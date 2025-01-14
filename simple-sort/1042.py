str_list = input().split(" ")
int_list = []

for s in str_list:
    int_list.append(int(s))
    
int_list.sort()
for i in int_list:
    print('%i' %(i))

print()

for s in str_list:
    print('%s' %(s))