def climbingStaircase(n):
    nOfWays = [1, 2]
    
    for i in range(2, n):
        nOfWays.append(nOfWays[i-1] + nOfWays[i-2])
    
    return nOfWays[n-1]    
    
print(climbingStaircase(1))
print(climbingStaircase(2))
print(climbingStaircase(3))
print(climbingStaircase(4))
print(climbingStaircase(5))