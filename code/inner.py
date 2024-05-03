import card_database as cdb

def card_checker(i):
    get_suit_names, get_value_names = cdb.cards()
    i = i.strip().split(" ")           
    x = {}                  
    for card in i:
        try:
            s, v = card.split("-")
            s, v = s.lower(), v.lower()
            suit_exists, suit_name = check_stuff(get_suit_names, s)
            value_exists, value_name = (check_stuff(get_value_names, v))
            value_name = int(value_name)
            if suit_exists == True and value_exists == True:
                if suit_name in x:
                    x[suit_name] += value_name
                else:
                    x[suit_name] = value_name
        except ValueError:
            s = card
            s = s.lower()
            suit_exists, suit_name = check_stuff(get_suit_names, s)
            if suit_exists:
                if suit_name in x:
                    x[suit_name] += 1
                else:
                    x[suit_name] = 1
    return x

def check_stuff(dict_that_has_lists_as_values, value_thats_in_list):
    for dict_keys in dict_that_has_lists_as_values:
        for dict_value in dict_that_has_lists_as_values[dict_keys]:
            if value_thats_in_list == dict_value:
                return True, dict_keys

            # else:
            #     exists = False
# def counter(i):
    # card_checker(i)

def main():
    print(card_checker(input("What? ")))

if __name__ == "__main__":
    main()