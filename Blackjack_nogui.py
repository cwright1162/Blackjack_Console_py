#! /usr/bin/env python3
"""
Blackjack Card Game

This is the Console version of the game Blackjack.
The program also included:
    User Registration
    User Login

Authors:
    Haley Johnson
    Hellen Geraldino-Madera
    Adrianne Santiago
    Chris Taliercio
    Ian Wiley
    Corey Wright
Version:
    2.2
"""

# import useful modules
import random
import sys
from turtle import *
import datetime
import time

# Components to build a deck
suits = ["spades", "hearts", "clubs", "diamonds"]
faces = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# List of random intro messages
welcomes = ["Welcome to a wonderful game of Blackjack! I'm Jeff Probst and I have just one question for you: Can you beat me? If you do, you get the title of Ultimate Blackjacker. Big enough stakes for ya?",
            "HOORAY! BLACKJACK!", "I challenge you to a game of Blackjack!"]

# List of components of passwords
pass_gens = ["wheatlover", "2bornot2b", "himom", "youplayingames", "iliketurtles", "lasagna", "hauntedshoppinglist"]

def main():
    """
    Main Function to run the program. In this function, we have the user register
    and then login. If they succeed, then they are able to play Blackjack.
    The user also may exit at any time by typing 'exit' into the inputs.
    """

    print("Welcome!")
    print("If you choose to exit the login screen at any time, type 'exit'")

    # Start registration and ask user to login with the generated credentials
    loginCred = registration()
    user = loginCred[0]
    password = loginCred[1]
    print()
    can_Play = login(user, password)

    # Check to make sure player's login was successful.
    # Only allow them to play if they do login
    if can_Play:

        # Game loop
        # Start Blackjack and once the round is over, ask if they want to play again
        while True:
            print()
            game = Blackjack()
            game.play()

            choice = input("Want to play another round? [Y/N]: ")

            # Validate user input
            if choice.upper() == 'Y':
                print("Heck yes!")

            elif choice.upper() == 'N':
                print("Boooooo. Bye")
                break

            # Handle case where user inputs incorrect response
            else:
                for _ in range(3):
                    print("...")
                    time.sleep(1)
                print("You know what. I'll take that as a yes! That's the spirit!")
                time.sleep(2)

    # If user doesn't login correctly, and somehow gets to this point, just exit the program
    else:
        sys.exit(0)


def registration():
    """
    Function that generates a username and password for the user.

    Returns:
        A tuple value with the generated username and password, respectively.
    """

    # Print Registration Form Title
    print("User Registration Form")
    print()

    # Ask for information. Allow user to type exit at anytime to quit
    first_Name = input("Enter your first name: ")

    if first_Name.upper() == 'EXIT':
        sys.exit("Exit requested")
    
    last_Name = input("Enter your last name: ")

    if last_Name.upper() == 'EXIT':
        sys.exit("Exit requested")
    
    birth_Year = input("Enter your birth year (you must be 13+ to play. This game *could* be played for money and we don't want any silly 12-year-olds gambling): ")

    current_Year = datetime.datetime.now().year

    # Keep trying to get a valid birthyear for as long as user does not input a correct string
    while True:

        # Try to get an integer value of birth_Year
        try:
            
            if current_Year - int(birth_Year) <= 13:

                sys.exit("You are too young to play. >:(")

            else:

                # User did input a valid year, so create credentials
                username = first_Name[0] + last_Name
                password = random.choice(pass_gens) + birth_Year

                print("\nRegistration Complete! \nLogin Informaion:")
                print("Username:", username)
                print("Password:", password)
                break

        except:

            if birth_Year.upper() == 'EXIT':
                    sys.exit("Exit requested")

            # User did not enter valid year. Try asking again
            print("That is an invalid year. try again.")
            birth_Year = input("Enter your birth year: ")

    return (username, password)
    

