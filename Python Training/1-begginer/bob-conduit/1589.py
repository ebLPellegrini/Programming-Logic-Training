def main():
    total_inputs = int(input())
    
    for _ in range(total_inputs):
        r1, r2 = map(int, input().split())
        r_conduit = r1 + r2
        print(r_conduit)
    
    
main()