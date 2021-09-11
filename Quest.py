from Operations.Fight import Back_To_Main
import random
#mob to kill, how many, reward exp
Quests = [
    ["Dog", 10, 25],
    ["Orc", 15, 75],
    ["Abony", 20, 250]
]

Mobs_Killed = 0
CAAQ =  True
RAND = random.randint(0, len(Quests) - 1)

def Quest_main(CAAQ):
    if (CAAQ == True):
        print(f"You must kill {Quests[RAND][0]} {Quests[RAND][1]} times.")
        print(f"You will receive {Quests[RAND][2]} Exp")
        print("Do you accept this quest?")
        CHOOSE = int(input("1. Yes\n2. No\n"))
        if CHOOSE == 1:
            Quest_Func(RAND)
            CAAQ = False
        else:
            Back_To_Main()
    else:
        Quest_Func(RAND)

def Quest_Func(RAND):
    print(f"You must kill {Quests[RAND][0]} {Quests[RAND][1]} times.")
    print(f"Your reward is: {Quests[RAND][2]} Exp\n")
    print(f"Killed mobs: {Mobs_Killed}/{Quests[RAND][1]}")
    input()

