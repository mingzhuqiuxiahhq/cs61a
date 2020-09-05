def split(n):
    return n // 10, n % 10

def sum_digit(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digit(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
    return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
        all_but_last, last = split(n)
        luhn_digit = sum_digit(last * 2)
        if n < 10:
            return luhn_digit
        else:
            return luhn_sum(all_but_last) + luhn_digit


print(luhn_sum(1234))


def ic(n):
    if n > 10:
        ic(n//10)
        print(n)
    else:
        print(n)


def ic(n):
    if n > 10:
        ic(n//10)
        print(n)
    else:
        print(n)






def inv_cas(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n > 0:
        f(n)
        g(g)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
