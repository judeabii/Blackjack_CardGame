# Blackjack
This is an implementation of the card game - Blackjack, using Python.

## Code Explanation
The `Card` class is used to help store the attributes each card in the deck that will help in a game of Blackjack.
The `__str__` function is also used to print out the description of a given card.

```commandline
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.valuecard = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
```

There is also a `Deck` class that is implemented which is used to generate a new and shuffled deck of cards at the start of the game.
Another use case is to ensure the cards are dealt to the player and the dealer.

```commandline
class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append((Card(suit, rank)))

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def get_card(self):
        return self.all_cards.pop()
```

Lastly, the `Player` class defines the various attributes of both the player and the dealer, such as the ability to add a card to their hand from the deck, keep track of the values of their cards, and ofcourse, the name of the Player.

There is also a `__str__` function which easily prints the cards in the hand of the player, along with its value.

```commandline
class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def hit_one_card(self, card):
        self.cards.append(card)

    def sum_of_cards(self):
        sum_of_cards = 0
        for cards in self.cards:
            sum_of_cards += cards.valuecard
        return sum_of_cards

    def __str__(self):
        value_sum = 0
        list_of_cards = []
        for cards in self.cards:
            value_sum += cards.valuecard
            list_of_cards.append(str(cards))
        return f'{self.name} has cards {list_of_cards} with value of {value_sum}'
```

### Gameplay

The player and the dealer are both dealt 2 cards at the start, with the player's cards visible and only one card of the dealer visible.

At every instance of the game there is a check to see if either the Player or dealer have a hand of 21 (Blackjack).

The player is presented with the option of "Hit" or "Stand". The player can continue selecting "hit" as long as the value of the cards are not greater than 21.

When the player decides to "stand" with the cards they have, the dealer is dealt cards. Programmed such that if the hand value of the dealer is less than 17, the dealer will compulsorily request for another card. 

In the end, there are only 3 outcomes: the player wins, the dealer wins or it's a draw. The user also has the option to play again or quit.

#### Sample Output
```commandline
Enter your name:
Jude
Jude has cards ['Two of Clubs', 'Ace of Spades'] with value of 13
Dealer's last card is [Six of Clubs]
Hit or Stand?
hit
Jude has cards ['Two of Clubs', 'Ace of Spades', 'Two of Spades'] with value of 15
Hit or Stand?
hit
Jude has cards ['Two of Clubs', 'Ace of Spades', 'Two of Spades', 'Four of Clubs'] with value of 19
Hit or Stand?
stand
Dealer has cards ['King of Spades', 'Six of Clubs'] with value of 16
Dealer has cards ['King of Spades', 'Six of Clubs', 'Four of Diamonds'] with value of 20
Dealer wins!!
Do you want to play again Jude? (Y/N)
N
Thank you for playing!
```