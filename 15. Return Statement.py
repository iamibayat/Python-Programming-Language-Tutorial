def cube(num):
    num*num*num             # without return statement

cube(3)                     # this will print nothing as nothing was returned



def cube1(num):
    return num*num*num
    print("hey,there")      # nothing written after return statement will be printed out

print (cube1(4))