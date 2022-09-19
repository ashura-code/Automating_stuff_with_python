# short program Guess the number

import random

i = 0
num = random.randint(0, 30)

print("guess the number : ")

while True:
    guess = int(input())
    i = i + 1
    if guess == num:
        print("congragulations, you have guessed the correct number in ", i, " chances")
        break
    if guess < num:
        print("low")

    if guess > num:
        print("high")


