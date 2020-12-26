'''a collection of custom objects used to store/manipulate/read data'''

class Pair:
    '''Pair(x: 'list, tuple, set or dict') -> [(a, b), (c, d)]
       Dict-like object without distinction between keys and values.

       'Pair' is an object the value of which is stored as self.PAIR
       and it takes the form of a list with only tuples inside, which
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
                if isiterable(pair) and len(pair) == 2:
                    par.append(tuple(pair))
        return par

    def toDict(self, side: 'key: \'left\' or \'right\'' = 'left'):
        '''turns 'PAIR' into dict. determine 'side' to specify
           which side should be key'''
        if side != 'left' and side != 'right':
            raise ValueError(f'invalid side: {side}')
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
                del self.PAIR[self.PAIR.index(w)]
        else:
            raise ValueError(f'{val} is not in Pair')

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
        if side != 'left' and side != 'right':
            raise ValueError(f'invalid side: {side}')
        if side == 'right':
            s = True
        else:
            s = False
        for w in self.PAIR:
            if isinstance(w[not s], obj) and not isinstance(w[s], obj):
                self.swap(self.PAIR.index(w))

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
        temp = self.PAIR.copy()
        flag = True
        while flag:
            flag = False
            for w in range(1, len(temp)):
                if temp[w - 1][s] > temp[w][s]:
                    temp[w - 1], temp[w] = temp[w], temp[w - 1]
                    flag = True
        self.PAIR = temp
        if both == True:
            self.sort(side)

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
        typ = type(self.PAIR[0][s])
        ptyp = True
        typ2 = type(self.PAIR[0][not s])
        if side is None:
            ptyp2 = True
        else:
            ptyp2 = False
        for w in self.PAIR:
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
