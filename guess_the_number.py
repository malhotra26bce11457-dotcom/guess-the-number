import random 
#pick a correct_number between 1 to 100
number = random.randint(1,100)

#keep track of how many guesses the player has made
attempts = 0

#set the maximum limit for the c number of guesses
max_attempts = 10 

print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100.")
print("You have 10 attempts to guess the number.")

#keep asking the player to guess the number untile they guess the number correctly 
while attempts < max_attempts:
    #ask the player to guess their number
    guess = int(input("Enter your number which you think is the correct number:"))
#count the number of attempts made by the player to guess the number
    attempts  +=1
#give feedback to the player on the baseses of their guess
    if guess < number:
       print("Your guess is smaller than the correct number. Please try again.")
    elif guess > number:
        print("Your guess is bigger than the  correct number. Please try again.")
    else:
        print("woohoo! you guessed the number correctly.")
        print("It took you", attempts, "attempts to guess the number correctly.")
        break
#if the player has used all their attempts and still could not guess the number correctly, then reveal the correct number
if attempts == max_attempts:
    print("Sorry, you have used all your 10 attempts. Better luck next time!")
    print("The correct number was:",  number)
