from math import pow
def main():
    while True:
        matrix_size = int(input())
        if matrix_size <= 0 or matrix_size > 15:
            break
        
        arr = []
        for i in range(matrix_size):
            tmp = []
            count = i
            for j in range(matrix_size):
                tmp.append(pow(2, count))
                count += 1
            arr.append(tmp)
    
        for i in range(matrix_size):
            answer = ''
            for j in range(matrix_size):
                answer += '{number:{width}d}'.format(width=len(str(arr[matrix_size-1][matrix_size-1]))-1, number= int(arr[i][j]))
            print(answer[1:])
        print("")

main()