def login(loginUser, loginPass):
    """
    Function that simulates a login prompt. The user must input a username
    and password that matches the generated credentials from registration

    Arguments:
        loginUser - The correct username
        loginPass - The correct password

    Return:
        True - Successful login simulation
    """

    # Login Form Message
    print("Blackjack Login")

    attemptLogin = True

    # Try to get the user to login for as long as they want to continue
    while attemptLogin:

        username = input("Username: ")

        if username.upper() == 'EXIT':
            sys.exit("Exit requested")
        
        password = input("Password: ")

        if password.upper() == 'EXIT':
            sys.exit("Exit requested")

        # Log the user in and return true if they input the correct info
        if username == loginUser and password == loginPass:

            attemptLogin = False
            print("Login Successful!")
            return True

        elif username != loginUser:

            print("Incorrect username. Please try again.")

        elif password != loginPass:

            print("Incorrect password. Please try again.")

        else:

            print("Incorrect username and password. Please try again.")


def _turtleWin():
    """
    Displays a fun victory message when you win a game
    """

    clear()
    color('Green')
    style = ('Dancing Script', 40, 'italic')
    write("Winner!", font=style, align='center')
    hideturtle()
    

def _turtleLose():
    """
    Displays a sad loss message when you lose a game
    """

    clear()
    color("Blue")
    style = ('Metal Mania', 40, 'bold')
    write("Loser!", font=style, align='center')
    hideturtle()


class Blackjack(object):
    """
    Class that contains alls the game code for Blackjack

    Arguments:
        Object - Treats Blackjack as a subclass of object
    """

    def __init__(self):
        """
        Initializes the instance of Blackjack with its own deck,
        player, and dealer. Gives each player 2 cards to start
        """

        # Generate deck and shuffle it
        self.deck = Deck()
        self.deck.shuffle()

        # Give the player and dealer two cards each for the start of the round
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])


    def play(self):
        """
        Start the game of Blackjack.
        Loops through a round of the game starting with the player's turn.
        End game messages are displayed based on win or loss
        """

        # Display a random welcome message
        print(random.choice(welcomes))
        print()

        # Display the player's hand along with one card of the dealer's hand
        print("Player:\n", self.player)
        print()
        print("Dealer:\n", self.dealer)
        print()

        # Check if player got Blackjack right after cards are dealt
        if self.player.hasBlackjack():

            print("Lucky you! You drew Blackjack!")
            # Turtle victory message
            _turtleWin()

        # Run through game like normal
        else:

            # Loop for as long as user wants to hit, or until bust
            while True:

                choice = input("Hit? [Y/N]: ")

                if choice.upper() == 'Y':

                    self.player.hit(self.deck.deal())
                    points = self.player.getPoints()

                    print("Player:\n", self.player)
                    print()

                    if points == 21:

                        print("You got a score of 21. You Stand.")
                        break

                    elif points > 21:

                        print("Bad luck. You Bust.")
                        break

                # Check to see if user inputs exit or an invalid response
                elif choice.upper() != 'Y' and choice.upper() != 'N':

                    if choice.upper() == 'EXIT':
                        sys.exit("User Request")

                    else:

                        print("Hey... You uh... need to enter a valid response.")
                        continue

                else:
                    break

            # Get the player's points at the end of turn
            player_Points = self.player.getPoints()

            if player_Points > 21:

                # Turtle loss message
                _turtleLose()

            # Player didn't bust, so see what dealer gets
            else:

                # Dealer's Turn
                print()
                self.dealer.hit(self.deck)
                print("Dealer:\n", self.dealer)
                print()

                # Get the dealer's points at the end of turn
                dealer_Points = self.dealer.getPoints()

                # Check if player or dealer won
                if dealer_Points > 21:

                    print("The Dealer Busts.")
                    # Turtle victory message
                    _turtleWin()

                elif dealer_Points > player_Points:

                    if dealer_Points == 21:

                        print("Dealer wins with Blackjack.")

                    else:

                        print("Dealer wins with a higher score.")

                    # Turtle loss message
                    _turtleLose()

                elif dealer_Points < player_Points:

                    if player_Points == 21:

                        print("Player wins with Blackjack.")

                    else:

                        print("Player wins with a higher score.")
                    # Turtle victory message
                    _turtleWin()

                elif dealer_Points == player_Points:

                    if self.player.hasBlackjack() and not self.dealer.hasBlackjack():

                        print("You win with Blackjack!")
                        # Turtle victory message
                        _turtleWin()

                elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():

                    print("Dealer wins with Blackjack")
                    # Turtle loss message
                    _turtleLose()

                else:

                    print("There's a tie. Dealer wins by default.")
                    # Turtle loss message
                    _turtleLose()
                
                    

