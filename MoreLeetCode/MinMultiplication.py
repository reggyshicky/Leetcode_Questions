def solution(A):
    multiplications = 0
    for i in range(len(A)):
        index = i
        value = A[i]
        
        if index % 4 == 0 and value <=0: #0, 4, 8...value should be positive
            multiplications += 1
        elif index % 2 == 1 and value != 0: #1,5,9.. value should be zero
            multiplications += 1
        elif index % 4 == 2 and value >= 0: #2,6,10 value should be negative
            if value == 0:
                return -1 #value cannot be converted to zero
            multiplications +=1
    return multiplications

#Test cases
A1 = [1, 0, 3, 4, 5, 0, 6]
A2 = [7, 4, -3, 0, -5, 1, 0]
A3 = [-5, 0, 3, 0]

print(solution(A1))  # Output: 3
print(solution(A2))  # Output: -1
print(solution(A3))  # Output: 2   
        
            
    
    















# def solution(A):
#     multiplications = 0

#     for i in range(len(A)):
#         index = i
#         value = A[i]

#         if index % 4 == 0 and value <= 0:  # For indices 0, 4, 8, ..., the element should be positive
#             multiplications += 1
#         elif index % 4 == 2 and value >= 0:  # For indices 2, 6, 10, ..., the element should be negative
#             if value == 0:  # If the element is 0, return -1 as it cannot be made negative
#                 return -1
#             multiplications += 1
#         elif index % 2 == 1 and value != 0:  # For indices 1, 3, 5, ..., the element should be zero
#             multiplications += 1

#     return multiplications

# Test cases
# A1 = [1, 0, 3, 4, 5, 0, 6]
# A2 = [7, 4, -3, 0, -5, 1, 0]
# A3 = [-5, 0, 3, 0]

# print(solution(A1))  # Output: 3
# print(solution(A2))  # Output: -1
# print(solution(A3))  # Output: 2