import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.valuecard = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


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


name = input("Enter your name:\n")

play_again = True

while play_again:

    player_one = Player(name)
    dealer = Player("Dealer")

    game_on = True

    my_deck = Deck()
    my_deck.shuffle_cards()

    for x in range(2):
        player_one.hit_one_card(my_deck.get_card())
        dealer.hit_one_card(my_deck.get_card())

    print(player_one)
    print(f"Dealer's last card is [{dealer.cards[-1]}]")

    if player_one.sum_of_cards() == 21:
        print(f'{player_one.name} wins!!')
        game_on = False

    if dealer.sum_of_cards() == 21:
        print(f'{dealer.name} wins!!')
        game_on = False

    while game_on:

        valid_inputs = ['hit', 'Hit', 'stand', 'Stand']
        decision = ""
        while decision not in valid_inputs:
            decision = input("Hit or Stand?\n")
        if decision.lower() == 'hit':
            player_one.hit_one_card((my_deck.get_card()))
            print(player_one)

            if player_one.sum_of_cards() == 21:
                print(f'BLACKJACK! {player_one.name} wins!!')
                game_on = False
                break

            elif player_one.sum_of_cards() > 21:
                print(f'Bust! {player_one.name} loses!!')
                game_on = False
                break

        else:
            game_on = False
            print(dealer)
            while dealer.sum_of_cards() < 17:  # and dealer.sum_of_cards()<player_one.sum_of_cards():
                dealer.hit_one_card(my_deck.get_card())
                print(dealer)

            if dealer.sum_of_cards() > 21:
                print(f'{dealer.name} Bust! {player_one.name} wins!!')
                break

            elif dealer.sum_of_cards() == 21:
                print(f'BLACKJACK! {dealer.name} wins!!')
                break

            elif dealer.sum_of_cards() > player_one.sum_of_cards():
                print(f'{dealer.name} wins!!')
                break

            elif dealer.sum_of_cards() < player_one.sum_of_cards():
                print(f'{player_one.name} wins!!')
                break

            elif dealer.sum_of_cards() == player_one.sum_of_cards():
                print("It's a draw!")

    valid_inp = ['yes', 'no', 'Yes', 'No', 'y', 'n', 'Y', 'N']
    playagain = ""
    while playagain not in valid_inp:
        playagain = input(f"Do you want to play again {player_one.name}? (Y/N)\n")
    if playagain.lower() == 'yes':
        play_again = True
    else:
        print("Thank you for playing!")
        play_again = False
