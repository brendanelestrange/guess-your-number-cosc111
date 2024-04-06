#code written by brendan lestrange
#no external help received :)


from random import randint
def guess(user_guess, correct_num):
    # If the user guesses wrong, tell them if their
    # guess is too low or too high, then return False.
    # Fix the XXXXX's in the template below to get it to work correctly
    if user_guess < correct_num: #compares the numbers
        print("this number is too low!")
        return False #scenerio is false
        # TODO: Print the output and return False
    elif user_guess > correct_num: #compares the numbers
        print("this number is too high, guess again!")
        # TODO: Print the output and return False
        return False #examines this scenerio to be false
    else: #sees that neither of the above conditions are met
        print("congratulations this is the correct number.\n you have broken the cycle.")
        return True #this statement is true.
        # TODO: If the user guesses correctly, congratulate them
        # and return True

if __name__ == "__main__":
    num = randint(-50, 50)
    while True:
        user_guess = int(input("Enter your guess: "))
        if guess(user_guess, num) == True:
            break