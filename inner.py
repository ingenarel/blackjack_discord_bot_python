def card_checker(i):
    suits = {"c": ["c", "club", "clbu", "clib", 
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
    x = 0
    i = i.split(" ")
    for card in i:
        for types in suits:
            if card in suits[types]:
                x += 1
            else:
                x += 0

    if x == 1:
        return "yes"
    elif x == 0:
        return "no"
    elif x > 1:
        return "multiple"
    else:
        print("error")

print(card_checker(input("what ")))