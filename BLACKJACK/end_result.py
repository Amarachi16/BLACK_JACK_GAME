# Write code here to print out the game outcome given a hand value.
def blackjack_or_bust(hand_value):

        if 4 <= hand_value < 21:
            return None
        elif hand_value == 21:
            return "BLACKJACK!"
        elif 21 < hand_value <= 31:
            return "BUST."
        else:
            return "BAD HAND VALUE!"