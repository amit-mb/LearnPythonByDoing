#An important thing to note is that the return type of input() is always a string
#Therefore you will get erranous results if you do something like this

A_number = input('Enter a number ')
B_number = input('Enter another number')
sum = A_number + B_number
#product = A_number * B_number;

print("The sum of two numbers is "  + sum )

#However, you can implicitly do type conversion to achieve the expected results

A_number = float(A_number)
B_number = float(B_number)
sum = A_number + B_number
print("The sum of two numbers is "  + str(sum) )
