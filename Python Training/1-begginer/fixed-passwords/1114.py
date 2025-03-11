def main():
    valid = False
    
    while valid == False:
        attempt = input()
        if attempt == '2002':
            valid = True
            print('Access Granted')
        else:
            print('Access Denied')
        
main()