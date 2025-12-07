
.#!/user/bin/env python3
# ----------------------------------------------------------------------------------------------------------
# script: PYCOMM V 1.3.3.py
# first created: 2/7/2025
# last updated: 11/29/2025
# created by: Blake podhorksy 
# created in: Microsoft Visual Studio/Github
# found at: Blakepodhorsky@gmail.com 
# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------
# purpose:
# This program will produce an output showcasing a list of commands that the user can access
# it will 1st welcome the user before asking them to input the password
# after it will present the user with a menu system with various options that can be accesed via user input
# user input will then determin which functions are accesed and what the user is presented with
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# version log: 2/7/2025 creation of PYCOMM 1.0- added banner, menu commands and options G, J, x
#              2/19/2025 creation of PYCOMM 1.1- added quiz game, quality improvments and bug fixes
#              2/19/2025 creation of PYCOMM 1.2- added mainline loop and bug fixes
#              3/3/2025 creation of PYCOMM 1.2.1- added documentation to program, menu commands now functions
#              4/7/2025 creation of PYCOMM 1.3- added more documentation and added Game Of Pig, bug fixes
#              5/14/2025 creation of PYCOMM 1.3.1- added word game, menu updates and documentation updates
#              5/15/2025 significant bug fixes and quality improvments to 1.3.1's additons
#              5/16/2025 minor adjustments to 1.3.1's additons to improve quality
#              11/12/2025 PYCOMM 1.3.2- Removed unecessary code, minor bug fixes with password functionality
#              11/12/2025 added Read.ME,transferd PYCOMM to Github
#              11/14/2025 1.3.2 additons to word game, slight change to documentation. Updated Read.ME
#              11/29/2015 PYCOMM 1.3.3- Added PC part selector, updated menu(option A), updated functions
#              12/3/2025 PYCOMM 1.4.0- Moddification of PC part picker. adjustments to documentation
# ------------------------------------------------------------------------------------------------------------

#imports
#---------------------------------------------
# this section provides imports to the program
import random
#---------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#function definitions
# this section defnines our various functions that the program 
# these functions are called within eachother or later in the program
#--------------------------------------------------------------------------------------------------------------

def menu():
    #this function gives the user a list that 
    #falls into place during the mainline program
    #it presents the user with various options
    print("please select from the following options:")\
    print("A - PC part selection")
    print("B - print welcome banner")
    print("M - display menu")
    print("Q - take a short quiz")
    print("J - Tell a horrendiously bad dad joke")
    print("P - Play Game Of Pig Game")
    print("G - play guess the word")
    print("X - Exit the program")

def pc_prt_select():
    # this function takes user imputs to create an optimal PC based of use and budget
    # this is modeled after a previous project i made, however it adds RAM and a CPU and a motherboard
    # all prciing info is based of off Amazon.com, these prices are the prices of december of 2025
    budget = num(input("Whats your budget(5000, 3500, 2500, 1500): "))
    pc_use = str(input("What is the PC for(gaming- streaming- editing): "))
    your_pc == str("Your PC parts include a " + gpu + ", a " + cpu + ", a " ram + " and a "  + mthr_brd)
    gpu = str("")
    cpu = str("")
    ram = str("")
    mthr_brd = str("")
    if pc_use == "Gaming" or pc_Use == "gaming":
        if budget == 5000:
             gpu = "ROG Astral GeForce RTX 5090 OC edition"
             cpu = "AMD RYZEN 7 7700X"
             ram = "Kingston Fury beast DDR5 64GB 6400 MHz"
             mthr_brd = "ASUS ROG Strix X870E-E Gaming Wifi"
             print(your_pc)
        elif budget == 3500:
             gpu = "AMD Radeon RX 7900 XT phantom OC"
             cpu = "AMD RYZEN 7 9800X3D"
             ram = "Kingston Fury beast DDR5 64GB 6400 MHz"
             mthr_brd = "TUF gaming B850- Plus WIFI AMD AM5 ATX"
             print(your_pc)
        elif budget == 2500:
            gpu = "Radeon RX 9060 XT OC"
            cpu = "Ryzen 5 9600X"
            ram = "T-FORCE DELTA DDR% 32GB 6000 MHz"
            mthr_brd = "ASUS ROG Strix X870E-E Gaming Wifi"
            print(your_pc)
        elif budget == 1500:
            gpu = ""
            cpu = ""
            ram = ""
            mthr_brd = ""
            print(your_pc)

def get_guess():
    # this function gets a users guess for the word game
    # it ensures that the input must be lower and exatly one character
    while True:
        guess = str(input("Guess: "))
        if not guess.islower():
            print("must be a lowercase letter!")
        elif len(guess) > 1:
            print("must be exaclty one character!")
        else:
            break
            
    return guess
    
def update_dashes(secret_word, dashes, guess):
    # this function updates the dashes during the word game
    updated_dash = list(dashes)
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            updated_dash[i] = guess
    return "".join(updated_dash)

