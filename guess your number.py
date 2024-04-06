

from random import randint




def guess(user_guess, correct_num):
    # If the user guesses wrong, tell them if their
    # guess is too low or too high, then return False.
    # Fix the XXXXX's in the template below to get it to work correctly
    if user_guess < correct_num:
        print("this number is too low!")
        return False
        # TODO: Print the output and return False
    elif user_guess > correct_num:
        print()
        # TODO: Print the output and return False
        return False
    else:
        print("congratulations this is the correct number")
        return True
        # TODO: If the user guesses correctly, congratulate them
        # and return True

if __name__ == "__main__":
    num = randint(-50, 50)
    while True:
        user_guess = int(input("Enter your guess: "))
        if guess(user_guess, num) == True:
            break