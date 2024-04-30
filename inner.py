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
             "1" : ["1", "one", "ace",
                 ],
             "2" : ["2", "two",
                 ],
             "3" : ["3", "three",
                 ],
             "4" : ["4", "four",
                 ],
             "5" : ["5", "five",
                 ],
             "6" : ["6", "six",
                 ],
             "7" : ["7", "seven",
                 ],
             "8" : ["8", "eight",
                 ],
             "9" : ["9", "nine",
                 ],
             "10": ["10", "ten", "king", "queen", 
                  "joker",
                 ],
             }
    i = i.strip().split(" ")            # removes whitespaces from left and right and then splits the given string based on whitespaces.
    x = {}                              # makes an empty dictionary called x
        
    for card in i:
        try:
            card_suit, card_value = card.strip().split("-")
            for value in values:
                if card_value in values[value]:
                    card_value = int(card_value)
            for suit in suits:
                if card_suit in suits[suit] and card_value in values:
                    if suit in x:          
                        x[suit] += 1       
                    else:                   
                        x[suit] = 1
        except ValueError:
            for suit in suits:
                if card in suits[suit]:
                    if suit in x:          
                        x[suit] += 1       
                    else:                   
                        x[suit] = 1
    return x

def main():
    print(card_checker(input("what ")))

if __name__ == "__main__":
    main()