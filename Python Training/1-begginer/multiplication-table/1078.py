def main():
    factor = int(input())
    product = factor
    
    for _ in range(10):
        print('%i x %i = %i' %(_ + 1, factor, product))
        product += factor
    
main()