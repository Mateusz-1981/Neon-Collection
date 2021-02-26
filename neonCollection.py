'''a collection of custom objects used to store/manipulate/read data'''

class Pair:
    '''Pair(x: 'list, tuple, set or dict') -> Pair[(a, b), (c, d)]
       Dict-like object without distinction between keys and values.

       'Pair' is an object the value of which is stored as self._PAIR
       and it takes the form of a list with only tuples inside, which
       contain exactly 2 values.'''

    def __init__(self, val = ()):
        self._PAIR = Pair._fromX(val)

    def __repr__(self):
        return f'Pair{self._PAIR}'

    def __add__(self, other):
        '''returns self + value'''
        if not isinstance(other, Pair):
            raise TypeError(f'{type(other)} cannot be added to Pair object')
        l = self.copy()
        for w in other:
            l.append(w)
        return l

    def __sub__(self, other):
        '''subtracts elements present in the subtrahend from minuend'''
        if not isinstance(other, Pair):
            raise TypeError(f'{type(other)} cannot be subtracted from Pair object')
        l = self.copy()
        for w in other:
            if w in l:
                l._PAIR.remove(w)
        return l

    def __mul__(self, multiplier):
        '''returns self * value'''
        if not isinstance(multiplier, int):
            raise TypeError(f'multiplier has to be type int, not {type(multiplier)}')
        return Pair(self._PAIR * multiplier)

    def __eq__(self, other):
        '''returns self == value'''
        if not isinstance(other, Pair):
            raise TypeError(f'{type(other)} cannot be compared with Pair object')
        if self._PAIR == other._PAIR:
            return True
        else:
            return False

    def __iter__(self):
        '''yields Pair elements'''
        for w in self._PAIR:
            yield w

    def __getitem__(self, key):
        '''returns an element from Pair by index'''
        return self._PAIR[key]

    def __delitem__(self, key):
        '''deletes an element from Pair by index'''
        del self._PAIR[key]

    def __len__(self):
        '''returns the lenght of Pair'''
        return len(self._PAIR)

    def _isiterable(obj):
        '''returns True if obj is iterable'''
        try:
            for w in obj:
                break
        except TypeError:
            return False
        else:
            return True

    # transformation methods
    def _fromX(val):
        '''turns a list, tuple or dict into Pair'''
        par = []
        if isinstance(val, dict):
            for key, arg in val.items():
                par.append((key, arg),)
        else:
            for pair in val:
                if Pair._isiterable(pair) and len(pair) == 2:
                    par.append(tuple(pair))
                else:
                    raise ValueError(f'"{pair}" argument is not an iterable or len != 2')
        return par

    def toDict(self, side: 'key: \'left\' or \'right\'' = 'left'):
        '''returns Pair as dict. determine 'side' to specify
           which side should be key'''
        if side != 'left' and side != 'right':
            raise ValueError(f'invalid side: {side}')
        dic = {}
        for w in self._PAIR:
            if side == 'right':
                dic[w[1]] = w[0]
            else:
                dic[w[0]] = w[1]
        return dic

    def toList(self):
        '''returns Pair as list'''
        lis = []
        for w in self._PAIR:
            lis.append(list(w))
        return lis

    def copy(self):
        '''returns a shallow copy of Pair'''
        return Pair(self._PAIR)

    # appending/deleting methods
    def append(self, pair):
        '''append a pair of values to Pair'''
        if len(pair) == 2 and not isinstance(pair, dict):
            self._PAIR.append(tuple(pair))
        elif len(pair) == 1 and isinstance(pair, dict):
            for key, val in pair.items():
                temp = (key, val)
            self._PAIR.append(temp,)
        else:
            raise ValueError('length of a pair has to be exactly 2')

    def insert(self, pair, place):
        '''insert a pair of values to Pair'''
        if len(pair) == 2 and not isinstance(pair, dict):
            self._PAIR.insert(place, tuple(pair))
        elif len(pair) == 1 and isinstance(pair, dict):
            for key, val in pair.items():
                temp = (key, val)
            self._PAIR.insert(place, temp)
        else:
            raise ValueError('length of a pair has to be exactly 2')

    def remove(self, val):
        '''removes pairs with 'val' element'''
        temp = self.readAll(val)
        if len(temp) != 0:
            for w in temp:
                del self._PAIR[self._PAIR.index(w)]
        else:
            raise ValueError(f'{val} is not in Pair')

    def removeByWhole(self, val):
        '''removes pairs equal to val'''
        temp = self._PAIR.count(val)
        if temp != 0:
            for w in range(temp):
                del self._PAIR[self._PAIR.index(val)]
        else:
            raise ValueError(f'{val} is not in Pair')

    # internal order methods
    def swap(self, index):
        '''swaps left and right element in Pair'''
        temp = list(self._PAIR[index])
        temp[0], temp[1] = temp[1], temp[0]
        self._PAIR[index] = tuple(temp)

    def swapAll(self):
        '''swaps left and right element in all pairs in Pair'''
        for w in range(len(self._PAIR)):
            self.swap(w)

    def swapTypes(self, obj: 'object', side = 'left'):
        '''formats Pair to contain elements of the same type on one side'''
        if side != 'left' and side != 'right':
            raise ValueError(f'invalid side: {side}')
        if side == 'right':
            s = True
        else:
            s = False
        for w in self._PAIR:
            if isinstance(w[not s], obj) and not isinstance(w[s], obj):
                self.swap(self._PAIR.index(w))

    def reverse(self):
        '''reverses the order of Pair'''
        l = []
        for w in range(len(self._PAIR) - 1, -1, -1):
            l.append(self._PAIR[w])
        self._PAIR = l

    def sort(self, side: 'choose side to sort by' = 'left', both = False):
        '''sorts pairs by the order of the 'side' element; set 'both' to
           True to also sort the other element (if possible)'''
        if side != 'left' and side != 'right':
            raise ValueError(f'invalid side: {side}')
        if side == 'right':
            s = True
        else:
            s = False
        if both == True:
            s = not s
        temp = self._PAIR.copy()
        flag = True
        while flag:
            flag = False
            for w in range(1, len(temp)):
                if temp[w - 1][s] > temp[w][s]:
                    temp[w - 1], temp[w] = temp[w], temp[w - 1]
                    flag = True
        self._PAIR = temp
        if both == True:
            self.sort(side)

    def _repair(self):
        '''if self._PAIR is broken returns a fixed version (debug tool)'''
        if Pair._isiterable(self._PAIR):
            x = Pair._fromX(self._PAIR)
            if self._PAIR == x:
                return False
            else:
                return x
        else:
            return []

    # reading methods
    def rleft(self):
        '''returns all the left values in list'''
        lis = []
        for w in self._PAIR:
            lis.append(w[0])
        return lis

    def rright(self):
        '''returns all the right values in list'''
        lis = []
        for w in self._PAIR:
            lis.append(w[1])
        return lis

    def read(self, val):
        '''returns the corresponding values from Pair'''
        lis = []
        for w in self._PAIR:
            if w[0] == val:
                lis.append(w[1])
            elif w[1] == val:
                lis.append(w[0])
        return lis

    def readAll(self, val):
        '''returns pairs with 'val' element'''
        lis = []
        for w in self._PAIR:
            if w[0] == val or w[1] == val:
                lis.append(w)
        return lis

    def index(self, val):
        '''returns index of pairs with 'val' element'''
        ind = []
        i = 0
        for w in self._PAIR:
            if w[0] == val or w[1] == val:
                ind.append(i)
            i += 1
        if ind == []:
            raise ValueError(f'{val} is not in Pair')
        else:
            return ind

    def indexByWhole(self, val):
        '''returns index of pairs equal to val'''
        ind = []
        i = 0
        for w in self._PAIR:
            if w == val:
                ind.append(i)
            i += 1
        if ind == []:
            raise ValueError(f'{val} is not in Pair')
        else:
            return ind

    def isSameType(self, side = None):
        '''left/right: checks if in all values on that side are the
           same type; None: checks if all pairs have a common type'''
        if side != 'left' and side != 'right' and side != None:
            raise ValueError(f'invalid side: {side}')
        if side == 'right':
            s = True
        else:
            s = False
        typ = type(self._PAIR[0][s])
        ptyp = True
        typ2 = type(self._PAIR[0][not s])
        if side is None:
            ptyp2 = True
        else:
            ptyp2 = False
        for w in self._PAIR:
            if not isinstance(w[s], typ):
                if not isinstance(w[not s], typ) or side is not None:
                    ptyp = False
            if ((not isinstance(w[s], typ2)
                 and not isinstance(w[not s], typ2))
                and ptyp2):
                ptyp2 = False
            if not ptyp and not ptyp2:
                return False
        else:
            return True

    def isUnique(self, side = 'left'):
        '''returns True if all the elements on the chosen side
           are unique'''
        if side != 'left' and side != 'right':
            raise ValueError(f'invalid side: {side}')
        if side == 'right':
            x = self.rright()
        else:
            x = self.rleft()
        l = []
        for w in x:
            if w not in l:
                l.append(w)
            else:
                return False
        else:
            return True



