def makeadder(n):
    def adder(k):
        return k + n
    return adder


def square(x):
    return x*x

def triple(x):
    return 3 * x

def compose2(f,g):
    def h(x):
        return f(g(x))
    return h

def sqrt(a):
    def update(x):
        return sqrud(x,a)
    def close(x):
        return approx(x*x,a)
    return improve(update,close)

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def sqrud(x,a):
    return (x+ a/x) / 2

def approx(x,y,tolerance=1e-15):
    return abs(x-y) < tolerance

def newton(f, df):
    def upd(x):
        return x - f(x) / df(x);
    return upd

def fdz(f, df):
    def nzero(x):
        return approx(f(x), 0)
    return improve(netwon(f,df), nzero)

def sqnt(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return newton(f,df)


def trace1(fn):
    def traced(x):
        print('Calling', fn, 'on argument',x)
        return fn(x)
    return traced

def square(x):
    return x*x


def sum_sqr_up(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total
