tuplex = ("Tuplex",False,3.2,1)
print(tuplex)

tuplex2 = (4,8,6,3,2,5)
print(tuplex2)

tuplex = tuplex2 + (9,)
print(tuplex)

tuple1 = (3,6,9,12,15,3,9,0,1)
print(tuple1.count(3))

tuple2 = (2,5,6,7,8,9,0,1,3,4)
_slice = tuple2[3:5]
print(_slice)
_slice = tuple2[:6]
print(_slice)