class Card(object):
    """
    Class for the Card object.
    Each card is initialized to have its own suit, face, and value.
    A Card can be face up or face down
    """

    def __init__(self, suit, face):
        """
        Initializes an instance of a Card with a suit, face, and point value
        """

        self.suit = suit
        self.face = face

        # If card is an ace, default value to 11
        if face == 'A':
            self.point = 11

        # If card is a Jack, Queen, or King, set value to 10
        elif face in ['J', 'Q', 'K']:
            self.point = 10

        # If card is not an Ace, Jack, Queen, or King, simply set point to the existing face value
        else:
            self.point = int(face)

        # Default Card to face up
        self.hidden = False


    def __str__(self):
        """
        Generates a String to describe the card

        Returns:
            a String of the card description, or state if it is hidden
        """

        if self.hidden:
            return 'Card Hidden'

        else:
            return self.face + ' of ' + self.suit 
        

    def face_down(self):
        """
        Sets the card to hidden
        """
        
        self.hidden = True


    def face_up(self):
        """
        Sets the card to visible
        """
        
        self.hidden = False


class Deck(object):
    """
    Class for the Deck object.
    A Deck contains a card for each combination of suits and faces
    """

    def __init__(self):
        """
        Create a populated Deck upon initialization.
        Shuffle the complete deck
        """

        self.cards = [Card(suit, face) for suit in suits for face in faces]
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the Deck of Cards
        """

        random.shuffle(self.cards)


    def deal(self):
        """
        Deals a sinlge card and removes it from the Deck

        Returns:
            A Card from the top of the Deck
        """

        return self.cards.pop()


class Player(object):
    """
    Class for the Player object.
    A Player is a participant in the game of Blackjack.
    Players can hit, stand, and has their own hand of cards
    """

    def __init__(self, cards):
        """
        Initialize the instance of the Player with their own hand of cards.
        """

        self.cards = cards


    def __str__(self):
        """
        Generates a list of the cards in the Player's hand

        Returns:
            hand - The Player's hand of Cards
        """

        # Take every card in the hand and generate a string
        # of cards in the player's hand
        # separated by commas
        hand = ", ".join(map(str, self.cards))

        # Get the total number of points and add it to the end of the string
        hand += "\n" + str(self.getPoints()) + " Points"

        return hand

    def hasBlackjack(self):
        """
        Checks if the Player has Blackjack.
        Score of 21

        Returns:
            True - Player has Blackjack
            False - Player does not have Blackjack
        """

        if self.getPoints() == 21:
            return True
        else:
            return False


    def hit(self, card):
        """
        Adds a Card the the Player's hand
        """

        self.cards.append(card)


    def getPoints(self):
        """
        Calculates the total number of points in the Player's hand.
        Changes the value of any Aces if necesssary.

        Returns:
            points - the total number of points the Player has.
        """

        points = 0

        for card in self.cards:

            points += card.point

            if card.face == 'A':

                if points > 21:
                    card.point = 1
                    points -= 10

        return points


class Dealer(Player):
    """
    Sub-Class of the Player Class.
    A Dealer is a specific type of Player who has special game rules.
    Only one Card is shown in the hand of the Dealer until it is their turn.
    Dealer's also must hit until they get points >= 17.
    """
    
    def __init__(self, cards):
        """
        Initializes the Dealer with a hand of cards.
        Also only shows one card until their turn occurs.
        """

        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self):
        """
        Generates a string depending on how many cards to show in the
        Dealer's hand.

        Returns:
            A String of Card(s) in the Dealer's Hand.
        """

        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)


    def hit(self, deck):
        """
        Simulates the Dealer taking a hit.
        Dealer must hit until their score is >= 17
        Adds a Card to their hand and shows the Dealer's full hand
        """

        self.showOneCard = False
        
        while self.getPoints() < 17:
            
            self.cards.append(deck.deal())


if __name__ == '__main__':

    # Run main function
    main()
