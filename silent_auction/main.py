from replit import clear
from art import logo

print(logo)

bids = {}
run_bids = True


def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bid}")


while run_bids:
    name = input("What is your name?\n")
    bid_price = int(input("What is your bid?\n$"))

    bids[name] = bid_price

    next_price = (input("Are there any other bidders? yes or no\n")).lower()
    if next_price == "no":
        run_bids = False
        highest_bidder(bids)
    elif run_bids == "yes":
        clear()
