from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    c_bid = bidding_record[bidder]
    if c_bid > highest_bid:
      highest_bid = c_bid
      winner = bidder
  clear()
  print(logo)
  print(f"The winner is {winner}, with a bid of €{highest_bid}!")


while bidding_finished == False:
  name = input("What is your name?\n")
  bid = int(input("How much do you bid?\n€"))
  bids[name] = bid
  again = input("Is there another bidder?\n").lower()
  if again == "yes":
    clear()
    print(logo)
  else:
    bidding_finished = True
    highest_bidder(bids)
    
  



