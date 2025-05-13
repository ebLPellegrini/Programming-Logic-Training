def main():
    instances = int(input())
    
    for i in range(instances):
        string = input()
        exclamations = string.count("!")
        
        string = string.split('!')
        number = int(string[0])
        
        print(oracleCalculus(number, exclamations))
       
def oracleCalculus(number, exclamations):
    result = 1
     
    while number >= 1:
        result *= number
        number = number - exclamations
        
    return result
                    
main()