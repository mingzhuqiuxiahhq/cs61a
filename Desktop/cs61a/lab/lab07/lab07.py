def insert_into_all(item, nested_list):
    """Assuming that nested_list is a list of lists, return a new list
    consisting of all the lists in nested_list, but with item added to
    the front of each.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + ls for ls in nested_list]


def subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists). The subsequences can appear in any order.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if s == []:
        return [[]]
    else:
        subset = subseqs(s[1:])
        return subset + insert_into_all(s[0], subset)




def inc_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = inc_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> inc_subseqs([])
    [[]]
    >>> seqs2 = inc_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """

    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev )
        else:
            a = subseq_helper(s[1:],s[0])
            b = subseq_helper(s[1:], prev )
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, 0)


def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1

    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    while m < len(first) and n < len(first) and sum(first[:m]) != sum(second[:n]):
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'


def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    for i in range(len(lst)-1,-1,-1):
        lst.append(lst.pop(i))


cs61a = {
    "Homework": 2,
    "Lab": 1,
    "Exam": 50,
    "Final": 80,
    "PJ1": 20,
    "PJ2": 15,
    "PJ3": 25,
    "PJ4": 30,
    "Extra credit": 0
}

def make_glookup(class_assignments):
    """ Returns a function which calculates and returns the current
    grade out of what assignments have been entered so far.

    >>> student1 = make_glookup(cs61a) # cs61a is the above dictionary
    >>> student1("Homework", 1.5)
    0.75
    >>> student1("Lab", 1)
    0.8333333333333334
    >>> student1("PJ1", 18)
    0.8913043478260869
    """
    total = 0
    avail_grade = 0
    student_grade = 0
    def grader(assigement, cur_grade):
        nonlocal total, avail_grade, student_grade
        avail_grade += class_assignments.get(assigement)
        student_grade += cur_grade
        total = student_grade/avail_grade
        return total
    return grader



def num_trees(n):
    """How many full binary trees have exactly n leaves? E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    if n == 1 or n == 2:
        return 1
    return


def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    gcount = 0
    def make_counter():
        count = 0
        def create_count(string):
            counter = 0
            nonlocal gcount, count
            if string == 'count':
                count += 1
                return count
            elif string == 'global-count':
                gcount += 1
                return gcount
            elif string == 'reset':
                count = 0
            elif string == 'global-reset':
                gcount = 0
        return create_count
    return make_counter
