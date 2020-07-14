# print("hello")
# name = "sophia"
# print(name)
# firstName= input ("type in your firstName: ")
# lastName= input ("type in your lastName: ")
# print ("your name is",firstName,lastName)

# firstNumber= int (input ("enter a number: "))
# secondNumber= int (input("enter another number: "))
# print (firstNumber * secondNumber)

# player1 = input("Player 1: ")
# print (player1)

# number = int(input("what is the number?"))
# summation = nuber +2
# print(summation)

# number = int(input("what is the number?"))

# if(nuber < 0):
#         number = int(input("put a number greater than 0:"))

# while (number >- 0):
#     print(number)    
#     number = number -1

keepPlaying = True

while(keepPlaying):
    player1 = input("what is 1's choice?")

    validinput = ["rock","paper","scissors"]

    while(player1 != "rock" and player1 != "paper" and player1 !="scissors"):
        player= input("please enter a valid choice (rock, paper or scissors):")

    # print(player1, "is the right choice")

    player2 = input("what is 2's choice?")

    validinput = ["rock","paper","scissors"]

    while(player2 != "rock" and player2 != "paper" and player2 !="scissors"):
        player= input("please enter a valid choice (rock, paper or scissors):")

    # print(player2, "is the right choice")

    if player1 == player2:
        print("Tie")
    elif player1 == 'rock' and player2 == 'scissors':
        print("Player 1 wins.")
    elif player1 == 'paper' and player2 == 'rock':
        print("Player 1 wins.")
    elif player1 == 'scissors' and player2 == 'paper':
        print("Player 1 wins.")
    elif player2 == 'rock' and player1 == 'scissors':
        print("Player 2 wins.")
    elif player2 == 'paper' and player1 == 'rock':
        print("Player 2 wins.")
    elif player2 == 'scissors' and player1 == 'paper':
        print("Player 2 wins.")

    choice = input("Would you lik to play again?(y/n): ")
    if(choice == "n"):
        keepPlaying = False