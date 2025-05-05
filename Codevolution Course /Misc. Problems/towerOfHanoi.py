def towerOfHanoi(n, fromRod, toRod, usingRod):
    if n == 1:
        print('Move disk 1 from %s to %s' %(fromRod, toRod))
        return
    
    towerOfHanoi(n-1, fromRod, usingRod, toRod)
    print('Move disk %i from %s to %s' %(n, fromRod, toRod))
    towerOfHanoi(n-1, usingRod, toRod, fromRod)
    
towerOfHanoi(3, 'A', 'C', 'B')