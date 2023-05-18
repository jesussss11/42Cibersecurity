import random
random_num = random.randint(1, 99)
def menu():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 an 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    print()
def question():
    intentos = 0
    while True:
        try:
            print("What's your guess between 1 an 99?")
            x = input()
            if x == "exit":
                print("Goodbye")
                print(f"You tried {intentos} attempts.")
                print()
                exit()
            intentos = intentos + 1
            guess_number = int(x)
            if guess_number > random_num:
                print("Too high!")
            elif guess_number < random_num:
                print("Too low!")
            elif guess_number == 42 and random_num == 42:
                print(f"The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulations! You got it on your first try!")
                print()
                exit()
            elif guess_number == random_num and intentos == 1:
                print("Congratulations! You got it on your first try!")
                print()
                exit()
            elif guess_number == random_num:
                print("Congratulations, you've got it!")
                print(f"You won in {intentos} attempts.")
                print()
                exit()
            print(f"You tried {intentos} attempts.")
            print()
        except Exception:
            print(f"You tried {intentos} attempts.")
            pass
menu()
question()