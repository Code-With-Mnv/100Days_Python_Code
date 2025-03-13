# Author : Manav
# Task : Secret Auction Program

bidding_dict = {}

def add_new_bidder(bidder, bid):
    bidding_dict[bidder] = bid

def find_max_bid():
    max_bid = 0
    max_bidder = ""
    for bidders in bidding_dict:
        if bidding_dict[bidders] > max_bid:
            max_bid = bidding_dict[bidders]
            max_bidder = bidders
    
    print(f"{max_bidder} has won the auction with the maximum bid of {max_bid}$!")

print("Welcome to the Auction!")
print()

while True:
    print()
    ch = input("Is there any bidder (y/n): ")
    print()
    if ch in "Yy":
        bidder = input("Enter the bidder's name: ")
        bid = int(input("Enter the bid amount: $"))
        add_new_bidder(bidder, bid)
        print("Bid added successfully!")
    else:
        find_max_bid()
        print("Thank you!")
        break


