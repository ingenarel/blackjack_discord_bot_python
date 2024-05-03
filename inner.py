import card_database as cdb

def card_checker(i):
    suit_list = cdb.all_suits_list()
    values_list = cdb.all_values_list()
    get_suit_names, get_value_names = cdb.cards()
    i = i.strip().split(" ")            # removes whitespaces from left and right and then splits the given string based on whitespaces.
    x = {}                              # makes an empty dictionary called x
    for card in i:
        try:
            for suits in get_suit_names:
                for suit in get_suit_names[suits]:
                    if i == suit:
                        
                    # else:
                    #     print("no")
                
        except ValueError:
            card_suit = card
            if card_suit in suit_list:

                return "yes-ValueWasNotGiven"
            else:
                return "no-ValueWasNotGiven"
                # pass
            
def check_item(list, i):
    i = i.strip()
    if i in list:       
        return True

def main():
    print(card_checker(input("what ")))

if __name__ == "__main__":
    main()