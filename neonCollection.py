'''a collection of custom objects used to store/manipulate/read data'''

class Pair:
    '''Pair(x: 'list, tuple, set or dict') -> [(a, b), (c, d)]
       Dict-like object without distinction between keys and values.

       'Pair' is an object the value of which is stored as self._PAIR
       and it takes the form of a list with only tuples inside, which
       contain exactly 2 values.'''

    def __init__(self, val = None):
        if val == None:
            self._PAIR = []
        else:
            self._PAIR = Pair._fromX(val)

    def __repr__(self):
        return f'Pair{self._PAIR}'

    def __add__(self, other):
        '''fuses Pairs together'''
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

    # transformation methods
    def _fromX(val):
        '''turns a list, tuple or dict into 'PAIR\''''
        par = []
        if isinstance(val, dict):
            for key, arg in val.items():
                par.append((key, arg),)
        else:
            for pair in val:
                if isiterable(pair) and len(pair) == 2:
                    par.append(tuple(pair))
        return par

    def toDict(self, side: 'key: \'left\' or \'right\'' = 'left'):
        '''turns 'PAIR' into dict. determine 'side' to specify
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
        '''turn 'pair' into list'''
        lis = []
        for w in self._PAIR:
            lis.append(list(w))
        return lis

    def copy(self):
        '''returns a shallow copy of the Pair'''
        return Pair(self._PAIR)

    # appending/deleting methods
    def append(self, pair):
        '''append a pair of values to 'PAIR\''''
        if len(pair) == 2 and not isinstance(pair, dict):
            self._PAIR.append(tuple(pair))
        elif len(pair) == 1 and isinstance(pair, dict):
            for key, val in pair.items():
                temp = (key, val)
            self._PAIR.append(temp,)
        else:
            raise ValueError('length of a pair has to be exactly 2')

    def insert(self, pair, place):
        '''insert a pair of values to 'PAIR\''''
        if len(pair) == 2 and not isinstance(pair, dict):
            self._PAIR.insert(place, tuple(pair))
        elif len(pair) == 1 and isinstance(pair, dict):
            for key, val in pair.items():
                temp = (key, val)
            self._PAIR.insert(place, temp)
        else:
            raise ValueError('length of a pair has to be exactly 2')

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
        if len(temp) != 0:
            for w in temp:
                del self._PAIR[self._PAIR.index(w)]
        else:
            raise ValueError(f'{val} is not in Pair')

    def removeByWhole(self, val):
        '''removes pairs equal to val'''
        temp = self.indexByWhole(val)
        if len(temp) != 0:
            for w in temp:
                del self._PAIR[self._PAIR.index(val)]
        else:
            raise ValueError(f'{val} is not in Pair')

    # internal order methods
    def swap(self, index):
        '''swaps left and right element in 'PAIR\''''
        temp = list(self._PAIR[index])
        temp[0], temp[1] = temp[1], temp[0]
        self._PAIR[index] = tuple(temp)

    def swapAll(self):
        '''swaps left and right element in all pairs in 'PAIR\''''
        for w in range(len(self._PAIR)):
            self.swap(w)

    def swapTypes(self, obj: 'object', side = 'left'):
        '''formats 'PAIR' to contain elements of the same type on one side'''
        if side != 'left' and side != 'right':
            raise ValueError(f'invalid side: {side}')
        if side == 'right':
            s = True
        else:
            s = False
        for w in self._PAIR:
            if isinstance(w[not s], obj) and not isinstance(w[s], obj):
                self.swap(self._PAIR.index(w))

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
        if not _neoninstance(self._PAIR, 'Pair'):
            try:
                if not isinstance(self._PAIR, dict):
                    new = []
                    for w in self._PAIR:
                        if isinstance(w, tuple) and len(w) == 2:
                            new.append(w)
                        elif isiterable(w) and len(w) == 2:
                            new.append(tuple(w))
                elif isinstance(self._PAIR, dict):
                    new = Pair._fromX(self._PAIR)
                return new
            except TypeError:
                return []
        else:
            return False

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
        '''returns the corresponding values from 'PAIR\''''
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



def _neoninstance(obj, typ: str):
    '''checks whether an object is typ'''

    def isPair(obj):
        if isinstance(obj, list):
            for w in obj:
                if not isinstance(w, tuple) or len(w) != 2:
                    break
            else:
                return True
        return False

    instances = {'Pair': isPair}

    try:
        if instances[typ](obj):
            return True
        else:
            return False
    except KeyError:
        raise ValueError(f'object \'{typ}\' does not belong to neonCollection')

def isiterable(obj):
    '''returns True if obj is iterable'''
    try:
        for w in obj:
            break
    except TypeError:
        return False
    else:
        return True
