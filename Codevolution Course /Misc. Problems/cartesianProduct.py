def cartesianProduct(arr1, arr2):
    finalSet = []
    
    for i in arr1:
        for j in arr2:
            finalSet.append([i, j])
    
    return finalSet

A = [1, 2]
B = [3, 4, 5]
print(cartesianProduct(A, B))