import os
import random
from string import ascii_uppercase
from tkinter import messagebox

from ttkbootstrap import *
from StringUtils import *

window = tk.Tk()
# window = ttk.Window(themename="darkly")
window.title('Hangman Game')
# window.iconbitmap('images/hangman.ico')
# window.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='images/hangman.ico'))

MAX_NUMBER_OF_GUESSES = 11
LETTERS_PER_ROW = 9

numberOfGuesses = 0
word = ""
guessedWord = ""


def loadImages():
    loadedImages = []
    for i in range(MAX_NUMBER_OF_GUESSES + 1):
        # loadedImages.append(tksvg.SvgImage(file="images/svg/hang" + str(i) + ".svg"))
        loadedImages.append(PhotoImage(file="images/png/hang" + str(i) + ".png"))
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
    global word
    global guessedWord
    global numberOfGuesses
    numberOfGuesses = 0

    word = loadRandomWord().upper()
    guessedWord = "_" * len(word)
    wordLabel.set(' '.join(guessedWord))
    imageLabel.config(image=images[numberOfGuesses])
    print("Set the Label to: " + ' '.join("_" * len(word)))
    print("The word is: " + word)
    print("The word is: " + word)
    print("The word is: " + str(len(word)))


def guess(guessedLetter):
    print("Guessed letter " + guessedLetter)
    global word
    global guessedWord
    global numberOfGuesses

    # if the number of guesses is less than the maximum number of guesses
    if numberOfGuesses < MAX_NUMBER_OF_GUESSES:

        # get the characters of the word
        wordCharacters = list(word)
        print("Word Characters: " + str(wordCharacters))

        # get the characters of the already guessed word
        guessedWordList = list(guessedWord)
        print("Guessed Word: " + str(guessedWordList))

        # if the guessed letter is in the word
        if word.count(guessedLetter) > 0:

            # loop through the word
            for letterIndex in range(len(wordCharacters)):

                # if the letter at the current index is the guessed letter
                if wordCharacters[letterIndex] == guessedLetter:
                    # set the guessed word at the current index to the guessed letter
                    guessedWordList[letterIndex] = guessedLetter

                # set the word label to the guessed word
                guessedWord = "".join(guessedWordList)
                wordLabel.set(" ".join(guessedWord))

                # if the word label is the same as the word with spaces
                if guessedWord == word:
                    messagebox.showinfo("Hangman", "You guessed it!")
                    newGame = messagebox.askyesno("Hangman", "Do you want to play again?")
                    if newGame:
                        print("New Game")
                        resetGame()
                    else:
                        print("Exit")
                        window.destroy()
        else:
            # increase the number of guesses
            numberOfGuesses += 1

            # set the image to the next image
            imageLabel.config(image=images[numberOfGuesses])

            # if the number of guesses is equal to the maximum number of guesses (game over)
            if numberOfGuesses == MAX_NUMBER_OF_GUESSES:
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
wordlistMenu.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

imageLabel = tk.Label(window)
imageLabel.grid(row=1, column=0, columnspan=3, padx=10, pady=40)

wordLabel = tk.StringVar()
tk.Label(window, textvariable=wordLabel, font='Arial 20 bold').grid(row=1, column=3, columnspan=6, padx=10)

letterIndex = 0
for letter in ascii_uppercase:
    tk.Button(window, text=letter, command=lambda pressedLetter=letter: guess(pressedLetter), font='Arial 16',
              width=4).grid(
        row=2 + letterIndex // LETTERS_PER_ROW,
        column=letterIndex % LETTERS_PER_ROW)
    letterIndex += 1

# n = 0
# for c in ascii_uppercase:
#     Button(window, text=c, command=lambda c=c: guess(c), font='Helvetica 18', width=4).grid(row=2 + n // 9,
#                                                                                             column=n % 9)
#     n += 1

# Button(window, text="New\nGame", command=lambda: resetGame(), font="Helvetica 10 bold", width=4).grid(row=4, column=8)

tk.Button(window, text="New\nGame", command=lambda: resetGame(), font="Arial 10 bold", width=4).grid(row=0, column=8)

window.mainloop()
