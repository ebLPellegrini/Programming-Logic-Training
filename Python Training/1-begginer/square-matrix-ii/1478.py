from math import fmod
def main():
    while True:
        array_Size = int(input())
        
        if array_Size == 0:
            break
        
        arr = []
        for i in range(1, (array_Size+1)):
            tmp = []
            value = i
            for _ in range(array_Size):
                tmp.append(abs(value))
                if value == 1:
                    value -= 3
                else:
                    value -= 1
            arr.append(tmp)
            
        for i in range(array_Size):
            answer = ''
            for _ in range(array_Size):
                answer += " %3d" %arr[i][_]
            print(answer[1:])
        print("")
                
main()    
            
                
                