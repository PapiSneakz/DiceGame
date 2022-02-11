import random

cash = 100

while True:
    print("Welcome to our casino!!!!!!")
    print("----------------------------")
    response = input("You have " + str(cash) + "$ (a game costs $20) \nYou wanna role the dice?(type yes or no): ")
    response = response.upper()
    if response == "NO":
        break
    while response != "YES" and response != "NO":
        response = input("Type yes or no")

    if response == "YES":
        player = random.randint(1,6)
        computer = random.randint(1,6)

        print("Player: " + str(player))
        print("Computer " + str(computer))
        print("----------------------------")
        if player == computer:
            print("Boo tie")
        elif player > computer:
            print("GG you won")
            cash += 20
        else:
            print("L you lost")
            cash -= 20

    play_again = input("Are you sure you dont want to play (again)?(Type yes or no): ")
    play_again = play_again.lower()
    if play_again != "yes":
        if cash < 100:
            lost = 100-cash
            print("What a shame u lost " + str(lost) + "$")
        else:
            won = cash-100
            print("Nice you won " + str(won) + "$")
        break
  
