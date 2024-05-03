# Build Deck - done

# Play round
    # Shuffling 
    # Dealing
    # Betting
    # Setting Trump - done
    # Playing hand
        # Rules on what can be played, when
    # Scoring round
import pprint as pp 

SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
PAIRED_SUITS = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
NUMBERS = ['Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
POWER = [1, 2, 3, 4, 5, 6]

def create_deck():
    cards = {
        #('King', 'Hearts'): {'effective_suit': 'Hearts', 'suit_power': 2, 'trump': False} 
    }
    for suit in SUITS:
        for number in NUMBERS:
            power = POWER[NUMBERS.index(number)]
            cards[(number, suit)] = {'effective_suit': suit, 'suit_power': power, 'trump': False}
    return cards

def set_trump(trump, deck):
    index_trump = SUITS.index(trump)
    clear_trump(deck)

    jack = 'Jack'
    for number, suit in deck:
        # Setting trump and increasing jack's power
        if suit == trump:
             deck[(number, suit)]['trump'] = True
             if number == jack:
                 deck[(number, suit)]['suit_power'] = 8
        # Switching same color jack
        elif (suit == PAIRED_SUITS[index_trump]) and (number == jack):
            deck[(number, suit)]['trump'] = True
            deck[(number, suit)]['effective_suit'] = trump
            deck[(number, suit)]['suit_power'] = 7
    return
    
def clear_trump(deck):
    for number, suit in deck:
        deck[(number, suit)]['effective_suit'] = suit
        deck[(number, suit)]['trump'] = False
        deck[(number, suit)]['suit_power'] = POWER[NUMBERS.index(number)]
    return

def get_winning_card(led_suit, hand, deck):
    # Returns index of winning card
    values = []
    for card in hand:
        bonus = 0
        if deck[card]['trump']:
            bonus = 20
        elif deck[card]['effective_suit'] == led_suit:
            bonus = 10
        
        values.append(deck[card]['suit_power'] + bonus)
    # winning index
    win_ind = values.index(max(values))
    
    # winning card
    return (hand[win_ind])

cards = create_deck()
set_trump('Hearts', cards)
#pp.pprint(cards)

card1 = ('King', 'Hearts')
card2 = ('Queen', 'Hearts')
card3 = ('King', 'Spades')
card4 = ('Jack', 'Diamonds')
hand = [card1, card2, card3, card4]

print(get_winning_card('Hearts', hand, cards))

set_trump('Hearts', cards)
clear_trump(cards)

pp.pprint(cards)


