def square(x):
    """This function gives the square of the input

    Parameters
    ----------
    x : float
        A number

    Returns
    -------
    float
        Square of the number
    """
    return x**2


def cube(x):
    return x**3


def power(x):
    return f"Square of {x}: {square(x)} and Cube of {x}: {cube(x)}"

def sin(x):
    return x - (x**3)/6 + (x**5)/120 - (x**7)/5040
