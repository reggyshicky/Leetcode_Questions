import math
def frogJump(X,Y,D):
    result = (Y - X) / D
    return math.ceil(result) #math.ceil() always rounds to the nearest whole number regardless ie 2.1 will be 3


print(frogJump(10, 85, 30))
print(frogJump(15,200,7))