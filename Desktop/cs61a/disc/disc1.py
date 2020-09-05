def jacket(temp, rain):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if rain == True or temp < 60:
        return True
    else:
        return False


def double(x):
    return x * 2
def triple(x):
    return x * 3
hat = double
double = triple