def wrd_lst_choice():
    # this function asks the user what type of words they would like for the word game
    # it then presents them with a random word from either a 3 word list or a 5 word list
    choice = str(input("What words would you like(3 or 5): "))
    words_3 = ["dog", "cat", "car", "lab", "pet", "vet", "war", "the", "pop", "sea", "eat", "pup", "men"]
    words_5 = ["point", "pichu", "mario", "sword", "cloud", "great", "theme", "loops", "menus", "keeps"]
    if choice == "3":
        secret_word = random.choice(words_3)
        return secret_word
    elif choice == "5":
        secret_word = random.choice(words_5)
        return secret_word
    else:
        print("error")

def word_game():
     # this fucntion creates a word game for the user similar to hangman
     # the goal is to guess the word in 10 tries, if they do the win, otherwsie they lose
     #  this also uses functions update_dashes and get_guess
        words_3 = ["dog", "cat", "car", "lab", "pet", "vet", "war", "the", "pop", "sea", "eat", "pup", "men"]
        words_5 = ["point", "pichu", "mario", "sword", "cloud", "great", "theme", "loops", "menus", "keeps"]
        word_lst = ([words_3, words_5])
        secret_word = wrd_lst_choice()
        dashes = "-"*len(secret_word)
        guesses_left = 10
        print(dashes)


    # this section uses previous functions to set up the actual game itself
        while guesses_left > 0:
            guess = get_guess()
            if guess in secret_word:
                print("That letter is in the secret word")
                dashes = update_dashes(secret_word, dashes, guess)
                print(dashes)
                print("you have  " + str(guesses_left) + " guesses left")
                if dashes == secret_word:
                    print("You win! The word was " + secret_word)
                    break
    
    # this section checks if the letter is not in the secret word, and then subtracts a guess from the total guesses
            else:
                print("That letter is not in the secret word")
                print(dashes)
                guesses_left = guesses_left - 1
                print("you have " + str(guesses_left) + " guesses left")

            if guesses_left == 0:
                print("You lose! The word was " + secret_word)

def quiz():
    #this function builds the quiz game
    #the quiz game asks the user various questions
    # if they get it right they score, otherwise the dont
    print("Multiple-choice quiz game!")
    score = 0
    q1 = """1. what is the capital of France?
    (a) Paris
    (b) france city
    (c) Frankreich
     """
    q2 = """2. How many bones do sharks have?
    (a) 500
    (b) 0
    (c) 200,000
    """
    q3 = """3. what does SQL stand for?
    (a) structured querry language
    (b) secret quiz lesson
    (c) someting quiet lurks
    """
    print(q1)
    # a_q1 stands for awnser to question 1, same for a_q2 and a_q3
    a_q1 = input("what is your choice: ")
    if a_q1 == "a" or a_q1 == "A":
        print("Corrct!")
        score += 1
    else:
        print("Incorect!")

    print(q2)
    a_q2 = input("what is your choice: ")
    if a_q2 == "b" or a_q2 == "B":
        print("correct!")
        score += 1
    else:
        print("incorrect!")
    
    print(q3)
    a_q3 = input("what is your choice: ")
    if a_q3 == "A" or a_q3 == "a":
        print("correct!")
        score += 1
    else:
        print("incorrect!")
    
    
    print("Quiz complete!")
    print("You awnsered " + str(score) + " out of 3 questions correctly")  

def joke():
    jokes = ["Why was 6 afraid of 7? because 7 8 9!", "What did america say to germany in the morning? EUROPE!", "whats a skeletons favorite insstument? the TRUMBONE!", 
             "What happend to the lumberjacks legs when he saw a bear? they WOOD'nt move!", "whats the quietest sound a cat can make? a Wisker!"]
    # random.choice selects a random option from a givin list, in this it allows each joke to be diffrent!f
    joked = random.choice(jokes)
    print(joked)


def banner():
    #this function prints our banner
    messege = """
 welcome to
 ____ ___  _ ____  ____  _      _      
/  __\\  \///   _\/  _ \/ \__/|/ \__/|
|  \/| \  / |  /  | / \|| |\/||| |\/||
|  __/ / /  |  \__| \_/|| |  ||| |  ||
\_/   /_/   \____/\____/\_/  \|\_/  \| 
"""
    
    print(messege)

def version():
    # this fucntion prints our verison number
    version_num = "1.3.3"
    print("                      " + version_num)
       
