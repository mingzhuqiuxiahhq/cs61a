from unicodedata import lookup
chinese = ['coin','string','myriad']
suits = chinese
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0:2] = ['heart','diamond']

[lookup('BLACK ' + s.upper() + ' SUIT') for s in suits]

def mk_wd(balance):
    def withdrew(amount):
        nonlocal balance
        if balanace >= amount:
            balance -= amount
            return balance
        else:
            return 'Insufficient balance'
    return withdrew


primes = [2,3,5,7,11]
it_pr = iter(primes)


def plus_minus(x):
    yield x
    yield -x
    yield x+x

def connect(name=None):
    """A connector between constraints"""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
