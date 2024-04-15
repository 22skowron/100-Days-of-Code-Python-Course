from tkinter import *
import pandas as pd
import random


    ################################## # # VARIABLES USED
BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORD_DISPLAY = 2000

random_index = 0

    ################################## # # LOADING DATA

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

print(df)
    ################################## # # FUNCTIONS

def flip_flashcard():
    english_word = df.loc[random_index, "English"]
    canvas.itemconfig(text_word, text=english_word)
    canvas.itemconfig(text_language, text="English")
    canvas.itemconfig(card, image=image_card_back)


def next_flashcard():
    global random_index
    global flip_card
    canvas.after_cancel(flip_card)
# Changing background, language
    canvas.itemconfig(card, image=image_card_front)
    canvas.itemconfig(text_language, text="French")
# Generating random index
    random_index = random.choice(df.index)
    print(random_index)
# Picking up French word
    french_word = df.loc[random_index, "French"]
# Displaying
    canvas.itemconfig(text_word, text=french_word)
# Flipping flashcard
    flip_card = canvas.after(FRENCH_WORD_DISPLAY, flip_flashcard)


def delete_words_pair():
    global df
    df.drop(random_index, inplace=True)
    print(df.index)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_flashcard()


def reset_progress():
    global df
    df = pd.read_csv("data/french_words.csv")
    df.to_csv("data/words_to_learn.csv", index=False)


    ################################## # # INTERFACE

window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=60, padx=60)

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=3)


image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file="images/card_back.png") # Front and back of the card used alternately
card = canvas.create_image(400, 263, image=image_card_back)


text_language = canvas.create_text(400, 170, text="French", font=("Arial", 22, "italic"))
# canvas.itemconfig(text_language, text="changed text")       # Example on how to change text on canvas

text_word = canvas.create_text(400, 270, text="Word", font=("Arial", 35, "bold"))

image_btn_wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=image_btn_wrong, highlightthickness=0, command=next_flashcard)
btn_wrong.grid(row=2, column=1)

image_btn_right = PhotoImage(file="images/right.png")
btn_right = Button(image=image_btn_right, highlightthickness=0, command=delete_words_pair)
btn_right.grid(row=2, column=3)

btn_skull = Button(text="☠", font=("Arial", 18, "normal"), command=reset_progress)
btn_skull.grid(row=2, column=2)

    ################################## # # PROGRAM START
flip_card = canvas.after(3000, flip_flashcard)
next_flashcard()

#######################################################################################################



#######################################################################################################

mainloop()