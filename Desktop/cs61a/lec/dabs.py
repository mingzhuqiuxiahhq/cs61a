def add_rationals(x, y):
        nx, dx = numer(x), denom(x)
        ny, dy = numer(y), denom(y)
        return rational(nx * dy + ny * dx, dx * dy)
def mul_rationals(x, y):
        return rational(numer(x) * numer(y), denom(x) * denom(y))
def print_rational(x):
        print(numer(x), '/', denom(x))
def rationals_are_equal(x, y):
        return numer(x) * denom(y) == numer(y) * denom(x)


def rational(n, d):
        return [n, d]
def numer(x):
        return x[0]
def denom(x):
        return x[1]



half = rational(1,2)

print_rational(half)

third = rational(1,3)
print_rational(mul_rationals(half, third))

def divisors(n):
    return [1] + [x for x in range(2,n) if n % x == 0]

def w(a,h):
    assert a % h == 0
    return a // h

def per(w,h):
    return 2 * (w+h)

def min_p(a):
    """
    >>> area = 80
    >>> w(area, 5)
    16
    >>> per(16, 5)
    42
    >>> per(10, 8)
    36
    >>> min_p(area)
    36
    >>> [min_p(n) for n in range(1, 10)]
    [4, 6, 8, 8, 12, 10, 16, 12, 12]
    """
    height = divisors(a)
    p = [per(w(a,h),h) for h in height]
    return min(p)

def tree(root, branches=[]):
    # this is a constructor - it builds new values
    for branch in branches:
        assert is_tree(branch)
    return [root] + list(branches)

def root(tree):
    #selector that just returns values
    return tree[0]
def branches(tree):
    #selector that just returns values
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_t1(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_t1(n-2), fib_t1(n-1)
        fib_n = root(left) + root(right)
        return tree(fib_n, [left,right])

def leaves(tree):
    if is_leaf(tree):
        return [root(tree)]
    else:
        return sum( [leaves(b) for b in branches(tree)], [])

def inc_leaves(t):
    if is_leaf(t):
        return tree(root(t)+1)
    else:
        bs = [inc_leaves(b) for b in branches(t)]
        return tree(root(t),bs)
def inc(t):
    return tree(root(t) +1, [inc(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def is_link(s):
    return s == empty or (len(s)==2 and is_link(s[1]))

def link(first, rest):
    return [first, rest]

def first(s):
    assert is_link(s), 'first only applies to linked list'
    assert s != empty, 'empty linked list has no first element'
    return s[0]

def rest(s):
    assert is_link(s), 'rest only applies to linked list'
    assert s != empty, 'empty linked list has no rest'
    return s[1]
empty = 'empty'
def extend_links(s,t):
    if s == empty:
        return t
    else:
        return link(first(s), extend_links(rest(s), t))
