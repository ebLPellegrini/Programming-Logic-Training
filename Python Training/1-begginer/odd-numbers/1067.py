def main():
    X = input()
    X = int(X)
    
    if X > 1000:
        print('Number above 1000 is not allowed')
        return 1
    else:
        for _ in range (1, X + 1, 2):
            print(_)
main()