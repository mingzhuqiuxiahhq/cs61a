"""
def sum_unique(n):

    sum, one, two, three, four, five, six, seven, eight, nine = 0,0,0,0,0,0,0,0,0,0
    if n < 10:
        return n
    else:
        if n // 10 == 1:
            one += 1
        elif n // 10 == 2:
            two = 1
        elif n // 10 == 3:
            three = 1
        elif n // 10 == 4:
            four = 1
        elif n // 10 == 5:
            five = 1
        elif n // 10 == 6:
            six = 1
        elif n // 10 == 7:
            seven = 1
        elif n // 10 == 8:
            eight = 1
        elif n // 10 == 9:
            nine = 1
        sum = sum +
"""

def sum_unique(n):
    result = 0
    while  n > 0:
        last, wo_last, include = n % 10, n // 10 , True
        while wo_last > 0:
            if wo_last % 10 == last:
                include = False
            wo_last //= 10
        if include:
            result = result + last
        n = n // 10
    return result
