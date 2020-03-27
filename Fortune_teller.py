import random
print("Welcome to the fortune telling game!!")
ques = ""
response = "y"
while response == "y":
    ques = input("You may ask a question\n")
    choice = random.randrange(1,5)
    if choice == 1:
        print("Yes")
    elif choice == 2:
        print("Yes, definitely")
    elif choice == 3:
        print("No")
    elif choice == 4:
        print("Maybe, i guess")
    response = input("\nWould you like to ask me another question? (y/n): ")

print("\nThank you, comeback if you have more questions!!")
