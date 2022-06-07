print("welcome")
import random

choices = ["rock", "paper", "scissors"]


is_running= True
while True:
    cpu = random.choice(choices)

    player = input("enter your prefered choice:").lower()
    if player in choices:
        pass
    else:
        ("you have entered an invalid option")
    if player == cpu:
        print("player:",player)
        print("cpu:", cpu)
        print("tie")
    elif player =="rock" and cpu == "scissors":
        print("player:", player)
        print("cpu:", cpu)
        print("player win")
        break
    elif player =="rock" and cpu == "paper":
        print("player:", player)
        print("cpu:", cpu)
        print("cpu win")
        break

    elif player =="scissor" and cpu == "paper":
        print("player:", player)
        print("cpu:", cpu)
        print("player win")
        break
    elif player =="scissors" and cpu == "rock":
        print("player:", player)
        print("cpu:", cpu)
        print("cpu win")
        break
    elif player =="paper" and cpu == "scissors":
        print("player:", player)
        print("cpu:", cpu)
        print("cpu win")
        break
    elif player =="paper" and cpu == "rock":
        print("player:", player)
        print("cpu:", cpu)
        print("player win")
        break
