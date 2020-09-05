LAB_SOURCE_FILE = __file__


def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(reverse_iter)))
    >>> print("Do not use lst[::-1], lst.reverse(), or reversed(lst)!") if any([r in cleaned for r in ["[::", ".reverse", "reversed"]]) else None
    """
    index, new_list = len(lst)-1, []
    while index >= 0:
        new_list = new_list  + [lst[index]]
        index -= 1
    return new_list

def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(reverse_recursive)))
    >>> print("Do not use lst[::-1], lst.reverse(), or reversed(lst)!") if any([r in cleaned for r in ["[::", ".reverse", "reversed"]]) else None
    """
    if len(lst) <= 0:
        return []
    else:
        return reverse_recursive(lst[1:len(lst)]) + [lst[0]]


from math import sqrt
def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """

    def lati(city_a,city_b):
        return (get_lat(city_a) - get_lat(city_b)) * (get_lat(city_a) - get_lat(city_b))

    def long(city_a,city_b):
        return (get_lon(city_a) - get_lon(city_b)) * (get_lon(city_a) - get_lon(city_b))

    def distance_cal(lat,lon):
        return sqrt(lati(city_a,city_b) + long(city_a,city_b))

    return distance_cal(lati, long)
#
#    x1, y1, x2, y2 = city_a[1], city_b[1], city_a[2], city_b[2]
#    lati, long = (x2-y2), (x1-y1)
#    return sqrt((lati*lati)+(long*long))


def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """

    def lati(city,lat):
        return (get_lat(city) - lat) * (get_lat(city) - lat)

    def long(city, lon):
        return (get_lon(city) - lon) * (get_lon(city) - lon)

    def distance_cal(city,latit,longt):
        return sqrt(lati(city,latit) + long(city,longt))



    #def

    def closer(distance_a, distance_b):

        if distance_a > distance_b:
            return get_name(city_b)
        else:
            return get_name(city_a)


    return closer(distance_cal(city_a,lat,lon), distance_cal(city_b,lat,lon))



#    x1, y1, x2, y2 = city_a[1], city_b[1], city_a[2], city_b[2]
#    a_dist = sqrt(((x1-lat)*(x1-lat))+((x2-lon)*(x2-lon)))
#    b_dist = sqrt(((y1-lat)*(y1-lat))+((y2-lon)*(y2-lon)))
#    if a_dist > b_dist:
#        return city_b[0]
#    else:
#        return city_a[0]

def check_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    >>> change_abstraction(False)
    """


# Treat all the following code as being behind an abstraction layer, you shouldn't need to look at it!

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name" : name, "lat" : lat, "lon" : lon}
    else:
        return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    def check(w1, w2, additional):
        if len(w1) == 0:
            return w2[0:]
        elif w1[0] == w2[0]:
            return check(w1[1:], w2[1:], additional)
        else:
            additional = w2[0]
            return additional + check(w1,w2[1:], ""+additional)

    return check(w1,w2, "")
