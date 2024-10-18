# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 7 - Beginner - Hangman Game - My Code
# WIP

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6 # my code
chosen_word = random.choice(word_list)
print(chosen_word)

# My code:
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print (placeholder)

display_list = []


# This loops creates _____ list
for n in range(0, word_length):
    display_list.append("_")
print(display_list)  # for checking

display = ""
letters_left = 0
game_ended = False
while not game_ended:
    guess = input("Guess a letter: ").lower()
    # add guessed letter to list
    for n in range(0, word_length):
        if chosen_word[n] == guess:
            display_list[n] = guess
    # convert list to string
    display = ""
    for char in display_list:
        display += char
    print(display)  # for checking
    # check if all letters in a word have been guessed, end game if that's the case
    letters_left = 0
    for n in range(0, word_length):
        if display_list[n] == "_":
            letters_left += 1
    print(f"letters_left = {letters_left}")  # for checking
    if letters_left == 0:
        game_ended = True