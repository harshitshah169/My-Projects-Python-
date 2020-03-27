import random
number = random.randrange(1,100)
print("Welcome to the Guessing Game!!")
guess = "wrong"
count = 0;

try:
    response = int(input("Enter an Integer between 0 to 100: "))

    while guess=="wrong":
                if response>number:
                    print("You have choosed a greater number...")
                    response = int(input("Enter a number between 0 to 100: "))
                    count+=1
                elif response<number:
                    print("You have choosed a smaller number...")
                    response = int(input("Enter a number between 0 to 100: "))
                    count += 1
                elif response == number:
                    count += 1
                    print("\nYou have guessed the correct number in " + str(count) + " Attempts")
                    guess="right"

    print("Congratulations, You Won!!!")
except ValueError:
    print("Invalid choice, You Lost")
