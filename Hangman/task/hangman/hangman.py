# Write your code here
import random

word_bank = ["python", "java", "kotlin", 'javascript']
computer = random.choice(word_bank)
blank = "-" * len(computer)
check = set(computer)
new_game = list(blank)
temp = list(computer)
listToStr = "".join([str(elem) for elem in new_game])
count = 0
letter = []

print("H A N G M A N\n")
while count < 8:
    print()
    print(listToStr)
    guess = input("Input a letter: ")
    letter.append(guess)
    if len(guess) > 1 or guess == "":
        print("You should input a single letter")
    if len(guess) == 1:
        if not 97 <= ord(guess) <= 122:
            print("It is not an ASCII lowercase letter")
        if letter.count(guess) >= 2:
            print("You already typed this letter")
    if guess not in check:
        print("No such letter in the word")
        count += 1
    elif guess in check:
        for index in range(len(temp)):
            if temp[index] == guess:
                new_game[index] = guess
            listToStr = "".join([str(elem) for elem in new_game])
    if new_game == temp:
        break
if temp == new_game:
    print("You guessed the word!")
    print("You survived!")
elif temp != new_game:
    print("You are hanged!")
