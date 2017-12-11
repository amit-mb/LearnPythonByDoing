#!usr/bin/python
#create a tuple containing elems of same type

my_tuple = (1,2,3)
print(my_tuple)

#create a tuple with elems of different types
another_tuple = ("Amit", 22, 5.6)
print(another_tuple)

#To access the induvizual elements of a tuple, we use the index

print("The first element of the tuple is " + another_tuple[0])

#Similarly we can use looping as well
'''
for i in range(0,len(another_tuple)):
    print("The " + str(i)+ "element of the tuple is " + str(another_tuple[i])
    '''

#create a tuple with a primitive type, a sub-list and sub-tuple

mixed_tuple = ("Hi bro!", [5,10,15], ("Morning", "Noon", "Evening", "Night"))
print(mixed_tuple)

#WE can access the elems in a similar way
print(mixed_tuple[0]);#Hi bro!
print(mixed_tuple[1]) #[5,10,15]
print(mixed_tuple[2]) #("Morning" ... )
#print(mixed_tuple[5]) #error

#LETS have some fun!
print("FUN!")
for i in range(0,len(mixed_tuple[0])) :
    print(mixed_tuple[0][i])

#MORE FUN??
print("MORE FUN!!")
for k in range(0, len(mixed_tuple)) :
    for m in range (0, len(mixed_tuple[k])):
        print(mixed_tuple[k][m])

#What happens when you assign a  set of values to a variable without round or square brackets

some_list = 1,2, "Good Eve", 5.3 #THis is called tuple packing, because we pack a set into a tuple
print(some_list)         # (1,2, "Good Eve",5.3) !! If no round brackets are given, it considers the list as a tuple

#Lets try something, Shall we?
a,b,c,d = some_list; #This is called tuple unpacking, because we unpack a tuple into seperate variables/containers of their own
print(a) #1
print(b)#2
print(c)#Good Eve
print(d) #5.3

#Technically the following code could also be called tuple packing, and it is!
otherTuple = (a,b,c,d)
print(otherTuple) #(1,2,"Good Eve", 5.3)

#type(function)
#Lets determine the type of tuples
intTuple = (1)
print(type(intTuple)) # return <class 'int'>

inttwoTuple = (1,2)
print(type(inttwoTuple)) #<<class 'tuple'>

#Lets try a mixed tuple
print(type(mixed_tuple)) # This is also of type 'tuple' !

#So we can conclude that a tuple with a single value is considered to be of its own type(int or float or str).
#A tuple is when you have multiple values stored in it, until then, its like any other variable
#Lets try some weird case
weirdTuple =(5,) #A tuple with single value and a siffixed comma
print(type(weirdTuple)) #!!! Its still a tuple, why? Because a comma signifies that there could be more than one value

#Lets now try something erratic
#If we try to access a index of a tuple thats exceeds the already defined one, Do we get an error or the value '0'?
heyTuple = (0,3,6,9) #multiples of 3 which have a single digit
#print(heyTuple[6])
#so we conclude that accessing indexes that are not yet defined ends up giving an error.
#You could think of heyTuple's memory allocation as [0,3,6,9, empty, empty, ... ]
#What about This
#print(heyTuple[1.0]) #error
#tuples are indexed only in integers and nothing else, indices must be integers

#Can we use negative indexes then?
print(heyTuple[-1])
print("Reversed tuple is :" )
#We could also reverse the whole tuple with a looping
reversedTuple = (0,0,0,0)
for i in range(0,len(heyTuple)):
    print(heyTuple[-i-1])
    #reversedTuple[i] = heyTuple[-i-1] #why -i-1?? Think for urself
    #The above line doesn't work. Why? THink of a workaround

#What can we conclude from this?
#We can say that indexes for a tuple are pointed in such as way as (.....[-3 poinitng to +2],[-2 pointing to +1],[-1 pointing to 0]|[0],[1],[2],....)

#lets learn slicing which is very similar to slicing an array in JS
fooTuple = ("A","m","i","t",1,9,9,7, 5.7)
#in JS we used to use the .slice method which was a method defined for array objects and array like objects as well
print(fooTuple[2:]) #similar to fooTuple.slice(2). returns (all elements expect the first two)
print(fooTuple[4:])#similar to fooTuple(4). Removes the first 4 elements from the tuple. returns (1,9,9,7,5.7)
print(fooTuple[2:6]) #fooTuple.slice(2,6). returns ("i", "t",1,9,9)

#lets try from the right side of [:]

print(fooTuple[:1]) #returned ('A'). slices all elements except the first
print(fooTuple[:2])

#Lets try to remove the tuple from the end. Emulate .pop() behaviour
print(fooTuple[:-1])
#pop() with multiple elements i.e remove last n elements
print(fooTuple[:-5]) # removes the last 5 elements
