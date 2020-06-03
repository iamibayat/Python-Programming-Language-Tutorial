# tuples are not like any lists, there value cant be changed once it is declared

my_coordinates = (0, 13)                            # for lists we use [] but for tuples we use ()
print(my_coordinates)

print(my_coordinates[1])

# my_coordinates[1] = 14                            # TypeError: 'tuple' object does not support item assignment
# print(my_coordinates)

my_coordinates2 = [(0, 13), (2, 45), (3, 8)]        # we can also put tuples inside the lists
print(my_coordinates2)

print(my_coordinates2[2])