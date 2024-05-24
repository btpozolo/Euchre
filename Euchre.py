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
import random

SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
PAIRED_SUITS = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
NUMBERS = ['Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
POWER = [1, 2, 3, 4, 5, 6]

GREEN = "\033[32m"
RESET = "\033[0m"

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

def get_winning_card(trick, deck):
    '''
    Takes a hand of cards and returns the winning card given trump suit 
    in deck and assumes first card in trick was card led
    '''

    # Card led starts as highest
    highest_card = trick[0][0]
    led_suit = deck[highest_card]['effective_suit']

    # Each other card is then compared to the current highest
    for idx in range(1, len(trick)):
        highest_card_power = deck[highest_card]['suit_power']

        card_suit = deck[trick[idx][0]]['effective_suit']
        card_is_trump = deck[trick[idx][0]]['trump']
        card_power = deck[trick[idx][0]]['suit_power']

        # print(f'{highest_card = }')

        # print(f'Current card is {trick[idx]}')
        # print(f'{card_suit = }')
        # print(f'{card_is_trump = }')

        if card_suit == led_suit:
            if card_power > highest_card_power:
                highest_card = trick[idx][0]
        elif card_is_trump:
            highest_card = trick[idx][0]
    
    winning_card = [(card, player) for card, player in trick if card == highest_card][0]
    print(f'{winning_card = }')
    return (winning_card[0], winning_card[1])

def shuffle_dict(d):
    items = list(d.items())
    random.shuffle(items)
    return dict(items)

def deal_cards(cards):
    shuffled_deck = shuffle_dict(cards)

    hands = [[] for _ in range(4)]
    
    for hand in hands:
        for _ in range(5):
            card, info = shuffled_deck.popitem()
            hand.append(card)

    showing_card, _ = shuffled_deck.popitem()

    return (hands[0], hands[1], hands[2], hands[3], showing_card)

def display_cards(cards, show_num=True):
    '''
    Need to be passed a list of card objects then displays them with number for playing.
    '''
    # Construct the card string
    num_cards = len(cards)

    print('+----------+ '* num_cards)
    if show_num:
        print("".join([f'|{GREEN}{num}{RESET}         | ' for num in range(1, num_cards + 1)]))
    else:
        print('|          | ' * num_cards)
    print("".join([f'|{card[0]:^10}| ' for card in cards]))
    print('|    of    | ' * num_cards)
    print("".join([f'|{card[1]:^10}| ' for card in cards]))
    print('|          | ' * num_cards)
    print('+----------+ ' * num_cards)

    return


def get_play(hand):
    return

def play_hand(cards):
    # deal hands 
    P1, P2, P3, P4, showing_card = deal_cards(cards)
    print('Players hand is:')
    display_cards(P1)
    print('Please select the number of a card to play:')
    p1_play = int(input()) - 1
    print(f'You played the {P1[p1_play][0]} of {P1[p1_play][1]}.')
    # Validate legal play

    set_trump('Hearts', cards)

    # Play cards
    card1 = P1[p1_play]
    card2 = ('Queen', 'Hearts')
    card3 = ('King', 'Spades')
    card4 = ('Jack', 'Diamonds')
    trick = [(card1, 'P1'), (card2, 'P2'), (card3, 'P3'), (card4, 'P4')]

    # Get winning play
    print(get_winning_card(trick, cards))

cards = create_deck()
play_hand(cards)
pp.pprint(cards)

''''
       User  Comp                               +---------+    
 Score:  5      7         Partner               |  Queen  |
Tricks:  2      2                               | Diamonds|
                           Nine                 +---------+

        User  Comp           D                    
 Score:  5      7         Partner
Tricks:  2      2  
                           Nine
 D                        Spades                        D
Computer 1       King                    Queen        Computer 2
                Hearts                  Diamonds
                            Queen
                            Clubs
Player's hand D
+----------+ +----------+ +----------+ +----------+ +----------+ 
|1         | |2         | |3         | |4         | |5         | 
|   King   | |  Queen   | |  Queen   | |   Ten    | |   Ten    | 
|    of    | |    of    | |    of    | |    of    | |    of    | 
|  Hearts  | |  Hearts  | |  Clubs   | |  Clubs   | |  Spades  | 
|          | |          | |          | |          | |          | 
+----------+ +----------+ +----------+ +----------+ +----------+ 
'''

''.endswith()

def to_jaden_case(string):
    return ' '.join([word.capitalize() for word in string.split()])
 
print(to_jaden_case('HOW CAN MIRRORS BE REAL'))

"HELLOW".capitalize()

def persistence(num):
    times = 0
    while len(str(num)) > 1:
        times += 1
        number = 1
        for char in str(num):
            number *= int(char)
        num = number
    return times

persistence(4)

def longest(a1, a2):
    chars = set(a1).union(a2)
    chars = sorted(list(chars))
    return ''.join(chars)

longest('fdsalfdjsa', 'fdsafdsa')
'''
algo:
    - remove before ://
    - keep until '.'
'''
prefixes =[
    'http://',
    'https://',
    'www.',
]

url = "https://hyphen-site.org"
new_url = ''

for pre in prefixes:
    if url.startswith(pre):
        l = len(pre)
        i = url.find(pre)
        url = url[i + l:]
print(url)

url = url.split('.')[0]

print(url)

if '://' in url:
    _, _,  s = url.partition('://')
    y, _, _ = s.partition('.')

y