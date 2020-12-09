'''a collection of custom objects used to store/manipulate/read data'''

class Pair:
    '''Pair(x: 'list, tuple, set or dict') -> [(a, b), (c, d)]
       Dict-like object without distinction between keys and values.

       'Pair' is an object the value of which is stored as self.PAIR
       and it takes a form of a list with only tuples inside, which
       contain exactly 2 values.'''

    def __init__(self, val = None):
        if val == None:
            self.PAIR = []
        else:
            self.PAIR = Pair._fromX(val)

    # transformation methods
    def _fromX(val):
        '''turns a list, tuple or dict into 'PAIR\''''
        par = []
        if isinstance(val, dict):
            for key, arg in val.items():
                par.append((key, arg),)
        else:
            for pair in val:
                par.append(tuple(pair))
        return par

    def toDict(self, side: 'key: \'left\' or \'right\''):
        '''turns 'PAIR' into dict. determine 'side' to specify
           which side should be key'''
        assert side == 'left' or side == 'right'
        dic = {}
        for w in self.PAIR:
            if side == 'right':
                dic[w[1]] = w[0]
            else:
                dic[w[0]] = w[1]
        return dic

    def toList(self):
        '''turn 'pair' into list'''
        lis = []
        for w in self.PAIR:
            lis.append(list(w))
        return lis

    # appending/deleting methods
    def append(self, pair):
        '''append a pair of values to 'PAIR\''''
        if len(pair) == 2 and not isinstance(pair, dict):
            self.PAIR.append(tuple(pair))
        elif len(pair) == 1 and isinstance(pair, dict):
            for key, val in pair.items():
                temp = (key, val)
            self.PAIR.append(temp,)

    def pop(self, val):
        '''removes and returns corresponding values to 'val\''''
        temp = self.read(val)
        self.remove(val)
        return temp

    def popAll(self, val):
        '''removes and returns a pair with 'val' element'''
        temp = self.readAll(val)
        self.remove(val)
        return temp

    def remove(self, val):
        '''removes pairs with 'val' element'''
        temp = self.readAll(val)
        for w in temp:
            del self.PAIR[self.PAIR.index(w)]

    # internal order methods
    def swap(self, index):
        '''swaps left and right element in 'PAIR\''''
        temp = list(self.PAIR[index])
        temp[0], temp[1] = temp[1], temp[0]
        self.PAIR[index] = tuple(temp)

    def swapAll(self):
        '''swaps left and right element in all pairs in 'PAIR\''''
        for w in range(len(self.PAIR)):
            self.swap(w)

    def swapTypes(self, obj: 'object', side = 'left'):
        '''formats 'PAIR' to contain elements of the same type on one side'''
        assert side == 'left' or side == 'right'
        if side == 'right':
            self.swapAll()
        for w in self.PAIR:
            if isinstance(w[1], obj) and not isinstance(w[0], obj):
                self.swap(self.PAIR.index(w))
        if side == 'right':
            self.swapAll()

    def sort(self, side: 'choose side to sort by' = 'left'):
        '''sorts pairs by the order of the left elements'''
        assert side == 'left' or side == 'right'
        cop = self.PAIR.copy()
        if side == 'right':
            self.swapAll()
        temp = self.rleft()
        temp.sort()
        par = []
        try:
            for w in temp:
                x = (w, self.read(w)[0])
                del self.PAIR[self.PAIR.index(x)]
                par.append(x)
        except (ValueError, NameError, IndexError, KeyboardInterrupt):
            self.PAIR = cop
            raise ValueError
        self.PAIR = par
        if side == 'right':
            self.swapAll()

    def repair(self):
        '''if self.PAIR is broken returns a fixed version'''
        if not neoninstance(self.PAIR, 'Pair'):
            try:
                if not isinstance(self.PAIR, dict):
                    new = []
                    for w in self.PAIR:
                        if isinstance(w, tuple) and len(w) == 2:
                            new.append(w)
                        elif isiterable(w) and len(w) == 2:
                            new.append(tuple(w))
                elif isinstance(self.PAIR, dict):
                    new = Pair._fromX(self.PAIR)
                return new
            except TypeError:
                return []
        else:
            return False

    # reading methods
    def rleft(self):
        '''returns all the left values in list'''
        lis = []
        for w in self.PAIR:
            lis.append(w[0])
        return lis

    def rright(self):
        '''returns all the right values in list'''
        lis = []
        for w in self.PAIR:
            lis.append(w[1])
        return lis

    def read(self, val):
        '''returns the corresponding values from 'PAIR\''''
        lis = []
        for w in self.PAIR:
            if w[0] == val:
                lis.append(w[1])
            elif w[1] == val:
                lis.append(w[0])
        return lis

    def readAll(self, val):
        '''returns pairs with 'val' element'''
        lis = []
        for w in self.PAIR:
            if w[0] == val or w[1] == val:
                lis.append(w)
        return lis

    def index(self, val):
        '''returns index of pairs with 'val' element'''
        ind = []
        for w in self.PAIR:
            if w[0] == val or w[1] == val:
                ind.append(self.PAIR.index(w))
        if ind == []:
            raise IndexError
        else:
            return ind

    def isSameType(self, side = None):
        '''left/right: checks if in all values on that side are the
           same type; None: checks if all pairs have a common type'''
        assert side == 'left' or side == 'right' or side == None
        if side == 'right':
            s = True
        else:
            s = False
        typ = type(self.PAIR[0][s])
        for w in self.PAIR:
            if not isinstance(w[s], typ):
                if not isinstance(w[not s], typ) or side is not None:
                    return False
        else:
            return True



def neoninstance(obj, typ: str):
    '''checks whether an object is typ'''

    def isPair(obj):
        if isinstance(obj, list):
            for w in obj:
                if not isinstance(w, tuple) or len(w) != 2:
                    break
            else:
                return True
        return False

    if typ == 'Pair' and isPair(obj):
        return True
    else:
        return False

def isiterable(obj):
    '''returns True if obj is iterable'''
    try:
        for w in obj:
            pass
    except TypeError:
        return False
    else:
        return True
