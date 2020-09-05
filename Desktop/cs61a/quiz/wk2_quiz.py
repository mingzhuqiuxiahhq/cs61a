

def lens(prev= lambda x: 0):
    """
put1 = lens()
get2, put2 = put1('cat','animal')
get3, put3 = put2('table', 'furniture')
get4, put4 = put3('cup','utensil')
get5, put5 = put4('thesis','paper')
    """

    def put(k,v):
        def get(k2):
            if k2 == k:
                return v
            else:
                return prev(k2)
        return get, lens(get)
    return put



def storeroom(helium, fn_even, fn_odd):
    """
    storeroom(1324, lambda x,y: x+y, lambda x,y: x*y)  # 4 + 2 > 3*1
    True
    """
    even_defined, odd_defined = False, False
    even, odd = None, None
    while helium > 0:
        digit, helium = helium % 10, helium // 10
        if digit % 2 == 0:
            if not even_defined:
                even = digit
                even_defined = True
            else:
                even = fn_even(even, digit)
        else:
            if not odd_defined:
                odd = digit
                odd_defined = True
            else:
                odd = fn_odd(odd,digit)
    return even > odd

def scul(ruler, k):
    """
    1 2 3 4
    """
    if ruler == 0 or k == 0:
        return 0
    a = (ruler % 10) + (scul(ruler // 10, k-1) * 10)
    b = scul(ruler // 10, k)
    return max(a,b)
