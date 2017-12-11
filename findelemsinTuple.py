#Lets say we have a string
my_message = "Hello There, We are Anonymous"
print('a' in my_message) #True
print('b' in my_message) #False
print('a ' in my_message) #False

#Can we search for same in a list of integers or floats?
my_numbers = [1,2,3,4,5, 7.5,10.5,13.5]
print(4 in my_numbers) #True
print('4' in my_numbers) #False
print('a' in my_numbers) #False

#Can we do the same for a tuple?

my_tuple = tuple(my_numbers)
print(1 in my_tuple ) #True
print(1 not in my_tuple) #False

#Lets see a use case for tuples and lists
userNames = ["Amit", "Adi", "Archi", "Parshya", "Langdya"]
for eachname in userNames:
    print("Hello, " + eachname)

#We can do the same for tuples
userNameTuple = tuple(userNames)
for eachname in userNameTuple:
    print('Namaskar '+ eachname) 
