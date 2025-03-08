import random
from hangman_art import logo, welcome, stages

words = ["python", "javascript", "java", "ruby", "kotlin", "mysql"]

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
life = 6 # Number of total attempts

print(welcome)
print(logo)

while life > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # reveal letter
                print(stages[life])
    else:
        print("That letter doesn't appear in the word, bad luck!!!!.")
        life -= 1
        print(stages[life])

# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
    print(stages[life])
else:
    print("You ran out of life. The word word was: "+chosen_word)
    print("You lost!")
    print(stages[life])