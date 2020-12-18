#imports both the random module and the word list from the words.py module
import random
from words import word_list

#function to select the word for the game
def word_select(played_words):

    #loop that removes all words that have already been played
    for played in list(word_list):
        if played in played_words:
            word_list.remove(played)

    #if all words have been played it sets a value, otherwise it picks a random
    #word from the list of remaining words
    if len(word_list) == 0:
        word = 0
    else:
        word = random.choice(word_list)
    return word


#function to run the hangman game
def play(word, played_words):

    #builds the blanks for the chosen word for the game
    solution = "-" * len(word)
    #initializes all the variables for the start of the game
    guessed = False
    guessed_letters = []
    guessed_words = []
    #there are only 6 tries for the head, both arms, body and both legs
    tries = 6
    #displays the game
    print("Let's play #Hangman: What's Trending Philly???")
    print(display_game(tries))
    print("#", solution)
    print("\n")

    #a loop that will run as long as the word is not guessed and there are enough tries
    while not guessed and tries > 0:
        
        #takes the users input for a guess as either a letter or word
        guess = input("Please guess a letter or word: ").upper()

        #checks to make sure the user input an acceptable letter guess
        if len(guess) == 1 and guess.isalpha():
            #checks to see if the letter was already guessed
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            #checks to see if the letter is not in the word and reduces tries
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                #adds letter to list of guesses
                guessed_letters.append(guess)
            #else it was correctly guessed
            else:
                print("Good job, ", guess, " is in the word!")
                #adds letter to list of guesses
                guessed_letters.append(guess)
                word_as_list = list(solution)
                #adds the correctly guessed letter into the correct spots in the word
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                solution = "".join(word_as_list)
                #if all the correct letters have been guessed, user won
                if "-" not in solution:
                    guessed = True

        #checks to make sure the user input an acceptable word guess
        elif len(guess) == len(word) and guess.isalpha():
            #checks to see if this was already guessed
            if guess in guessed_words:
                print("You already guessed the word", guess)
            #if the guess is not the word, reduces tries by one
            elif guess != word:
                print(guess, " is not the word.")
                tries -= 1
                #adds guessed word to list of guesses
                guessed_words.append(guess)
            #otherwise the user guessed correctly and ginished the game
            else:
                guessed = True
                word_completion = word
        #else the user did not enter a valid guess
        else:
            print("Not a valid guess.")

        #redisplays the game for the next guess and displays already guessed letters
        print(display_game(tries))
        print("#", solution)
        print("\n")
        guessed_letters = sorted(guessed_letters)
        print("Guessed Letters: ", guessed_letters)

    #checks at the end of the while loop if the user won or lost
    if guessed:
        print("You guessed the hashtag!")
        played_words.append(word)
    else:
        print("Sorry, no more tries...The hashtag was #" + word)
        played_words.append(word)


#builds the display for each stage of the game
def display_game(tries):
    stages = ["""
                --------
                |      |
                |      0
                |     \\|/
                |      |
                |     / \\
                -
            """,
            """
                --------
                |      |
                |      0
                |     \\|/
                |      |
                |     / 
                -
            """,
            """
                --------
                |      |
                |      0
                |     \\|/
                |      |
                |    
                -
            """,
            """
                --------
                |      |
                |      0
                |     \\|
                |      |
                |    
                -
            """,
            """
                --------
                |      |
                |      0
                |      |
                |      |
                |    
                -
            """,
            """
                --------
                |      |
                |      0
                |    
                |     
                |    
                -
            """,
            """
                --------
                |      |
                |      
                |    
                |     
                |    
                -
            """
    ]
    return stages[tries]

    
#main function to run the game from
def main():
    #initializes the list of played words
    played_words = []
    #selects the word for the game
    word = word_select(played_words)
    #starts the first game
    play(word, played_words)

    #keeps the game running as long as the user wants to
    while input("Play Again? (Y/N) [N] ").upper() == "Y":
        #selects the word for the next game keeping a list of played words
        word = word_select(played_words)
        #will end the game after all words have been played
        if word == 0:
            print("You have played all the available trends at this moment, play again later")
            input("Press enter/return to exit")
            break
        #will play a new game as long as the user wants to and there are remaining words
        else:
            play(word, played_words)


#allows the game to be started from the command prompt
if __name__ == "__main__":
    main()
