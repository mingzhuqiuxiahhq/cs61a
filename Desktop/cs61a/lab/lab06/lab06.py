this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    count = 0
    def adder(b):
        nonlocal a
        nonlocal count
        total = a + b + count
        count += 1
        return total
    return adder


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    pre,cur = 0,1
    count = 0
    def m_f():
        nonlocal pre, cur
        nonlocal count
        if count == 0:
            count += 1
            return pre
        elif count == 1:
            count += 1
            return cur
        else:
            count += 1
            cur, pre = cur + pre, cur
            return cur
    return m_f


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    #needs to be a mutation list
    #get a iterator/generator to pass out the position of the match int
    #
    contents = lst
    def mut_list(message, target_position,value=elem):
        nonlocal contents
        if message == 'insert':
            contents = contents.insert(contents.index(target_position)+1,value)


    return mut_list


#    if type(lst) == list:
#        if entry in lst:
#            [lst.insert(lst.index(entry)+1,elem)]
#            return lst[:lst.index(entry)+2] + insert_items(lst[lst.index(entry)+2:], entry,elem)
#        else:
#            return lst[:]
#    else:
#        return []
