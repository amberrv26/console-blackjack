import random
import time

deck_values = []
t = 0.7
betting_mode = False
money = 5000

def values(deck, i):
    if deck[i][0] == "A": #Automatically sets the Ace value to 11
        deck_values.append(11)
    elif (deck[i][0] == "1") or (deck[i][0] == "J") or (deck[i][0] == "Q") or (deck[i][0] == "K") : #Automatically sets all picture card values to 10, as well as the 10 card itself
        deck_values.append(10)
    else:
        deck_values.append(int(deck[i][0])) #If the card is values 2-9, simply turns that value into an integer for calculations before appending it to the deck_values array

def player_turn(player, player_vals, player_total, game_finished, deck): #Player's turn
    choice = ''
    again = True
    if player_total != 21: #If the player is lucky enough to start on 21, automatically goes to dealer's turn
        while again == True:
            while ((choice != "s") and (choice != "t")):
                time.sleep(t)
                choice = input("Stick or twist? (s/t) ").lower()
                print()
            if choice == "t":
                if deck_values[0] == 11:
                    if (player_total + deck_values[0]) > 21: #Determines if the Ace value should be changed to 1 - i.e if the player has an Ace and a 7, then draws a 6, sets total to 14 rather than 24
                        deck_values[0] = 1
                player.append(deck[0])
                deck.remove(deck[0])
                player_vals.append(deck_values[0])
                player_total += deck_values[0]
                deck_values.remove(deck_values[0])
                time.sleep(t)
                print(f"New card: {player[len(player)-1]}. New total: {player_total}.\n")
                choice = ''
                if player_total > 21:
                    time.sleep(t)
                    print("You went bust!\n") #Turn automatically ends if the player goes bust (over 21) or if they reach 21 exactly
                    again = False
                elif player_total == 21:
                    again = False
                else:
                    again = True
            elif choice == "s":
                again = False
    return player_total

def dealer_turn(dealer, dealer_vals, dealer_total, player_total, deck):
    time.sleep(t)
    if "Ace" in dealer[0] and "Ace" in dealer[1]: #while loop won't run if the dealer has 2 Aces due to 11 as the default
        dealer_total = 2
    print(f"Dealer's hand: {dealer[0]} and {dealer[1]}. Value is {dealer_total}.\n") #On the dealer's turn, you see the other card they were holding
    while (dealer_total < 17) and (player_total <= 21) and (dealer_total < player_total): #Per the rules of blackjack, the dealer must take cads until their total is 17 or more
        time.sleep(t)
        if deck_values[0] == 11:
            if (dealer_total + deck_values[0]) > 21:
                deck_values[0] = 1
        dealer.append(deck[0])
        deck.remove(deck[0])
        dealer_vals.append(deck_values[0])
        dealer_total += deck_values[0]
        deck_values.remove(deck_values[0])
        time.sleep(t)
        print(f"Dealer drew: {dealer[len(dealer)-1]}. Dealer's new total: {dealer_total}.\n")

    if dealer_total > 21:
        time.sleep(t)
        print("The dealer went bust!\n")
    else:
        time.sleep(t)
        print("The dealer sticks!\n")

    return dealer_total

def calculate_money(bet, money, winner): #Money is sometimes global, sometimes parameter, but it is the same variable
    if winner == "d":
        print(f"You lost £{bet}!\n")
    elif winner == "n":
        print(f"You won £{bet}! You made your money back.\n")
        money += bet
    elif winner == "p":
        prize = bet * 2
        print(f"You won £{prize}!\n")
        money += prize
    return money
    

def results(dealer_total, player_total, betting_mode, bet):
    global money
    winner = ""
    if ((dealer_total > player_total) and (dealer_total <= 21)) or (player_total > 21): #Lose conditions: dealer has a higher total, or player went bust (over 21)
        time.sleep(t)
        print("Dealer wins.\n")
        winner = "d"
    elif dealer_total == player_total: #Tie condition: the totals are equal
        time.sleep(t)
        print("It's a tie!\n")
        winner = "n"
    else: #Win conditions: player has a higher total than dealer, or dealer went bust
        time.sleep(t)
        print("Player wins!\n")
        winner = "p"

    if betting_mode == True:
        money = calculate_money(bet, money, winner)

    menu(betting_mode)

