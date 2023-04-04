import os
import random
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase

window = Tk()
window.title('Hangman Game')

MAX_NUMER_OF_GUESSES = 11


def loadImages():
    loadedImages = []
    for i in range(MAX_NUMER_OF_GUESSES + 1):
        loadedImages.append(PhotoImage(file="images/hang" + str(i) + ".png"))
    return loadedImages


images = loadImages()


# def loadRandomWord():
#     # load all files from the folder "wordlists"
#     files = os.listdir("wordlists")
#     # choose a random file
#     file = random.choice(files)
#     print("The word is in the file: " + file)
#     # load the file
#     with open("wordlists/" + file, "r") as f:
#         words = f.read().splitlines()
#     # choose a random word from the file
#     word = random.choice(words)
#     print("The word is: " + word)
#
#     return word

def loadRandomWord():
    if selectedWordlist is None:
        messagebox.showerror("Hangman", "Please select a wordlist")
        return
    # load the file
    with open("wordlists/" + selectedWordlist, "r") as f:
        words = f.read().splitlines()
    # choose a random word from the file
    word = random.choice(words)
    print("The word is: " + word)

    return word


def resetGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0

    the_word = loadRandomWord().upper()
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_" * len(the_word)))
    imgLabel.config(image=images[numberOfGuesses])
    print("Set the Label to: " + ' '.join("_" * len(the_word)))
    print("The word is: " + the_word_withSpaces)
    print("The word is: " + the_word)
    print("The word is: " + str(len(the_word)))


def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < MAX_NUMER_OF_GUESSES:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You guessed it!")
        else:
            numberOfGuesses += 1
            imgLabel.config(image=images[numberOfGuesses])
            if numberOfGuesses == MAX_NUMER_OF_GUESSES:
                messagebox.showwarning("Hangman", "Game Over")


selectedWordlist = None


# def askForWordlist():
#     global selectedWordlist
#     selectedWordlist = askopenfilename(initialdir="wordlists", title="Select a wordlist",
#                                        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

def setWordlist(wordlist=None):
    print("Wordlist: " + str(wordlist))
    global selectedWordlist
    if wordlist is None:
        selectedWordlist = wordlistSelect.get()
    else:
        selectedWordlist = wordlist


wordlistSelect = StringVar()
wordlistSelect.set("Select a wordlist")
wordlistMenu = OptionMenu(window, wordlistSelect, *os.listdir("wordlists"), command=setWordlist)
wordlistMenu.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

imgLabel = Label(window)
imgLabel.grid(row=1, column=0, columnspan=3, padx=10, pady=40)

lblWord = StringVar()
Label(window, textvariable=lblWord, font='consolas 24 bold').grid(row=1, column=3, columnspan=6, padx=10)

n = 0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font='Helvetica 18', width=4).grid(row=2 + n // 9,
                                                                                            column=n % 9)
    n += 1

Button(window, text="New\nGame", command=lambda: resetGame(), font="Helvetica 10 bold").grid(row=4, column=8)

window.mainloop()
