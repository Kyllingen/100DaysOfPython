import blackjack_art
import random

logo = blackjack_art.logo

#Blackjack house rules
#Cards, don't need to worry about suites and we assume
#that the deck is infinite, so we don't need to remove cards
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def drawCard():
    '''Draw a card from the deck'''
    return random.choice(cards)


def showResult(playerSum, computerSum):
    '''Show the result of the game'''
    
    if playerSum == -1:
        print("Blackjack! You win")
    elif computerSum == -1:
        print("Computer has Blackjack! You lose")
    elif playerSum > 21:
        print("Bust! You lose")
    elif computerSum > 21:
        print("Computer bust! You win")
    elif playerSum >= computerSum:
        print("You win")
    else:
        print("You lose")
        
def playAgain():
    '''Ask the player if they want to play again'''
    
    playAgain = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if playAgain == 'y':
        return True
        
    return False

def playerTurn(playerHand):
    '''Player's turn. Keep drawing cards until the player decides to pass or goes over 21'''
    keepDrawing = True
    
    while keepDrawing:
        draw = input("Type 'y' to get another card, 'n' to pass: ")
        if draw == 'y':
            playerHand.append(drawCard())
            
            if sum(playerHand) == 21 and playerHand.len() == 2:
                return -1
            elif sum(playerHand) > 21:
                
                # if player has an Ace and the total is over 21, change the value of the Ace to 1
                if 11 in playerHand:
                    playerHand[playerHand.index(11)] = 1
                else:
                    keepDrawing = False
        else:
            keepDrawing = False
        print(f"Your current hand: {playerHand}")
        
    return sum(playerHand)
            
def computerTurn(computerHand):
    '''Computer's turn. Keep drawing cards until the total is 17 or more'''
    
    while sum(computerHand) < 17:
        computerHand.append(drawCard())
        
        if sum(computerHand) > 21:
            if 11 in computerHand:
                    computerHand[computerHand.index(11)] = 1
            else:
                break
    
    print(f"Computer hand: {computerHand}")        
    return sum(computerHand)

def newGame():
    '''Start a new game of Blackjack'''
    playerHand = []
    computerHand = []
    
    #deal two cards to each player and print the first card of the computer
    for i in range(2):
        playerHand.append(drawCard())
        computerHand.append(drawCard())
        
    print(f"Your cards {playerHand}")
    print(f"Computer first card: {computerHand[0]}")
    
    #Player's turn if not already blackjack.
    #  Stop if the player goes over 21
    if sum(playerHand) == 21:
        playerSum = -1
    else:
        playerSum = playerTurn(playerHand)
    
    #Computer's turn if player didn't bust or got Blackjack
    # Computer must draw cards until the total is 17 or more
    if playerSum != -1 and playerSum <= 21:
        computerSum = computerTurn(computerHand)
    else:
        computerSum = sum(computerHand)
        
    showResult(playerSum, computerSum)

print(logo)
while playAgain():
    newGame()