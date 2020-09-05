"""The first python prgram"""

from operator import floordiv, mod

def divide_exact(n, d=10):
  """Return the quotient and remainder of dividing N by D
  >>> q, r = divide_exact(505, 3)
  >>> q
  168
  >>> r
  1
  """
  return floordiv(n,d), mod(n,d)

def absValue(x):
    """Return absolute value of x"""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
