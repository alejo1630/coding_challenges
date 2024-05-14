# https://www.codewars.com/kata/65ba420888906c1f86e1e680/train/python


def collinearity(x1, y1, x2, y2):

    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0) or (x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0):

        return True
    
    elif (x2 == 0 or y2 == 0):

        return False

    elif x1/x2 == y1/y2:
        
        return True

    else:

        return False

print(collinearity(1,1,1,1))
print(collinearity(1,2,2,4))
print(collinearity(1,1,6,1))
print(collinearity(1,2,-1,-2))
print(collinearity(1,2,1,-2))
print(collinearity(4,0,11,0))
print(collinearity(0,1,6,0))
print(collinearity(4,4,0,4))
print(collinearity(0,0,0,0))
print(collinearity(0,0,1,0))
print(collinearity(5,7,0,0))