def game(dealer, player, dealer_vals, player_vals, dealer_total, player_total, betting_mode, bet, deck):
    game_finished = False
    while game_finished == False:
        player_total = player_turn(player, player_vals, player_total, game_finished, deck) #Player always goes first
        dealer_total = dealer_turn(dealer, dealer_vals, dealer_total, player_total, deck)
        game_finished = True
    results(dealer_total, player_total, betting_mode, bet)
    
def deal(betting_mode, bet, deck):
    dealer = []
    player = []
    dealer_vals = []
    player_vals = []
    dealer_total = 0
    player_total = 0
    for i in range(0, 2): #Gives both the player and dealer two cards
        dealer.append(deck[0])
        dealer_vals.append(deck_values[0])
        deck.remove(deck[0])
        deck_values.remove(deck_values[0])
        player.append(deck[0])
        player_vals.append(deck_values[0])
        deck.remove(deck[0])
        deck_values.remove(deck_values[0])

    dealer_total = dealer_vals[0] + dealer_vals[1]
    time.sleep(t)
    print(f"Dealer's hand: {dealer[0]}. Value is {dealer_vals[0]}.\n") #Even though both dealer and player have two cards, player should only be aware of one card
    player_total = player_vals[0] + player_vals[1]
    time.sleep(t)
    print(f"Your have: {player[0]} and {player[1]}. Value is {player_total}.\n")
    game(dealer, player, dealer_vals, player_vals, dealer_total, player_total, betting_mode, bet, deck)

def place_bet(bet):
    global money
    game_over = False
    time.sleep(t)
    print(f"You have £{money}.\n")
    if money < 5:
        time.sleep(t)
        game_over = True
    else:
        while (bet < 5) or (bet > money):
            time.sleep(t)
            try:
                bet = int(input("How much will you bet? \n"))
            except ValueError:
                print("Invalid value.\n")
            if bet > money:
                time.sleep(t)
                print("You cannot afford that.\n")
            elif bet < 5:
                time.sleep(t)
                print("Must bet at least £5 in money.\n")
        money -= bet
    print(f"You have bet £{bet}. You currently have £{money}.")
    return bet, game_over

def shuffle_deck(betting_mode, cards):
    global deck_values
    bet = 0
    deck = []
    deck_values = []
    for i in range(0, 52): #Shuffle the cards
        random_suit = random.randint(0, len(cards)-1)
        while len(cards[random_suit]) == 0:
            random_suit = random.randint(0, len(cards)-1)
        random_val = random.randint(0, len(cards[random_suit])-1)
        deck.append(cards[random_suit][random_val])
        values(deck, i)
        cards[random_suit].pop(random_val)

    if betting_mode == True:
        bet, game_over = place_bet(bet)
        if game_over:
            print("You cannot bet anymore. Game over.")
        elif bet >= 5:
            deal(betting_mode, bet, deck)
    else:
        deal(betting_mode, bet, deck)

def create_deck():
    cards = []
    hearts = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    clubs = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    diamonds = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    spades = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    for i in range(0, len(hearts)): #Create the deck
        hearts[i] += " of Hearts"
        clubs[i] += " of Clubs"
        diamonds[i] += " of Diamonds"
        spades[i] += " of Spades"
    cards.append(hearts)
    cards.append(clubs)
    cards.append(diamonds)
    cards.append(spades)
    return cards

def settings():
    choice = ''
    betting_mode = False
    while (choice != "y") and (choice != "n"):
        choice = input("Enable betting mode? (y/n) ")
        print()

    if choice == "y":
        print("Betting mode enabled.\n")
        betting_mode = True
    return betting_mode
        
def menu(betting_mode): #Player menu
    choice = ''
    while (choice != "y") and (choice != "n"):
        choice = input("Play blackjack? (y/n) ").lower()
        print()

    if choice == "y":
        cards = create_deck()
        shuffle_deck(betting_mode, cards)
    elif choice == "n":
        time.sleep(t)
        print("Goodbye.\n")
        if betting_mode:
            if (money - 5000) < 0:
                print(f"You finished with £{money}. You lost £{5000-money}.")
            elif money == 5000:
                print(f"You finished with £{money}. You broke even.")
            else:
                print(f"You finished with £{money}. You won £{money-5000}.")

if __name__ == "__main__":
    betting_mode = settings()
    menu(betting_mode)
