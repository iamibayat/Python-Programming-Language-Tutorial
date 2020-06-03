my_lists = ["Html", "Css", "Javascript", "Python", "Php"]

print(my_lists)
print("\n")


print(my_lists[0])                  # this will print out index number 0 from the start
print(my_lists[2])                  # this will print out index number 2 from the start
print("\n")


print(my_lists[-1])                  # this will print out index number 0 from the back
print(my_lists[-3])                  # this will print out index number 2 from the back
print("\n")


print(my_lists[1:])                  # this will print out all the elements starting from index 1
print(my_lists[3:])                  # this will print out all the elements starting from index 3
print("\n")


print(my_lists[1:3])                # this will print out starting from index 1 upto the element before index 3
print("\n")


my_lists[2] = "Java"                # we can also change the value of any index number
print(my_lists)