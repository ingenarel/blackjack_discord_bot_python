from card_database import cards
def card_checker(i):
    suits, values = cards()
    i = i.strip().split(" ")            # removes whitespaces from left and right and then splits the given string based on whitespaces.
    x = {}                              # makes an empty dictionary called x
    for card in i:
        try:
            card_suit, card_value = card.strip().split("-")
        except ValueError:
            card_suit = card
        check_item()
        
def check_item(list, i):
    i = i.strip()
    for key in list:
        if i in list:       
            return True

def main():
    print(card_checker(input("what ")))

if __name__ == "__main__":
    main()