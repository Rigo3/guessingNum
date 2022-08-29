from random import *

name = input("Enter your name: ")
randomNum = randint(1,100)
attempt = 8
print(f"Hi {name},\nI chose a random number between 1 and 100, try to guess it... \nIn 8 attempts!\nGood luck!\n")



while attempt != 0 :
    attemptNum = int(input(f"attempt {attempt}: "))
    if attemptNum >0 and attemptNum <101:

        if attemptNum < randomNum :
            attempt -= 1
            print (f"Your number is lower than the one I chose, you have {attempt} attempts left")
        elif attemptNum > randomNum:
            attempt -=1
            print(f"Your number is greater than the one I chose, you have {attempt} attempts left")
        elif attemptNum == randomNum:
            attempt -=1
            print(f"Contratulations! you guess the number({randomNum}) correctly in your attempt number {8-attempt}.")
            break
    else:
        print(f"Sorry, you enter a number outsite the range of 1-100, try again with other number")

if attempt == 0:
    print(f"Sorry, you have no attempts left! the number was {randomNum}. You lost, I WON!")


