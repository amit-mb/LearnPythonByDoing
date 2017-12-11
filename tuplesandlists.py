#Lets learn two functions tuple() and list()
#tuple() functions converts a list or a array or an array of string into a tuple. Lets see how

message = "Hello Friend"
print(tuple(message))

#list() function convers an array or a list of an array of string into a list. What is a list?
#List is equivalent of arrays in JS or C
print(list(message))

#can we do this?
print(list(tuple(message)))

#or this for that matter?
print(tuple(list(message)))

#Yes, we can do both. tuple() returns a tuple and list() returns a list or an array
