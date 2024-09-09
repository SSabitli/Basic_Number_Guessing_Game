import random

logo = """
                                                                                                                                                                                     ,---,                                                                                                              ,--.                                                          ,`--.' |  
  ,----..                                                              ___      ,---,                             ,--.'|                       ____                               |   :  :  
 /   /   \                                                           ,--.'|_  ,--.' |                         ,--,:  : |                     ,'  , `.  ,---,                      '   '  ;  
|   :     :          ,--,                                            |  | :,' |  |  :                      ,`--.'`|  ' :         ,--,     ,-+-,.' _ |,---.'|               __  ,-.|   |  |  
.   |  ;. /        ,'_ /|             .--.--.    .--.--.             :  : ' : :  :  :                      |   :  :  | |       ,'_ /|  ,-+-. ;   , |||   | :             ,' ,'/ /|'   :  ;  
.   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '          .;__,'  /  :  |  |,--.   ,---.          :   |   \ | :  .--. |  | : ,--.'|'   |  ||:   : :      ,---.  '  | |' ||   |  '  
;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./          |  |   |   |  :  '   |  /     \         |   : '  '; |,'_ /| :  . ||   |  ,', |  |,:     |,-.  /     \ |  |   ,''   :  |  
|   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_            :__,'| :   |  |   /' : /    /  |        '   ' ;.    ;|  ' | |  . .|   | /  | |--' |   : '  | /    /  |'  :  /  ;   |  ;  
.   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `.           '  : |__ '  :  | | |.    ' / |        |   | | \   ||  | ' |  | ||   : |  | ,    |   |  / :.    ' / ||  | '   `---'. |  
'   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \          |  | '.'||  |  ' | :'   ;   /|        '   : |  ; .':  | : ;  ; ||   : |  |/     '   : |: |'   ;   /|;  : |    `--..`;  
'   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /          ;  :    ;|  :  :_:,''   |  / |        |   | '`--'  '  :  `--'   \   | |`-'      |   | '/ :'   |  / ||  , ;   .--,_     
|   :    /  :  ,      .-./|   :    |'--'.     /'--'.     /           |  ,   / |  | ,'    |   :    |        '   : |      :  ,      .-./   ;/          |   :    ||   :    | ---'    |    |`.  
 \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'             ---`-'  `--''       \   \  /         ;   |.'       `--`----'   '---'           /    \  /  \   \  /          `-- -`, ; 
  `---`                     `----'                                                         `----'          '---'                                     `-'----'    `----'             '---`"                                                                                                                                                                                         
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100")
difficulty = input("Please choose a difficulty: 'Easy', 'Hard' ").lower()

attempts = {"easy": 10,
            "hard": 5}

n_guesses = attempts[difficulty]

true_guess =  False
true_game_over = False

while true_guess == False:
    chosen_number = random.randint(0, 100)
    while n_guesses > 0:
        player_guess = int(input("Please Make a Guess! "))
        if player_guess == chosen_number:
            print("You got it!")
            true_game_over = True
            break
        elif player_guess > chosen_number:
            n_guesses -= 1
            print(f"Too high! {n_guesses} lives remaining!")
        elif player_guess < chosen_number:
            n_guesses -= 1
            print(f"Too low! {n_guesses} lives remaining")
    if n_guesses == 0:
        print("No lives remaining, Game Over!")
        true_guess = True
    else:
        again = input("Would you like to Play again? Type 'Y' or 'N'").lower()
        if again == "y":
            continue
        elif again == "n":
            break