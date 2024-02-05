from ProbabilityDensityFunction import PDF
"""def Probability(PDF, args, c, GT=True) :
"""

def Probability(PDF, args, c, GT=True):
    mu = args[0]
    sigma = args[1]
    a = mu - 5 * sigma
    b = c
    s0 = 0
    s1 = 0
    s2 = 0
    m = 500
    h = (b - a) / (2 * m)

    myTuple = (a, mu, sigma)

    s0 = PDF(myTuple)
    myOtherTuple = (b, mu, sigma)
    s0 += PDF(myOtherTuple)

    for x in range(1000):

        myList = list(myTuple)
        myList[0] = myList[0] + h
        myTuple = tuple(myList)

        if x % 2 == 0:
            s1 += (PDF(myTuple))

        if x % 2 != 0:
            s2 += (PDF(myTuple))

    approximation = (h/3)*(s0+(4*s1)+(2*s2))

    return approximation


def main():
    args = 100, 12.5
    c = 105
    GT = False
    if GT == False:
        Comparator = "<"
    else:
        Comparator = ">"

    print("P(x",Comparator,c,"|N(",args[0],",",args[1],")) =",Probability(PDF, args, c, False))

main()

