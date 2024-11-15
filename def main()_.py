from hnngo import HangMan
from guess import Guessn
from guess import ScoreClass
def display_scoreboard():
    with open("user.txt", "r") as file:
        lines = file.readlines()
    print("\n--- Scoreboard ---")
    for i in range(0, len(lines), 3):  # Step by 3 to get each user record
        username = lines[i].strip()
        score = lines[i+2].strip()
        print(f"Name: {username} | Score: {score}")
    print("------------------\n")
def main():
    print("........  hello in our puzzle program  ........ ")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    user_found = False
    with open("__pycache__/user.txt","r+") as file:
        lines = file.readlines()
    for i in range(0, len(lines), 3):  
        stored_username = lines[i].strip()
        stored_password = lines[i+1].strip()
        if stored_username == username and stored_password == password:
            user_found = True
            ScoreClass.score = int(lines[i+2].strip())  
            break
    
    if user_found:
        print("Welcome back! Your current score is:", ScoreClass.score)
        print("press 0 to see the scoreboard")
        print("Welcome back to our program", username, "we have two games\n1: Hangman\n2: Guess a number")
        choice = int(input())
        if choice==0:
            display_scoreboard()
        if choice == 1:
            game = HangMan()
            game.runhangeman()
        elif choice == 2:
            game = Guessn()
            game.geussM()
        else:
            print("Invalid choice!")
    else:
        print("Welcome new user! Starting score is:", ScoreClass.score)
        with open("user.txt", "a") as file:
            file.write(username + "\n")
            file.write(password + "\n")
            file.write(str(ScoreClass.score) + "\n")
        
        print("Welcome", username, "!")
        print("press 0 to see the scoreboard")
        print("We have two games:\n1: Hangman\n2: Guess a number")
        choice = int(input())
        if choice==0:
            display_scoreboard()
        elif choice == 1:
            game = HangMan()
            game.runhangeman()
        elif choice == 2:
            game = Guessn()
            game.geussM()
        else:
            print("Invalid choice!")
    with open("user.txt", "w") as file:
        for i in range(0, len(lines), 3):
            if lines[i].strip() == username and lines[i+1].strip() == password:
                file.write(username + "\n")
                file.write(password + "\n")
                file.write(str(ScoreClass.score) + "\n")
            else:
                file.write(lines[i])
                file.write(lines[i+1])
                file.write(lines[i+2])
main()

    





    
