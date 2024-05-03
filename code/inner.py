from random import choice
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
            value_exists, value_name = check_stuff(get_value_names, v)
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


def counter(dict):
    x = 0
    for key in dict:
        for value in dict[key]:
            if value in ["king", "queen", "joker"]:
                x += 10
            else:
                x += int(value)
    if x < 21:
        return "win"
    elif x == 21:
        return "blackjack"
    else:
        return "lose"


def random_card_picker():
    return choice(cdb.all_suits_list()), choice(cdb.all_cards_list())


def hit():
    score = 0
    suit, value = random_card_picker()
    if value in ["king", "queen", "joker"]:
        score += 10
    else:
        score += int(value)
    return score, suit, value


def dealer_cards():
    x = {}
    total_score = 0
    while total_score < 17:
        score, suit, value = hit()
        if suit not in x:
            x[suit] = []
        x[suit].append(value)
        total_score += score

    return x


def player_card():
    x = {}
    times = 0
    while times < 2:
        _, suit, value = hit()
        if suit not in x:
            x[suit] = []
        x[suit].append(value)
        times += 1

    return x


if __name__ == "__main__":
    for _ in range(100):
        # x = dealer_cards()
        y = player_card()
        print(y)
        # print(counter(x))
