ages = [15,20,38,54, 20, 1, 6]
ages.sort() #You cannot assign this to any other variable as we do in JS.
            # Thats simply because another variable that you define wont be of the type list. However there's a workaround
print(ages)

sorted_array = [None] * len(ages)
sorted_array = ages.sort();
print(sorted_array)   #Turns out, this doesn't work either

#Lets get introduced to sum() fn
sumOfAges = sum(ages)
print(sumOfAges)        
