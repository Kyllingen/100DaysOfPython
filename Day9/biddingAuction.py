import os
import biddingAuction_art

bidders = {}
bidding = True

#clear screen in console
def clear():
    os.system("cls" if os.name == 'nt' else "clear")
    
def addBidder():
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    
    bidders[name] = bid
    
def showHighestBidder():
    highestBid = 0
    highestBidder = ""
    
    for bidder in bidders:
        if bidders[bidder] > highestBid:
            highestBid = bidders[bidder]
            highestBidder = bidder
    
    print(f"The winner is {highestBidder} with a bid of ${highestBid}.\n\n")
    
#Main Logic
print(biddingAuction_art.logo)
print("Welcome to the secret auction program\n\n")
    
while bidding:
    addBidder()
    
    moreBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")   
    if moreBidders != "yes":
        bidding = False
    
    clear()

showHighestBidder()