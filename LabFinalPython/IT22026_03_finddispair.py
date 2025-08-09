import math
def distanceOfTwoPair(a1,a2,b1,b2):
    disa = a1 - a2
    disb = b1 - b2
    print(math.sqrt(disa*disa + disb*disb))

distanceOfTwoPair(1,4,2,6)