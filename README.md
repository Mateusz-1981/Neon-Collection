# Neon-Collection
A collection of a few objects I felt were missing

## Pair
"Pair(x: 'list, tuple, set or dict') -> [(a, b), (c, d)].
Dict-like object without distinction between keys and values.  
'Pair' is an object the value of which is stored as self.PAIR and it takes the form of a list with
only tuples inside, which contain exactly 2 values.

initiation example:
> \>\>\> x = Pair({12: 'a', 13: 'b', 'c': 14})  
\>\>\> x = Pair([[12, 'a'], [13, 'b'], ['c', 14]])  
\>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), ('c', 14)]  

#### append(pair)  
Appends 1 pair. Takes in list, tuple, set or dict.  
example:  
> \>\>\> x.append(['d', 15])  
\>\>\> x.append({16: 'e'})  
\>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  

#### index(value)
Returns a list of indexes of pairs containing a given value.  
example:  
> \>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  
\>\>\> x.index('e')  
[4]  

#### read(value); readAll(value)  
Read returns a list of corresponding values to the given ones; readAll returns the entire pairs which
contain the given value.  
example:  
> \>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  
\>\>\> x.read(13)
['b']
\>\>\> x.readAll(13)
[(13, 'b')]

#### remove(value)
Removes all pairs which contain a given value.  
example:
> \>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  
\>\>\> x.remove(12)  
\>\>\> x.PAIR  
[(13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  

#### pop(value); popAll(value)
Pop returns a list of corresponding values to the given ones and removes them; popAll returns the entire pairs which
contain the given value and removes them.  
> \>\>\> x.PAIR  
[(13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  
\>\>\> x.pop(13)  
['b']  
\>\>\> x.popAll(14)  
[('c', 14)]  
\>\>\> x.PAIR  
[('d', 15), (16, 'e')]  

#### rleft(); rright()
Return a list of all left/right values.  
example:  
> \>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  
\>\>\> x.rleft()  
[12, 13, 'c', 'd', 16]  
\>\>\> x.rright()  
['a', 'b', 14, 15, 'e']  

#### swap(index); swapAll()
'swap' swaps left and right element in a specified pair. 
'swapAll' swaps right and left element in all pairs.
example:  
> \>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), ('c', 14), ('d', 15), (16, 'e')]  
\>\>\> x.swap(0)  
\>\>\> x.swap(1)  
\>\>\> x.PAIR  
[('a', 12), ('b', 13), ('c', 14), ('d', 15), (16, 'e')]  
\>\>\> x.swapAll()  
\>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), (14, 'c'), (15, 'd'), ('e', 16)]  

#### swapTypes(object type, side)
Swaps elements in some pairs so that the specified type of an object is on the chosen side.  
example:  
> \>\>\> x.PAIR  
[('a', 12), ('b', 13), (14, 'c'), (15, 'd'), ('e', 16)]  
\>\>\> x.swapTypes(int, 'left')  
\>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), (14, 'c'), (15, 'd'), (16, 'e')]  

If the action cannot be done (for example if a pair does not contain the specified type) nothing is changed  
in that pair.

#### isSameType(side)
Returns True if all the elements on the specified side are of the same type.  
If no side is chosen, the function will return True if there is at least one element in every pair that is of the
same type.  
example:  
> \>\>\> x.PAIR  
[(12, 'a'), (13, 'b'), (14, 'c'), (15, 'd'), ('e', 16)]  
\>\>\> x.isSameType('left')  
False  
\>\>\> x.swapTypes(int, 'left')  
\>\>\> x.isSameType('left')  
True  
\>\>\> x.PAIR = [(12, 'a'), (13, 'b'), (14, 'c'), (15, 'd'), ('e', 'd'), (12, 3)]  
\>\>\> x.isSameType() # will return False as there is a pair that does not contain int and a pair that does not
contain str  
False  

#### sort(side, both)
Sorts pairs by the order of elements on the specified side. If both == True then the function will sort both sides
with priority set for the specified side.  
example:  
> \>\>\> x = Pair([(8, 'b'), (8, 'a'), (2, 'b'), (2, 'c'), (0, 'e'), (0, 'a')])  
\>\>\> x.sort('left')  
\>\>\> x.PAIR  
[(0, 'e'), (0, 'a'), (2, 'b'), (2, 'c'), (8, 'b'), (8, 'a')]  
\>\>\> x = Pair([(8, 'b'), (8, 'a'), (2, 'b'), (2, 'c'), (0, 'e'), (0, 'a')])  
\>\>\> x.sort('left', True)  
\>\>\> x.PAIR  
[(0, 'a'), (0, 'e'), (2, 'b'), (2, 'c'), (8, 'a'), (8, 'b')]  

#### repair()
If self.PAIR does not comply with 'Pair' definition returns a repaired version of self.PAIR. Else returns False.  
example:  
> \>\>\> x.PAIR  
(('d', 15), (16, 'e'), [12, 3], [4])  
\>\>\> x.repair()  
[('d', 15), (16, 'e'), (12, 3)]  
\>\>\> x.PAIR = x.repair()

#### toDict(side)
Turns Pair into Dict. Choose side to specify which side should become key.  
example:  
> \>\>\> x.PAIR  
[('d', 15), (16, 'e'), (12, 3)]  
\>\>\> x.toDict('left')  
{'d': 15, 16: 'e', 12: 3}  
\>\>\> x.toDict('right')  
{15: 'd', 'e': 16, 3: 12}  

#### toList()
Turns Pair into List.  
example:  
> \>\>\> x.PAIR  
[('d', 15), (16, 'e'), (12, 3)]  
\>\>\> x.toList()  
[['d', 15], [16, 'e'], [12, 3]]  


## neoninstance(object, type)
Equivallent to 'isintsance' but works for objects present in this module. (for now it only works with 'Pair')
Returns True if the given object is of the given type.  
example:  
> \>\>\> neoninstance(x.PAIR, 'Pair')  
True  
\>\>\> neoninstance([12, 4], 'Pair')  
False  

## isiterable(object)
Returns True if object is iterable.  
example:  
> \>\>\> isiterable(12)  
False  
\>\>\> isiterable([12])  
True  
