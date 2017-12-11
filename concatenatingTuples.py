#Hack to declare empty lists with a pre-defined size
twoTables = [None] * 4
threeTables = [None] * 4

for i in range(0,4):
    twoTables[i] = 2 * i;
    threeTables[i] = 3*i;

print(twoTables)
print(threeTables)

#Now lets concatenate the two lists
twothreeTables = twoTables + threeTables;
print(twothreeTables)

#Now, lets do the same for lists
# tenTableTuple = [None] * 5
# eleventableTuple = [None] * 5
#converting list into a tuple
# tenTableTuple = tuple(tenTableTuple)
# eleventableTuple = tuple(eleventableTuple)

# for i in range(0,5):
#     tenTableTuple[i] = 10 * i;
#     eleventableTuple[i] = 11 * i;

#Cant do this because python doesnt support tuple item assignment

#So lets do it other way
twoTableTuple = tuple(twoTables) #convert a list onto tuple
threeTableTuple = tuple(threeTables)

#concatenation of tuples
twothreeTableTuple = twoTableTuple + threeTableTuple
print(twothreeTableTuple)
