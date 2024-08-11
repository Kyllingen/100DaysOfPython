import os
import bidding_auction_art as bidding_auction_art

bidders = {}
bidding = True

#clear screen in console
def clear():
    os.system("cls" if os.name == 'nt' else "clear")
    
def add_bidder():
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    
    bidders[name] = bid
    
def show_highest_bidder():
    highest_bid = 0
    highest_bidder = ""
    
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            highest_bidder = bidder
    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.\n\n")
    
#Main Logic
print(bidding_auction_art.logo)
print("Welcome to the secret auction program\n\n")
    
while bidding:
    add_bidder()
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")   
    if more_bidders != "yes":
        bidding = False
    
    clear()

show_highest_bidder()