class Number:
    '''Number(x, base) -> Number (base)
    positive integer that can be represented with any base'''

    symbols = [chr(w) for w in range(48, 58)] + [chr(w) for w in range(65, 91)]

    def __new__(cls, integer, base):
        return super(Number, cls).__new__(cls)

    def __init__(self, integer, base):
        if base <= 1:
            raise ValueError('base has to be >= 2')
        self._base = base
        self._numlist = []
        if isinstance(integer, Number):
            integer = int(integer)
        while integer//self._base != 0:
            self._numlist.append(integer%self._base)
            integer //= self._base
        self._numlist.append(integer%self._base)

    def _checking_decorator(method):
        def check(self, other):
            if not isinstance(other, int) and not isinstance(other, Number):
                raise TypeError(f'"{other}" is neither "int" nor "Number"')
            if other < 0:
                raise ValueError('other has to be >= 0')
            return method(self, other)
        return check

    def _symbols_decorator(method):
        def check(self):
            if len(self.symbols) < self._base:
                raise ValueError('base cannot be represented; expand "symbols"\
 list or use "repr_list"')
            return method(self)
        return check

    def _equalising_func(self, other):
        temp = self._copy()
        other = Number(other, temp._base)
        while len(temp._numlist) < len(other._numlist):
            temp._numlist.append(0)
        while len(temp._numlist) > len(other._numlist):
            other._numlist.append(0)
        return temp, other

    def _copy(self):
        return Number(self, self._base)

    @_symbols_decorator
    def __repr__(self):
        return (''.join([Number.symbols[self._numlist[w]]
                         for w in range(len(self._numlist)-1, -1, -1)])
                + ' (' + str(self._base) + ')')

    @_symbols_decorator
    def __str__(self):
        return ''.join([Number.symbols[self._numlist[w]]
                        for w in range(len(self._numlist)-1, -1, -1)])

    def __int__(self):
        temp = self._numlist.copy()
        for w in range(len(temp)-1, 0, -1):
            temp[w-1] += temp[w] * self._base
        return temp[0]

    @_checking_decorator
    def __add__(self, other):
        temp = self._copy()
        temp._numlist[0] += int(other)
        w = 0
        while temp._numlist[w]//temp._base != 0:
            if w+1 == len(temp._numlist):
                temp._numlist.append(0)
            temp._numlist[w+1] += temp._numlist[w]//self._base
            temp._numlist[w] %= temp._base
            w += 1
        return temp

    @_checking_decorator
    def __sub__(self, other):
        if self < other:
            raise ValueError(f'{other} is greater than {self}')
        temp, other = self._equalising_func(other)
        for w in range(len(other._numlist)):
            temp._numlist[w] -= other._numlist[w]
            if temp._numlist[w] < 0:
                temp._numlist[w] += temp._base
                temp._numlist[w+1] -= 1
        try:
            while temp._numlist[-1] == 0:
                del temp._numlist[-1]
        except IndexError:
            return Number(0, temp._base)
        return temp

    @_checking_decorator
    def __mul__(self, other):
        temp, other = self._equalising_func(other)
        multiplied = []
        formated = Number(0, temp._base)
        for w in range(len(other._numlist)):
            current = []
            rest = 0
            for i in range(w):
                current.append(0)
            for i in temp._numlist:
                current.append((other._numlist[w]*i + rest)%temp._base)
                rest = (other._numlist[w]*i + rest)//temp._base
            current.append(rest)
            formated._numlist = current
            multiplied.append(formated._copy())
        added = Number(0, temp._base)
        for w in multiplied:
            added += w
        return added

    @_checking_decorator
    def __pow__(self, other):
        temp = int(self._copy())
        other = int(other)
        return Number(temp**other, self._base)

    def _division(self, other):
        if other == 0:
            raise ZeroDivisionError('other cannot be == 0')
        temp, other = int(self), int(other)
        div = Number(temp//other, self._base)
        mod = Number(temp%other, self._base)
        return div, mod

    @_checking_decorator
    def __floordiv__(self, other):
        return self._division(other)[0]

    @_checking_decorator
    def __mod__(self, other):
        return self._division(other)[1]

    @_checking_decorator
    def __lt__(self, other):
        temp, other = self._equalising_func(other)
        for w in range(len(temp._numlist)-1, -1, -1):
            if temp._numlist[w] < other._numlist[w]:
                return True
            elif temp._numlist[w] > other._numlist[w]:
                return False
        else:
            return False

    def __le__(self, other):
        return self < other or self == other

    @_checking_decorator
    def __eq__(self, other):
        temp, other = self._equalising_func(other)
        for w in range(len(temp._numlist)):
            if temp._numlist[w] != other._numlist[w]:
                return False
        else:
            return True

    def int_base(self):
        '''return the base of the Number'''
        return self._base

    def repr_list(self):
        '''return list with integers representing the Number'''
        temp = self._numlist.copy()
        temp.reverse()
        return temp



roman_numerals = Pair([(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'),
                       (10, 'X'), (5, 'V'), (1, 'I')])

def roman(integer, symbol_list = roman_numerals):
    if len(symbol_list)%2 != 1:
        raise ValueError('symbol_list len has to be uneven')
    if integer <= 0:
        raise ValueError('integer has to be <= 0')
    symbol_list = symbol_list.copy()
    symbol_list.swapTypes(int, 'left')
    symbol_list.sort()
    symbol_list.reverse()
    symbols = symbol_list.rright()
    translation = symbol_list.rleft()
    rounds, outcome = [], ''
    for w in translation:
        rounds.append(integer//w)
        integer %= w
    outcome += rounds[0] * symbols[0]
    for w in range(1, len(symbols)-1):
        if rounds[w+1] == 4:
            if rounds[w] >= 1:
                outcome += symbols[w+1] + symbols[w-1]
            else:
                outcome += symbols[w+1] + symbols[w]
            rounds[w+1] = 0
        else:
            outcome += symbols[w] * rounds[w]
    outcome += symbols[-1] * rounds[-1]
    return outcome

def roman_to_int(roman, symbol_list = roman_numerals):
    if len(symbol_list)%2 != 1:
        raise ValueError('symbol_list len has to be uneven')
    outcome, roman = 0, list(roman)
    symbol_list = symbol_list.copy()
    symbol_list.append([0, 0])
    for w in range(len(roman)-1):
        if roman[w] == 0:
            continue
        current = symbol_list.read(roman[w])[0]
        nex = symbol_list.read(roman[w+1])[0]
        if nex > current:
            outcome += nex - current
            roman[w+1] = 0
        else:
            outcome += current
        roman[w] = 0
    outcome += symbol_list.read(roman[-1])[0]
    return outcome



def _def_comparator(lower, greater):
    return lower <= greater

def merge_sort(lis, method = _def_comparator):
    if not isinstance(lis, list):
        raise TypeError(f'"lis" has to be type "list" not {type(lis)}')
    if len(lis) in [0, 1]:
        return lis
    p1, p2 = lis[:len(lis)//2], lis[len(lis)//2:]
    p1 = merge_sort(p1)
    p2 = merge_sort(p2)
    i1, i2, current = 0, 0, []
    while i1 != len(p1) and i2 != len(p2):
        if method(p1[i1], p2[i2]):
            current.append(p1[i1])
            i1 += 1
        else:
            current.append(p2[i2])
            i2 += 1
    current += p1[i1:]
    current += p2[i2:]
    return current



def _neoninstance(obj, typ: str):
    '''checks whether an object is typ (debug tool)'''

    def isPair(obj):
        if isinstance(obj, list):
            for w in obj:
                if not isinstance(w, tuple) or len(w) != 2:
                    break
            else:
                return True
        return False

    def isNumber(obj):
        for w in obj:
            if not isinstance(w, int):
                return False
        else:
            return True

    def isRoman(obj):
        return obj == roman(roman_to_int(obj))

    instances = {'Pair': isPair,
                 'Number': isNumber,
                 'Roman': isRoman}

    try:
        return instances[typ](obj)
    except KeyError:
        raise ValueError(f'object \'{typ}\' does not belong to neonCollection')
