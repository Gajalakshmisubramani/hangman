import random
from wordfile import list1
def input_file():
    select_name,select_list= random.choice(list1)
    return select_name,select_list



def input_word(select_list):
    word = random.choice(select_list)
    return word.upper()


def play(word,select_name):
    d_line = "_" * len(word)
    answered = False
    answered_letters = []
    answered_words = []
    tries = 6
    print("Let's start the game")
    print("the random word having",len(word),"letter")
    print("the word is from",select_name)
    print(display_hangman(tries))
    print(d_line)
    print("\n")
    while not answered and tries > 0:
        answer = input("answer a letter or word: ").upper()
        if len(answer) == 1 and answer.isalpha():
            if answer in answered_letters:
                print("You already answered the letter", answer)
            elif answer not in word:
                print(answer, "is not in the word.")
                tries -= 1
                answered_letters.append(answer)
            else:
                print(answer, "is in the word!")
                answered_letters.append(answer)
                word_as_list = list(d_line)
                indices = [i for i, letter in enumerate(word) if letter == answer]
                for index in indices:
                    word_as_list[index] = answer
                d_line = "".join(word_as_list)
                if "_" not in d_line:
                    answered = True
        elif len(answer) == len(word) and answer.isalpha():
            if answer in answered_words:
                print("You already answered the word", answer)
            elif answer != word:
                print(answer, "is not the word.")
                tries -= 1
                answered_words.append(answer)
            else:
                answered = True
                d_line = word
        else:
            print("the symbol enetered is not vaild one")
        print(display_hangman(tries))
        print(d_line)
        print("\n")
    if answered:
        print("the answer is correct,you win!")
    else:
        print("there is no tries left. The word was " + word + ".")
        print("try next time,all the best")


def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
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


def main():
    select_name, select_list = input_file()
    
    while True:
        word = input_word(select_list)
        play(word,select_name)
        select_name,select_list=input_file()
        
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break

if __name__ == "__main__":
    main()
