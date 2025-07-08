'''
Ask for two numbers and print:

Sum

Difference

Product

Quotient

'''

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

print("The sum of the two number is : ", a + b)

if a>b: 
    diff = a-b
else:
    diff = b-a
print("The differnce of the two number is : ",diff )

print("The multiplication of the two number is : ", a*b)

if a>b:
    q = a/b; 
     
else:
    q = b/a


print("The Quotient of the two number is : ", q)
