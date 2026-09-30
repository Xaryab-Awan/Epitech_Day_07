import random
from english_words import get_english_words_set
max_attempts=6
def my_shuffle(word):
    letters=list(word)
    result=""
    while letters:
        i=random.randrange(len(letters))
        result+=letters.pop(i)
    return result

def scramble(word):
    scrambled=my_shuffle(word)
    while scrambled==word:
        scrambled=my_shuffle(word)
    return scrambled

def pick_word(length):
    words=get_english_words_set(['gcide'],lower=True)
    candidates=[w for w in words if len(w)==length and w.isalpha() and len(set(w))>1]
    if not candidates:
        return None
    return random.choice(candidates)

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

def scramble_game():
    print("******************** WORD SCRAMBLE ********************")
    word=None
    while word is None:
        length=get_word_length()
        word=pick_word(length)
        if word is None:
            print("No usable words of that length, try another.")
    scrambled=scramble(word)
    attempts=max_attempts
    while attempts>0:
        print("Scrambled word:",scrambled)
        guess=input("Your guess: ").strip().lower()
        if guess==word:
            print("Correct! Well done!")
            return
        attempts-=1
        print("Wrong!",attempts,"attempts left")
        print()
    print("You lost! The word was:",word)

scramble_game()