def Game_Of_Pig():

    # ---------------------------------------------------------------------
    # This code will play the game of pig 
    # it will roll a dice at random and if you get a 1 then you
    # will lose that turn and then 
    # it will move on to the next person/computer. If you get to 100 or 
    # more than 100 you will win the game. 
    # ----------------------------------------------------------------------
    
    def roll():
        return random.randint(1, 6)
    
    def player_turn():
        round_score = 0
        while True:
            print(f"This round you have: {round_score}")
            action = input("Would you like to roll or bank? ").lower()
            
            if action == "bank":
                return round_score
            elif action == "roll":
                roll_result = roll()
                print(f"You rolled a {roll_result}.")
                
                if roll_result == 1:
                    print("You rolled a 1! You get a zero for this round!")
                    return 0  
                    # --------------------------------
                    # End the turn with a score of 0
                    # --------------------------------
                round_score += roll_result
            else:
                print("Invalid input. Please choose 'roll' or 'bank'.")
    
    def computer_turn():
        round_score = 0
        while round_score < 15:  
            # --------------------------------------------------------
            # The computer will keep rolling until it hits 15 or more
            # --------------------------------------------------------
            roll_result = roll()
            print(f"The computer rolled a {roll_result}.")
            
            if roll_result == 1:
                print("The computer rolled a 1. End of turn.")
                return 0  
                # ----------------------------------------------
                # Computer gets 0 for the turn if it rolls a 1
                # ----------------------------------------------
            round_score += roll_result
            print(f"This round the computer has: {round_score}")
        # -------------------------------------------
        # The computer banks once it hits 15 or more
        # -------------------------------------------
        print(f"The computer banks {round_score}.")
        return round_score
    
    def Game_Of_Pig():
        player_score = 0
        computer_score = 0
        turn_number = 1
    
        while player_score < 100 and computer_score < 100:
            print(f"\nTurn {turn_number}")
            print(f"Your Current Score is: {player_score}")
            print(f"Computer Current Score is: {computer_score}")
            # --------------
            # Player's turn
            # --------------
            print("\nIt's your turn!")
            player_round_score = player_turn()
            player_score += player_round_score
            print(f"You banked {player_round_score} points. Your total score is: {player_score}")
            
            if player_score >= 100:
                break
            # ------------------------------------------
            # Pause before switching to computer's turn
            # ------------------------------------------
            input("\nPress Enter for the computer's turn...")
            # -----------------
            # Computer's turn
            # -----------------
            print("\nIt's the computer's turn!")
            computer_round_score = computer_turn()
            computer_score += computer_round_score
            print(f"The computer banked {computer_round_score} points. The computer's total score is: {computer_score}")
            
            if computer_score >= 100:
                break
            
            turn_number += 1
        # ---------------------
        # Determine the winner
        # ---------------------
        if player_score > 100 and computer_score > 100:
            if player_score > computer_score:
                print(f"\nYou win with a score of {player_score} vs {computer_score}!")
            else:
                print(f"\nThe computer wins with a score of {computer_score} vs {player_score}!")
        elif player_score >= 100:
            print(f"\nYou win with a score of {player_score}!")
        else:
            print(f"\nThe computer wins with a score of {computer_score}!")

    Game_Of_Pig()

def mainline_pw():
    # this fucntion runs a password authentication that checks if the user inputs the right PW
    # if they do, it then procceds to provide the user with the menu and options that will be called
    correct_pass = "finals"
    guesses_left = 3
    while guesses_left > 0:
        guess = input("enter your password: ")
        if guess != correct_pass:
            guesses_left = guesses_left - 1
            print("Incorrect password. you have " + str(guesses_left) + " attempts left. Please try again.")
        elif guesses_left <= 0:
            print("Incorrect password, Maximum number of attempts reached. Access denied.")
            break
        elif guess == correct_pass:
            print("Correct password! Access granted.")
               
            while guess == correct_pass:# while True starts an infinite loop, this will continue as long as option X is not selected
                menu()
                your_choice = input("Option choice: ")
                if your_choice == "A" or your_choice == "a":
                    pc_prt_select()
                elif your_choice == "B" or your_choice == "b":
                    banner()
                elif your_choice=="M" or your_choice=="m":
                    menu()
                elif your_choice == "Q" or your_choice == "q":
            # ------------------------------------------------
            # Quiz game
            # this section of our code will call the quiz game
            # if the user imputs Q or q as their menu choice
            #-------------------------------------------------
                    quiz()
                elif your_choice == "J" or your_choice == "j":
                    joke()
                elif your_choice == "P" or your_choice == "p":
                    Game_Of_Pig()
                
                elif your_choice == "G" or your_choice == "g":
                   word_game()

                #----------------------
            # Infinite loop denial
            # -------------------------------------------------------------------
            # this Elif statment will break our while loop if the imput is X or x
            # this then causes the exit statment at the end of our code to trigger
            # -------------------------------------------------------------------
                elif your_choice == "X" or your_choice == "x":
                    print("goodbye")
            # this break statment will trigger the end of our program
            # if there was not break here our program would loop forever
                    break
                
    exit()
# ----------------------------------------------------------------------------------------------------------
#mainline/Password authentication (the coil)
#this section prints out banner and version number, then it calls the function mainline_pw
#this function does a password authentication, followed by our actual program and menu system
# ----------------------------------------------------------------------------------------------------------

banner()
version()
mainline_pw()

# welcome to the rattle (end of program)

# ----------------------------------------------------------------------------------------------------------







