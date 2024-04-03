from typing import List
def reconstructMatrix(upper: int, lower:int, colsum: List[int]) -> List[List[int]]:
    n = len(colsum)
    upper_list = [0 for _ in range(n)]
    lower_list = [0 for _ in range(n)]
    
    for i, v in enumerate(colsum):
        if v == 1:
            if upper > lower:
                upper_list[i] = 1
                upper -= 1
            else:
                lower_list[i] = 1
                lower -= 1
        elif v == 2:
            upper_list[i] = lower_list[i] = 1
            upper, lower = upper - 1, lower -1
    return [upper_list, lower_list] if upper == lower == 0 else []

print(reconstructMatrix(2, 1, [1, 1, 1])) #[[1,0,1],[0,1,0]]
print(reconstructMatrix(2, 3, [2, 2, 1, 1])) #[]
print(reconstructMatrix(5, 5, [2,1,2,0,1,0,1,2,0,1])) #[[1,0,1,0,1,0,0,1,0,1],[1,1,1,0,0,0,1,1,0,0]]
    



# Given the following details of a matrix with n columns and 2 rows :
# The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
# Your task is to reconstruct the matrix with upper, lower and colsum.
# Return it as a 2-D integer array.
# If there are more than one valid solution, any of them will be accepted.
# If no valid solution exists, return an empty 2-D array.
