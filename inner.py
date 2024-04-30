def card_checker(i):
    suits = {
            "c": ["c", "club", "clbu", "clib", 
                "ckub", "clu", "cllub", "vlub", 
                "ciub", "xlub", "cpub", "cluh", 
                "cliv", "clun", "clubb", "clubs", 
                "clbus", "clubz", "clusb", "clb", 
                "cuub",
                ],
            "d": ["d", "diamond", "diamod", "diamomd", 
                "diamons", "diomond", "daimond", "diamonds", 
                "diaminds", "diamon", "diamobd", "diamojd", 
                "dimond", "diomand", "diamonf", "diamnond", 
                "diamondd", "diamomds", "diamknd", "diamnod", 
                "diampnd",
                ],
            "h": ["h", "heart", "heary", "hearrt", 
                "hear", "hearts", "heats", "hert", 
                "hearts", "hearr", "heartr", "heartt", 
                "hert", "hearst", "hearty", "hearrts", 
                "heartsa", "harts", "hearat", "hearth", 
                "heartsy",
                ],
            "s": ["s", "spade", "spad", "spae", 
                "spadde", "spaee", "spades", "spadds", 
                "spadse", "spadess", "spadesa", "spadex", 
                "spadec", "psade", "spdaes", "soade", 
                "spaed", "spadea", "spadse", "spadew", 
                "soades",
                ],
            }
    values = {
             1 : ["1", "one",
                 ],
             2 : ["2", "two",
                 ],
             3 : ["3", "three",
                 ],
             4 : ["4", "four",
                 ],
             5 : ["5", "five",
                 ],
             6 : ["6", "six",
                 ],
             7 : ["7", "seven",
                 ],
             8 : ["8", "eight",
                 ],
             9 : ["9", "nine",
                 ],
             10: ["10", "ten", "king", "queen", "joker",
                 ],
             }
    i = i.strip().split(" ")            # removes whitespaces from left and right and then splits the given string based on whitespaces.
    x = {}                              # makes an empty dictionary called x
    
    for card in i:                      # for every card in the splitted given string,
        for types in suits:             # it goes over every types of suits. c, d, h and s
            if card in suits[types]:    # and if the card is in in the the list of words in a suit, does the following stuff:
                if types in x:          # if a type of card already exists in the empty dictionary called x
                    x[types] += 1       # it adds a plus one value to it
                else:                   # and if the card doesn't exist on the x dictionary yet,
                    x[types] = 1        # it enters it in the dictionary, and sets the value to 1
    
    return x

print(card_checker(input("what ")))