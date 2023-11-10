# Write code here to identify the name of each card.
def draw(num):
    while 0 < num < 14:
        if num == 1:
            return "Drew an Ace"
        elif 2 <= num <=10 and num != 8:
            return "Drew a " + str(num)
        elif num == 8:
            return "Drew an 8"
        elif num == 11:
            return "Drew a Jack"
        elif num == 12:
            return "Drew a Queen"
        else:
            return "Drew a King"
    return "BAD CARD"  