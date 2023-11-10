# Use randint to generate random cards. 
from random import randint
from end_result import blackjack_or_bust
from card_value import card_value
from card_name import draw
# Write all of your part 2B code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_human_turn():
  a = randint(1,13)
  b = randint(1,13)
  print(draw(a))
  print(draw(b))
  hv = card_value(a) + card_value(b)
  
  bingo = True
  while hv < 21:

    c = input(f"You have {hv}. Hit (y/n)? ")
    if c == 'y':
      c = randint(1,13)
      print(draw(c))
      hv += card_value(c)
    elif c == 'n':
      print(f"Final hand: {hv}.")
      break
    else:
      print("Sorry I didn't get that.")
      while bingo:
        if c != 'n' and c!='y':
          bingo = False
          
  if hv >= 21:
    print(f"Final hand: {hv}.")
    print(blackjack_or_bust(hv))
play_human_turn()   

 