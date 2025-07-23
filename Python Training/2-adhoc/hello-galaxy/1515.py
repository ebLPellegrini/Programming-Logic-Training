def main():
        verify = True
        while verify == True:
            test_cases = int(input())
            if test_cases == 0:
                verify = False
            else:
                print(first_planet(test_cases))
        
def first_planet(test_cases):
    year_first_message = 2114  
    planet_first_message = ''
    
    
    for _ in range(test_cases):
        planet_name, year_arrival, years_taken = input().split()
        year_arrival = int(year_arrival)
        years_taken = int(years_taken)
        
        year_sent = year_arrival - years_taken
        
        if year_first_message > year_sent:
            year_first_message = year_sent
            planet_first_message = planet_name
            
    return planet_first_message
        
main()