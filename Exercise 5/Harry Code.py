import random


def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    return 1


comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if (score == 0):
    print("Its a draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")





# import random
#
# def check_winner(comp, user):
#     """
#     Function to determine the winner.
#     Returns:
#         0  -> Draw
#         1  -> User Wins
#         -1 -> Computer Wins
#     """
#     if comp == user:
#         return 0
#
#     # Snake (0) beats Water (1)
#     # Water (1) beats Gun (2)
#     # Gun (2) beats Snake (0)
#     if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
#         return -1  # Computer wins
#     else:
#         return 1  # User wins
#
#
# print("Welcome to Snake, Water, Gun Game!")
# print("Enter your choice:")
# print("0 for Snake 🐍")
# print("1 for Water 💧")
# print("2 for Gun 🔫")
#
# while True:
#     try:
#         user = int(input("Your choice: "))
#         if user not in [0, 1, 2]:
#             print("Invalid input! Please enter 0, 1, or 2 only.")
#
#         else:
#             break
#     except ValueError:
#         print("Invalid input! Please enter a number (0, 1, or 2).")
#         exit()
#
# comp = random.randint(0, 2)
#
# choices = ["Snake 🐍", "Water 💧", "Gun 🔫"]
# print(f"\nYou chose: {choices[user]}")
# print(f"Computer chose: {choices[comp]}")
#
# result = check_winner(comp, user)
#
# if result == 0:
#     print("\nIt's a draw! 🤝")
# elif result == 1:
#     print("\nYou won! 🎉")
# else:
#     print("\nYou lost! 😢")

