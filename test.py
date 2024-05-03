import card_database as cdb

get_suit_names, get_value_names = cdb.cards()
s, v = input().strip().split("-")

x = {}

def check_stuff(dict_that_has_lists_as_values, value_thats_in_list):
    for dict_keys in dict_that_has_lists_as_values:
        for dict_value in dict_that_has_lists_as_values[dict_keys]:
            if value_thats_in_list == dict_value:
                return dict_keys

suit_name = check_stuff(get_suit_names, s)
value_name = int(check_stuff(get_value_names, v))

x[suit_name] = value_name

print(x)