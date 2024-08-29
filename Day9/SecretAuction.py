from auction_art import draw

print(draw)
continue_bidding = True
bids = {}
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bids == "no":
        continue_bidding = False
    else:
        print("\n" * 100)

print(f"The winner is {max(bids)} with a bid of { max(bids.values())}.")