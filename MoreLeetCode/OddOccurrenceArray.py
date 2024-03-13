def oddOccurence(Array):
    result = 0
    
    for i in Array:
        result = result ^ i
    return result

print(oddOccurence([2,5,2,9,6,9,6]))
print(oddOccurence([5,6,5,9,8,9,8,6,1]))