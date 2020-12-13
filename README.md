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

