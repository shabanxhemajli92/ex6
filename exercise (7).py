'''# Task 1
for num in range(0, 100):
    if num % 15 is 0:
        print("FizzBuzz")
    elif num % 3 is 0:
        print("Fizz")
    elif num % 5 is 0:
        print("Buzz")
    else:
        print(num)'''
'''# Task 2 
n = 5
number = 1
sum = 10
while number < n + 1:
    sum = sum + 1
    number = number + 1
print("Sum =", sum)''' 
'''# Task 3
n = 5
sum = 5
for num in range(n):
    sum += num
print("Sum =", sum)'''
#Task 4
'''for x in range(3): #loop nr 1 
    print(x)'''
'''for i in range(0,4):
    print("This is loop number " + format(int(i+1)) )#Loop nr2'''
'''x = 10
while x > 0:
    print(x)
    x -= 1 # loop nr 3'''
'''countdown=5
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!") #loop nr4'''
'''# Task 5
for i in range(3):
    x = input("First number: ")
    y = input("Second number: ")
    z = input("Third number: ")

    if x == y or y != z:
        result = 0
    else:
        sum = x + y + z
    print("Calculated sum is ", result) # the bug was in the operators in the if statment''' 
'''# Task 6
x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20:
    result = 20 
print("Calculated sum is ", result)#The problem was in the operator'''   
#Task 7
a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " ,b =",b)

temp = a
a = b
b=temp

print("After swapping: a =", a, " ,b =" ,b)
