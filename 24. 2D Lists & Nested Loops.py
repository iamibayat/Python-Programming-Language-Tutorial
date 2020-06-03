# nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

# OR

nested_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(nested_lists)
print('\n')


for rows in nested_lists:
    print(rows)
print('\n')


for rows in nested_lists:
    for each_value in rows:
        print(each_value)
print('\n')

