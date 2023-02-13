bids = {}


bid_over = False
while not bid_over:
    print("Welcome to the secret auction program.\n")
    bidder_name = input("What is your name?:\n")
    bid_amount = input("What's your bid?:\n$")
    bids[bidder_name] = bid_amount
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
    if continue_auction == "yes":
        print("\n"*100)
    if continue_auction == "no":
        bid_over = True
max_bid = max(bids.values())
max_bidder = max(bids, key=bids.get)
print(f"The highest bidder is {max_bidder} with a bid of ${max_bid}")
