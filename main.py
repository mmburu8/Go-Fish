from itertools import combinations
import random
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shapes = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
fulldeck = []
def build_deck():
    for shape in shapes:
        for value in values:
            deckstar = value + ' of ' + shape
            fulldeck.append(deckstar)
    return fulldeck

def top_card(deck):
    topcard = deck[0]
    deck.remove(topcard)
    return topcard
def get_random_card(deck):
    c = random.choice(deck)
    deck.remove(c)
    return c
hand_deck = []
def deal_hand(deck, size_of_hand):
    for x in range(size_of_hand):
        x = top_card(fulldeck)
        deck.append(x)
gsfhd = []
def get_suit(deck, deck_2):
    for y in deck:
        suit = y[:1]
        deck_2.append(suit)
p_count = []
c_count = []
def same_suit(deck, count):
    avant = len(deck)
    comb = combinations(deck, 2)
    for i in list(comb):
        n = 0
        if i[0] == i[1]:
            z = list(i)
            if i == ('1', '1'):
                i = ('10', '10')
            if deck == p_gsfhd:
                print("Ranks ", i, " have been matched from player deck")
            else:
                print("Ranks ", i, " have been matched from computer deck")
            for y in z:
                deck.remove(y)
                count.append(y)
            n = 1
        if n == 1:
            break
    apres = len(deck)
    if avant == apres:
        if deck == p_gsfhd:
            print(player_hand)
            x = input("What rank would you like to ask for?").upper()
            y = x[:1]
            if not y in p_gsfhd:
                print(y)
                print("You do not have that rank in your deck. Please choose a rank you have.")
                x = input("What rank would you like to ask for?").upper()
                y = x[:1]
            print("Computer give me your", x)
            if y in c_gsfhd:
                print(x)
                print("Found you !!!")
                c_gsfhd.remove(y)
                deck.remove(y)
                count.append(y)
                count.append(y)
            else:
                print("Player Go Fish > -")
                p_card = top_card(fulldeck)
                print("This is the card you have picked up ", p_card)
                player_hand.append(p_card)
                p_value = p_card[:1]
                deck.append(p_value)
                print(player_hand)
        else:
            s = random.choice(deck)
            if s == '1':
                print("Computer has asked for your 10")
            else:
                print("Computer has asked for your", s)
            n = input("Do you have this rank?")
            if s in p_gsfhd:
                print(s)
                print(n)
                if s == '1':
                    print("You have handed out this rank 10 to the computer.")
                else:
                    print("You have handed out this rank ", s, " to the computer.")
                p_gsfhd.remove(s)
                deck.remove(s)
                count.append(s)
                count.append(s)
            else:
                print(n, "Computer Go Fish - <")
                c_card = top_card(fulldeck)
                comp_hand.append(c_card)
                c_value = c_card[:1]
                deck.append(c_value)
    return deck

def show_hand_deck(deck_1, deck_2):
    for x in deck_2:
        i = 0
        c = x[:1]
        for y in deck_1:
            if not c in y:
                i += 1
            if i == len(deck_1):
                deck_2.remove(x)
    return deck_2


player_hand = []
p_gsfhd = []
def premiere_player_hand():
    deal_hand(player_hand, 7)
    get_suit(player_hand, p_gsfhd)
    print(player_hand)

comp_hand = []
c_gsfhd = []
def ordinateur_hand():
    deal_hand(comp_hand, 7)
    get_suit(comp_hand, c_gsfhd)
    print(len(comp_hand))


def MBRFI():
    build_deck()
    random.shuffle(fulldeck)
    print(fulldeck)
    premiere_player_hand()
    ordinateur_hand()
    while len(fulldeck) != 0 and len(p_gsfhd) != 0 and len(c_gsfhd) != 0:
        print(player_hand)
        same_suit(p_gsfhd, p_count)
        show_hand_deck(p_gsfhd, player_hand)
        show_hand_deck(c_gsfhd, comp_hand)
        same_suit(c_gsfhd, c_count)
        show_hand_deck(c_gsfhd, comp_hand)
        show_hand_deck(p_gsfhd, player_hand)
        print("The length of computer deck is ", len(comp_hand))
    else:
        pest = len(p_count) / 2
        pest = int(pest)
        cest = len(c_count) / 2
        cest = int(cest)
        print("Player pair count is ", str(pest), " and computer pair count is ", str(cest))
        if pest > cest:
            print("Player wins!!!!! Yey!!! > - ")
        else:
            print("Computer wins. You lose!!! - - ")



MBRFI()