# 1. Write a Python script that initializes two variables
# multiplies the result, store the result in a third variable,
# and prints the result
x = 2
y = 3
result = x + y
print(result)
assert(result == 5)

# Assert is a function that checks 
# if that a condition is true
# if false, it produces an error and halts the program execution
# It is widely used in production software when you need to 
# verify that a value has an exact value, or isn't empty or null
# that might be required for subsequent calculations

# 2. (3 + 2) * 5 = ?
assert((3 + 2) * 5 == 25)

# 3. 3-6 * 2 = ?
assert((3-6 * 2) == -9)

# 4. (10/5) - (2+6) = ?
assert((10/5) - (2+6) == -6)

# 5. 2*2/2+2-2 = ?
assert((2*2/2+2-2) == 2)

# 6. (20 * 5) - ((3 + 2) * 2) * 5 = ?
x = (20 * 5) - ((3 + 2) * 2) * 5
assert(x == 50)

# 7. Write a function with param x
# print if it is zero, negative or positive
def sign(x):
    if x < 0:
        print("x is negative!")
    elif x > 0:
        print("x is positive!")
    else:
        print("x is zero!")

sign(-3)
sign(100)
sign(0)

# 8. Write a script that subtracts 1 from the string '2021'
# return the result as a string
def subtract_str(s, n):
    return str(int(s) - n)

print(subtract_str('2021', 1))
print(subtract_str('0', 10))
print(subtract_str('-35002', -35002))

# 9. Write a script that has a variable num_files = 33256
# Print a message like this: 'User has 33256 total files on disk'

def print_num_files(n):
    print('User has ' + str(n) + " total files on disk")

# assume we obtained the number of total files on disk
# and stored it in this variable
total_num_files = 33256
print_num_files(total_num_files)

# 10. Print 'Hello, Hunter' 50 times. 
# Allow the program to print out different user names

def greet_user(name, n):
    for x in range(n):
        print("Hello, " + name + "! I've greeted you " + str(x+1) + " times!")

greet_user("Hunter", 50)
greet_user("Sarah", 10)
greet_user("Barnaby", 2)