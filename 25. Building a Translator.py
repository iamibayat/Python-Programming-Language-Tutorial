'''vowels = ['a', 'e', 'i', 'o', 'u']
emp_list = []


def translator(word):
    for i in word:
        flag = True
        for j in vowels:
            if i == j:
                emp_list.append('g')
                flag = False
                break
        if flag:
            emp_list.append(i)


word = input("Enter word to translate: ")
translator(word)

print(emp_list)

string = ''
length = len(emp_list)
for k in range(length):
    string = string + emp_list[k]

print(string)'''



def translator(words):
    translation = ''
    for letter in words:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation


print(translator(input('Enter a phrase: ')))
