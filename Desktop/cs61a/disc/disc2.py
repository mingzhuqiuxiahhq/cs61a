"""
*** High order function ***
A function that 'takes' or 'return' a function as a parameter
-- example of taking a functions
def hof(sq):
    #takes function as a parameter and
    x = 5
    sq(x)
    #returns a function
    return sq
-- or just returning a function without an input function parameter

def hof2(x):
    return hof(x)


-- it can be used to generalise functions  i.e.

def sq(x):
    return x*x

def

*** currying
 this allows users to convert a function that takes many parameter args into a
 chain of function that each takes a single args

def curried_pow(x):
     def h(y):
         return pow(x,y)
     return h
curried_pow(2)(3)

"""
#top level function take another function or operator
def curry2_not_lambda(operate):
#second function that takes an arg
    def sec_f(x):
#third function that take an arg and return
        def third_f(y):
            return operate(x, y)
        return third_f
    return sec_f


lamb_curry = lambda h: lambda x: lambda y: h(x,y)



n = 5
def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)
f = f(g, n)
g = (lambda y: y())(f)



def keep_ints(cond, n):
        i = 1
        while i <= n:
            if cond(i) == True:
                print(i)
            i +=1

def mk(n):
    def do_k(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return do_k

def print_delayed(x):

    def delay_print(y):
        print(x)
        return print(y)
    return delay_print
    """
    f = print_delayed(1)
    f = f(2)
    1
    f = f(3)
    2
    f = f(4)(5)
    3
    4
    f("hi")
    5
    """


def print_n(n):

    def inner_print(x):
        if n <= 0 :
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print
