import random
import time
from english_words import get_english_words_set
time_limit=15
number_of_penalties=12

def check(num):  
    if num<=0:
         print("You loooose!!")
         return True
    return False

def get_word_length():
      word_length=-1
      while word_length < 1:
             try:
                 word_length = int(input("Enter the length of the word you want to guess: "))
                 if word_length < 1:
                     print("Length must be 1 or greater.")
             except ValueError:
                 print("Please enter a valid integer.")
                 word_length = -1
      return word_length

def  rand():
    num=[1,2,3,4,5]
    return random.choice(num)


def randomword(word_length):
        words=get_english_words_set(['gcide'],lower=True)
        selected_words=[word for word in words if len(word)==word_length and word.isalpha()]
        if not selected_words:
         return None
        choosen_word=random.choice(selected_words)
        return choosen_word


def input_pattern(length):
    empty_word=[]
    for i in range(length):
        empty_word.append('_')
    print()
    return empty_word

def check_char(char,word):
    return [i for i, c in enumerate(word) if c == char]

def check_full_word(ans,word):
     if ans==word:
          return True
     else:
          return False

def get_char():
    char=""
    while len(char) != 1 or not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
            try:
                char=str(input("Enter the character you guessed: "))
                if len(char)>1:
                    print("A character cant be that long!")
                if len(char) == 1 and not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
                    print("Please Enter a Valid character!")
            except (ValueError,TypeError):
                print("Please Enter a Valid character!")
                char="" 
    char=char.lower()
    return char

def hint(word, empty_word):
    hidden = [word[i] for i in range(len(word)) if empty_word[i] == "_"]
    letter = random.choice(hidden)
    for i in check_char(letter, word):
        empty_word[i] = letter
    return letter

def main_func(number_of_penalties):
    print("********************WELCOME TO HANGMAN!!!!!!********************")
    word=None
    while word is None:
        word_length=get_word_length()
        word=randomword(word_length)
        if word is None:
            print("No words of that length, try another.")
    empty_word=input_pattern(word_length)
    print("Making a word...")
    guessed=[]
    while number_of_penalties>0:
        for char in empty_word:
             print(char,end=" ")
        print()
        print()
        choice=input("1) Guess a character: \n2) Guess the full word\n For Hint Enter ? it costs 2 penalties\n>").strip()
        if choice == "1":
            start_time=time.time()
            char=get_char()
            if time.time()-start_time > time_limit:
                        print("Too slow! Time's up.")
                        number_of_penalties-=1
                        continue
            if char in guessed:
                print("You already guessed that!")
                continue
            guessed.append(char)
            indexes=check_char(char,word)
            if not indexes:  
                print("Wrong Guess")
                number_of_penalties-=1
            else:
                print("Correct Guess")
                for i in indexes:
                     empty_word[i]=char
                if "_" not in empty_word:
                    print("Congratulations!!,Well Done")
                    print("Your Word was: ",word)
                    return
        elif choice =="2":
             start_time=time.time()
             guessed_word=input("Enter the full word: ").strip().lower()
             if time.time()-start_time > time_limit:
                print("Too slow! Time's up.")
                number_of_penalties-=5
                continue
             if(check_full_word(guessed_word,word)):
                  print()
                  print("Congratulations!!,Well Done")
                  print("Your Word was: ",word)
                  return
             else:
                  number_of_penalties-=5
                  print()
                  print("Wrong Guess Sorry")
        elif choice=="?":
             hidden_letters = {word[i] for i in range(len(word)) if empty_word[i] == "_"}
             if len(hidden_letters) <= 1:
                  print("You cant use hint right now")
                  continue
             if number_of_penalties - 2 <= 0:
                  print("cant use hint because of penalties")
                  continue
             char=hint(word,empty_word)
             number_of_penalties-=2
             guessed.append(char)
        else:
             print("Enter a valid Choice!!")
             print()
             continue
        print("You got ",(number_of_penalties)," number of penalties left")
        if(number_of_penalties==1):
             print("Lucky Enough You are getting some increase in penalties lets see what your luck says ")
             number_of_penalties+=rand()
             print("You now have ",number_of_penalties," penalites left")
        print()
    check(number_of_penalties)
    print("The word was: ",word)
        
main_func(number_of_penalties)