import time

from hangman import Hangman

def play():
    game = Hangman()

    game.message("Welcome to the wild west!")
    game.render()
    time.sleep(4)

    game.clear_messages()
    game.message("The ole rascal's been charged with a crime he didn't commit.")
    game.render()

    time.sleep(5)
    game.clear_messages()
    game.message("Help him prove his innocence by guessing his alibi the ole fashion way: a game of Hangman.")
    game.render()

    time.sleep(5)
    game.clear_messages()
    game.message("Alright cowboy, get in there and start guessing.")
    game.render()

    time.sleep(5)
    game.clear_messages()

    while True:
        game.render()
        game.prompt()
        if game.has_won():
            game.clear_messages()
            game.message("Good job partner! The ole rascal made it out alive. You're pretty sharp.")
            game.render()
            return
        
        if game.has_lost():
            game.message("Its a somber day pal. You couldn't prove the ole rascal's innocence. Better luck next time.")
            game.render()
            return

if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print("\nWell so long quitter. Thanks for trying I guess...")

