def times(m,n):
    if n == 1:
        return m
    elif n == 0:
        return 0
    else:
        return m + times(m,n-1)

# times(5,3)


def is_prime(n, m=2):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """

    if n == 1:
        return False
    elif m == n:
        return True
    elif n % m == 0:
        return False
    else:
        return is_prime(n,m+1)

def stair_way(n,m):
    if m == 0 or n == 0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        stair_way(n-1) + stair_way(n-2)
def count_k(n,k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n == k:
        return 1
    elif k == 1:
        return 1
    else:
        return count_k(n,k-1) + count_k(n-k,k)

def test():
    """
    >>> a = [1,5,4,[2,3],3]

    >>> print(a[0],a[-1])
    1 3
    >>> len(a)
    5
    >>> 2 in a
    False
    >>> 4 in a
    True
    >>> a[3][0]
    2
    """

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [a * (a-1) for a in s if a % 2 !=0]

#def max_product(s):
    """
    >>> max_product([10,3,1,9,2])
    90
    >>> max_product([5,10,510,5])
    125
    >>> max_product([])
    1
    """
#    if s == []:
#        return 1



#    return []* [a for a in s if a > s[]]

def chn(n):

    """
    >>> chn(123)
    False
    >>> chn(3241968)
    True
    >>> chn(3245968)
    False
    """
    if n//10 == 0:
        return True
    return ((n//10)%10) < (n % 10) and ((n // 10)%10) < ((n//100)%10) and chn(n//100)



def cmn(n):
    """
    >>> cmn(103)
    False
    >>> cmn(153)
    True
    >>> cmn(3241968)
    False
    >>> cmn(2345986)
    True
    """
    def helper(x, is_increasing):

        if x // 10 == 0:

            return True

        if is_increasing and ((x % 10) < (x //10)%10):

            return helper(x // 10, is_increasing)

        return (x % 10) > ((x //10)%10) and helper(x//10,False)
    return helper(n,True)
























####
