from random import choice
import card_database as cdb

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
