import re

from get_word import get_word
from clear import clear
from color import gray, red
from render_noose import render_noose

CHANCES = 7

class Hangman:
    def __init__(self):
        self.word = get_word().upper()
        self.used_incorrect_letters = []
        self.messages = []
        
        self.letters = {}
        for letter in self.word:
            if letter in [".", " "]:
                continue
            self.letters[letter] = False
            
        
    def render(self):
        clear()
        print(gray("( To exit, hit Ctrl + C )\n\n"))
        count = "(" + str(len(self.used_incorrect_letters)) + "/" + str(CHANCES) + ")"
        if (CHANCES - len(self.used_incorrect_letters) < 3):
            count = red(count)
        else:
            count = gray(count)
        render_noose(len(self.used_incorrect_letters))
        print("Used " + count + ": " + " ".join(self.used_incorrect_letters))
        print(self.make_word_bar())
        print(self.make_message_box())            

    def make_word_bar(self):
        word_bar = ""
        for letter in self.word:
            if letter == " ":
                word_bar = word_bar + "   "
            elif letter == ".":
                word_bar = word_bar + " . "
            elif self.has_letter(letter) and self.letters[letter]:
                word_bar = word_bar + " " + letter + " "
            else:
                word_bar = word_bar + " _ "
        return word_bar
    
    def make_message_box(self):
        box = " ____________________________________________________ "
        box = box + "\n|                                                    |"
        
        for message in self.messages:
            box = box + "\n| " + message
            for i in range(50 - len(message)):
                box = box + " "
            box = box + " |"

        if not len(self.messages):
            box = box + "\n|                                                    |"
            box = box + "\n|                                                    |"
        
        box = box + "\n|____________________________________________________|"
        
        return box

    def prompt(self):
        letter = input("Pick a letter > ")
        self.clear_messages()

        if (letter.upper() in self.used_incorrect_letters 
            or (self.has_letter(letter) and self.letters[letter])):
            self.message("Whoa there partner, you already used that letter. The ole thinker gettin dusty?")
            return
        
        if not re.match(r'[A-Z]', letter.upper()):
            self.message("Ope, I guess I should've told ya, you only need to worry about letters from A-Z")
            return
            
        if letter.upper() not in self.letters:
            self.used_incorrect_letters.append(letter.upper())
            self.message("Careful there partner. The ole rascal can only take so much. Be more careful next time.")
            return
        self.letters[letter.upper()] = True

    def message(self, message):
        line = ""
        for letter in message:
            line = line + letter
            
            if (len(line) == 50):
                self.messages.append(line)
                line = ""
        if len(line):
            self.messages.append(line)
    
    def clear_messages(self):
        self.messages = []

    def has_letter(self, letter):
        return letter in self.letters
    
    def has_won(self):
        for letter in self.word:
            if not self.has_letter(letter):
                continue
            if not self.letters[letter]:
                return False
        return True

    def has_lost(self):
        return len(self.used_incorrect_letters) >= CHANCES
