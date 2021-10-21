import random
import hangman_art
import hangman_words
from replit import clear

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
guessed = []

print(hangman_art.logo)

#print(f'the solution is {chosen_word}.')

display = []
for i in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in guessed:
        print("You have already guessed " + guess)
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        continue

    guessed += guess

    if guess not in chosen_word:
        print("You have guessed " + guess + " which is not in the word. You lose a life.")
        lives -= 1
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    print(f"{' '.join(display)}")

    if lives == 0:
        end_of_game = True
        print(f"You lose!!\nThe chosed word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You win!!")

    print(hangman_art.stages[lives])