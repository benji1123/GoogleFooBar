from math import sqrt

def isPerfectSquare(num):
    return sqrt(num) == int(sqrt(num)) 

def solution(area):
    output = []
    potentialSquare = area
    while area > 0:
        if isPerfectSquare(potentialSquare):
            # update numbers
            area -= potentialSquare
            output.append(potentialSquare)
            potentialSquare = area
        else:
            # check next largest possibility
            potentialSquare -= 1
    return output

# prompt input
testVal = int(input("enter an integer-area: "))
print("use these panels: ", solution(testVal))
