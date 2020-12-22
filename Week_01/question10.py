# 10. Print 'Hello, Hunter' 50 times. 
# Allow the program to print out different user names

def greet_user(name, n):
    for x in range(n):
        print("Hello, " + name + "! I've greeted you " + str(x+1) + " times!")

greet_user("Hunter", 50)
greet_user("Sarah", 10)
greet_user("Barnaby", 2)