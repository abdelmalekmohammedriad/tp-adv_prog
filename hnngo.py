import random
from guess import ScoreClass
class HangMan:
    def __init__(self):
        print("it's hangman game")
    def runhangeman(self):
        f = ["apple", "banana", "mango", "orange"]
        r = random.randint(0, 3)
        k = f[r]
        bol = bol2 = False

        l = len(k)
        res = ['_'] * l
        print("The word to guess has", l, "letters.")
        split = list(k)

        attempts = l

        for t in range(l+2):
            bol = False  
            print("Guess a letter:")
            a = input().lower()

            for j in range(l):
                if a == split[j]:
                    bol = True
                    res[j] = a

            if bol:
                print("Good, keep going:", res, "\n")
            else:
                print("No problem, try again\n")
            
            print(l+2- t - 1, "attempts left\n")

            if res == split:  
                print("You win!\n")
                print("The word was:", k)
                ScoreClass.score +=1
                print(" the current score is:", ScoreClass.score)

                break
        else:
            print("You lost. The word was:", k)

