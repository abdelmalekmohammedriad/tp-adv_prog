import random
class ScoreClass: 
    score=0
    def __init__(self):
        print("the current score is:",ScoreClass.score)  
class Guessn:
    def __init__(self):
        print("welcome to guessing game\n")
    def geussM(self):
        clist=[1,2,3,4,5,6,7,8,9,10]
        n=random.choice(clist)
        for t in range(4):
            a=int(input("guess a number?\n"))
            if a==n:
                print("congrats u win !!")
                ScoreClass.score+=1
                break
            elif a>n:
                print("this number is higher")
            else:
                print("this number is less")
