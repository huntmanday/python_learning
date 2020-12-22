# 8. Write a script that subtracts 1 from the string '2021'
# return the result as a string
def subtract_str(s, n):
    return str(int(s) - n)

print(subtract_str('2021', 1))
print(subtract_str('0', 10))
print(subtract_str('-35002', -35002))