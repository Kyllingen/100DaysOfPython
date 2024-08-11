import blackjack_art
import random

logo = blackjack_art.logo

#Blackjack house rules
#Cards, don't need to worry about suites and we assume
#that the deck is infinite, so we don't need to remove cards
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def draw_card():
    '''Draw a card from the deck'''
    return random.choice(cards)


def show_result(player_sum, computer_sum):
    '''Show the result of the game'''
    
    if player_sum == -1:
        print("Blackjack! You win")
    elif computer_sum == -1:
        print("Computer has Blackjack! You lose")
    elif player_sum > 21:
        print("Bust! You lose")
    elif computer_sum > 21:
        print("Computer bust! You win")
    elif player_sum >= computer_sum:
        print("You win")
    else:
        print("You lose")
        
def play_again():
    '''Ask the player if they want to play again'''
    
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'y':
        return True
        
    return False

def player_turn(player_hand):
    '''Player's turn. Keep drawing cards until the player decides to pass or goes over 21'''
    keep_drawing = True
    
    while keep_drawing:
        draw = input("Type 'y' to get another card, 'n' to pass: ")
        if draw == 'y':
            player_hand.append(draw_card())
            
            if sum(player_hand) == 21 and player_hand.len() == 2:
                return -1
            elif sum(player_hand) > 21:
                
                # if player has an Ace and the total is over 21, change the value of the Ace to 1
                if 11 in player_hand:
                    player_hand[player_hand.index(11)] = 1
                else:
                    keep_drawing = False
        else:
            keep_drawing = False
        print(f"Your current hand: {player_hand}")
        
    return sum(player_hand)
            
def computer_turn(computer_hand):
    '''Computer's turn. Keep drawing cards until the total is 17 or more'''
    
    while sum(computer_hand) < 17:
        computer_hand.append(draw_card())
        
        if sum(computer_hand) > 21:
            if 11 in computer_hand:
                    computer_hand[computer_hand.index(11)] = 1
            else:
                break
    
    print(f"Computer hand: {computer_hand}")        
    return sum(computer_hand)

def new_game():
    '''Start a new game of Blackjack'''
    player_hand = []
    computer_hand = []
    
    #deal two cards to each player and print the first card of the computer
    for i in range(2):
        player_hand.append(draw_card())
        computer_hand.append(draw_card())
        
    print(f"Your cards {player_hand}")
    print(f"Computer first card: {computer_hand[0]}")
    
    #Player's turn if not already blackjack.
    #  Stop if the player goes over 21
    if sum(player_hand) == 21:
        player_sum = -1
    else:
        player_sum = player_turn(player_hand)
    
    #Computer's turn if player didn't bust or got Blackjack
    # Computer must draw cards until the total is 17 or more
    if player_sum != -1 and player_sum <= 21:
        computer_sum = computer_turn(computer_hand)
    else:
        computer_sum = sum(computer_hand)
        
    show_result(player_sum, computer_sum)

print(logo)
while play_again():
    new_game()