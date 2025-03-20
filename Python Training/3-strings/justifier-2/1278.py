import re

def main():
    validation = False
    text = []
    count = 0
    
    while validation == False:
        lines = int(input())
        if lines == 0:
            validation = True
            break
        
        biggest_String_Size = 0
        
        for _ in range(lines):
            text.append(input())
            text[_] = re.sub(r'\s+', ' ', text[_].strip())
            
            if len(text[_]) > biggest_String_Size:
                biggest_String_Size = len(text[_])
                
        for _ in range(lines):
            if _ == 0 and count != 0:
                print()
                    
            if len(text[_]) == biggest_String_Size:
                print(text[_])
            else:
                print(text[_].rjust(biggest_String_Size))
        text.clear()
        count += 1
    
main()