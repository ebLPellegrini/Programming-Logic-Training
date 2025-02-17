def main():
    test_Cases = int(input())
    
    for _ in range(test_Cases):
        problem = input()
        
        if problem == 'P=NP':
            print('skipped')
        else:
            addend0, addend1 = map(int, problem.split("+"))
            
            result = addend0 + addend1
            print('%i' %(result))
main()