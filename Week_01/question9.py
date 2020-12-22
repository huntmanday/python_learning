# 9. Write a script that has a variable num_files = 33256
# Print a message like this: 'User has 33256 total files on disk'

def print_num_files(n):
    print('User has ' + str(n) + " total files on disk")

# assume we obtained the number of total files on disk
# and stored it in this variable
total_num_files = 33256
print_num_files(total_num_files)