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