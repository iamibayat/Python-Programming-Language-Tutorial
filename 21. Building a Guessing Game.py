'''
print("What is the capital of Bangladesh?")

answer = input("Enter: ")

if answer == "Dhaka":
    print("Dhaka is correct.")
else:
    while answer != "Dhaka":
        answer = input("Enter Again: ")
    print("Dhaka is correct.")
'''




'''
print("What is the capital of Bangladesh?")
secret_word = "Dhaka"
guess_word = ""                              # we create an empty variable

while guess_word != secret_word:
    guess_word = input("Enter guess_word: ")
    
print("You win!!")
'''



print("What is the capital of Bangladesh?")
secret_word = "Dhaka"
guess_word = ""

count = 0
count_limit = 3
times_up = False

while guess_word != secret_word and not (times_up):
    if count < count_limit:
        guess_word = input("Enter guess_word: ")
        count += 1
    else:
        times_up = True

if times_up:
    print("Your time's up. You lose!!")
else:
    print("You win!!")






'''
print("What is the capital of Bangladesh?")
secret_word = "Dhaka"
guess_word = ""

count = 0
count_limit = 3
times_up = False

while guess_word != secret_word:
    if count < count_limit:
        guess_word = input("Enter guess_word: ")
        count += 1
    else:
        times_up = True
        break                                       # we use break to get out of the loop

if times_up:
    print("Your time's up. You lose!!")
else:
    print("You win!!")

# OR

if times_up == False:
    print("You win!!")
else:
    print("Your time's up. You lose!!")
'''