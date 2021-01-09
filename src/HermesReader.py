import sys
import time
import tarotDeck
import menu

hermes = tarotDeck.Reader()
deck = tarotDeck.Deck()
deck.shuffle()

while True:

    # Print option menu
    for key in menu.spreads:
        print('\n', key)
        time.sleep(.25)

    # Get user input
    menuChoice = input("Please select a spread: \n")

    if menuChoice == '0':  # Three Card
        for cards in menu.threeCard:
            hermes.draw(deck)
        hermes.threeCardDeal()
    elif menuChoice == '1':  # Horseshoe
        for cards in menu.horseShoe:
            hermes.draw(deck)
        hermes.horseShoeDeal()

    elif menuChoice == '2':  # Celtic Cross
        for cards in menu.celticCross:
            hermes.draw(deck)
        hermes.celticCrossDeal()

    elif menuChoice == '9':  # Exit
        sys.exit()

    else:
        print("Please select a valid option.")

    hermes.clear()  # Clears Reader Hand
