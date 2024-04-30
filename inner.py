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
        except ValueError:
            card_suit = card
        check_item(suits, card)
        
def check_item(dict, i):
    i = i.strip()
    for key in dict:
        if i in dict[key]:       
            exists = True     
    if exists == True:    
        return exists

def main():
    print(card_checker(input("what ")))

if __name__ == "__main__":
    main()