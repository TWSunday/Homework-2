import math
def PDF(args):
    """
    This function takes input from a tuple to perform a Gaussian/Normal probability distribution function
    :param tuple: takes a tuple which contains x, mu, and sigma in that order
    :return: f(x)
    """
    x = args[0]
    mu = args[1]
    sigma = args[2]

    a = 1/(sigma*math.sqrt(2*math.pi))
    b = ((x-mu)/sigma)**2
    c = math.exp(-.5*b)

    solution = a*c

    return solution
