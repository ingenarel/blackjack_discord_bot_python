def cards():
    suits = {
        "clubs": [
            "c",
            "club",
            "clbu",
            "clib",
            "ckub",
            "clu",
            "cllub",
            "vlub",
            "ciub",
            "xlub",
            "cpub",
            "cluh",
            "cliv",
            "clun",
            "clubb",
            "clubs",
            "clbus",
            "clubz",
            "clusb",
            "clb",
            "cuub",
            "♣",
        ],
        "diamonds": [
            "d",
            "diamond",
            "diamod",
            "diamomd",
            "diamons",
            "diomond",
            "daimond",
            "diamonds",
            "diaminds",
            "diamon",
            "diamobd",
            "diamojd",
            "dimond",
            "diomand",
            "diamonf",
            "diamnond",
            "diamondd",
            "diamomds",
            "diamknd",
            "diamnod",
            "diampnd",
            "💎",
            "♦",
            "🔸",
            "🔹",
            "🔶",
            "🔷",
        ],
        "hearts": [
            "h",
            "heart",
            "heary",
            "hearrt",
            "hear",
            "hearts",
            "heats",
            "hert",
            "hearts",
            "hearr",
            "heartr",
            "heartt",
            "hert",
            "hearst",
            "hearty",
            "hearrts",
            "heartsa",
            "harts",
            "hearat",
            "hearth",
            "heartsy",
            "♥",
            "❤️",
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "💔",
            "💖",
            "💗",
            "💘",
            "💝",
            "💞",
            "💟",
        ],
        "spades": [
            "s",
            "spade",
            "spad",
            "spae",
            "spadde",
            "spaee",
            "spades",
            "spadds",
            "spadse",
            "spadess",
            "spadesa",
            "spadex",
            "spadec",
            "psade",
            "spdaes",
            "soade",
            "spaed",
            "spadea",
            "spadse",
            "spadew",
            "soades",
            "♠",
        ],
    }

    values = {
        "1": [
            "1",
            "one",
            "ne",
            "oe",
            "on",
            "oone",
            "onne",
            "onee",
            "noe",
            "oen",
            "oine",
            "ione",
            "okne",
            "kone",
            "olne",
            "lone",
            "opne",
            "pone",
            "onbe",
            "obne",
            "onhe",
            "ohne",
            "onje",
            "ojne",
            "onme",
            "omne",
            "onew",
            "onwe",
            "ones",
            "onse",
            "oned",
            "onde",
            "oner",
            "ace",
            "ce",
            "ae",
            "ac",
            "aace",
            "acce",
            "acee",
            "cae",
            "aec",
            "aqce",
            "qace",
            "awce",
            "wace",
            "asce",
            "sace",
            "azce",
            "zace",
            "acxe",
            "axce",
            "acde",
            "adce",
            "acfe",
            "afce",
            "acve",
            "avce",
            "acew",
            "acwe",
            "aces",
            "acse",
            "aced",
            "acer",
            "1️⃣",
        ],
        "2": [
            "2",
            "two",
            "wo",
            "to",
            "tw",
            "ttwo",
            "twwo",
            "twoo",
            "wto",
            "tow",
            "trwo",
            "rtwo",
            "tfwo",
            "ftwo",
            "tgwo",
            "gtwo",
            "tywo",
            "ytwo",
            "twqo",
            "tqwo",
            "twao",
            "tawo",
            "twso",
            "tswo",
            "tweo",
            "tewo",
            "twoi",
            "twio",
            "twok",
            "twko",
            "twol",
            "twlo",
            "twop",
            "2️⃣",
        ],
        "3": [
            "3",
            "three",
            "hree",
            "tree",
            "thee",
            "thre",
            "tthree",
            "thhree",
            "thrree",
            "threee",
            "htree",
            "trhee",
            "there",
            "trhree",
            "rthree",
            "tfhree",
            "fthree",
            "tghree",
            "gthree",
            "tyhree",
            "ythree",
            "thgree",
            "thbree",
            "tbhree",
            "thnree",
            "tnhree",
            "thjree",
            "tjhree",
            "thuree",
            "tuhree",
            "thyree",
            "theree",
            "thrdee",
            "thdree",
            "thrfee",
            "thfree",
            "thrtee",
            "thtree",
            "threwe",
            "thrwee",
            "threse",
            "thrsee",
            "threde",
            "threre",
            "threew",
            "threes",
            "threed",
            "3️⃣",
        ],
        "4": [
            "4",
            "four",
            "our",
            "fur",
            "for",
            "fou",
            "ffour",
            "foour",
            "fouur",
            "fourr",
            "ofur",
            "fuor",
            "foru",
            "fdour",
            "dfour",
            "frour",
            "rfour",
            "ftour",
            "tfour",
            "fgour",
            "gfour",
            "fvour",
            "vfour",
            "fcour",
            "cfour",
            "foiur",
            "fiour",
            "fokur",
            "fkour",
            "folur",
            "flour",
            "fopur",
            "fpour",
            "fouyr",
            "foyur",
            "fouhr",
            "fohur",
            "foujr",
            "fojur",
            "fouir",
            "foure",
            "fouer",
            "fourd",
            "foudr",
            "fourf",
            "foufr",
            "fourt",
            "4️⃣",
        ],
        "5": [
            "5",
            "five",
            "ive",
            "fve",
            "fie",
            "fiv",
            "ffive",
            "fiive",
            "fivve",
            "fivee",
            "ifve",
            "fvie",
            "fiev",
            "fdive",
            "dfive",
            "frive",
            "rfive",
            "ftive",
            "tfive",
            "fgive",
            "gfive",
            "fvive",
            "vfive",
            "fcive",
            "cfive",
            "fiuve",
            "fuive",
            "fijve",
            "fjive",
            "fikve",
            "fkive",
            "fiove",
            "foive",
            "fivce",
            "ficve",
            "fivfe",
            "fifve",
            "fivge",
            "figve",
            "fivbe",
            "fibve",
            "fivew",
            "fivwe",
            "fives",
            "fivse",
            "fived",
            "fivde",
            "fiver",
            "5️⃣",
        ],
        "6": [
            "6",
            "six",
            "ix",
            "sx",
            "si",
            "ssix",
            "siix",
            "sixx",
            "isx",
            "sxi",
            "swix",
            "wsix",
            "saix",
            "asix",
            "szix",
            "zsix",
            "sxix",
            "xsix",
            "sdix",
            "dsix",
            "seix",
            "esix",
            "siux",
            "suix",
            "sijx",
            "sjix",
            "sikx",
            "skix",
            "siox",
            "soix",
            "sixz",
            "sizx",
            "sixs",
            "sisx",
            "sixd",
            "sidx",
            "sixc",
            "6️⃣",
        ],
        "7": [
            "7",
            "seven",
            "even",
            "sven",
            "seen",
            "sevn",
            "seve",
            "sseven",
            "seeven",
            "sevven",
            "seveen",
            "sevenn",
            "esven",
            "sveen",
            "seevn",
            "sevne",
            "sweven",
            "wseven",
            "saeven",
            "aseven",
            "szeven",
            "zseven",
            "sxeven",
            "xseven",
            "sdeven",
            "dseven",
            "eseven",
            "sewven",
            "sesven",
            "sedven",
            "serven",
            "sreven",
            "sevcen",
            "secven",
            "sevfen",
            "sefven",
            "sevgen",
            "segven",
            "sevben",
            "sebven",
            "sevewn",
            "sevwen",
            "sevesn",
            "sevsen",
            "sevedn",
            "sevden",
            "severn",
            "sevren",
            "sevenb",
            "sevebn",
            "sevenh",
            "sevehn",
            "sevenj",
            "sevejn",
            "sevenm",
            "7️⃣",
        ],
        "8": [
            "8",
            "eight",
            "ight",
            "eght",
            "eiht",
            "eigt",
            "eigh",
            "eeight",
            "eiight",
            "eigght",
            "eighht",
            "eightt",
            "ieght",
            "egiht",
            "eihgt",
            "eigth",
            "ewight",
            "weight",
            "esight",
            "seight",
            "edight",
            "deight",
            "eright",
            "reight",
            "eiught",
            "euight",
            "eijght",
            "ejight",
            "eikght",
            "ekight",
            "eioght",
            "eoight",
            "eigfht",
            "eifght",
            "eigtht",
            "eitght",
            "eigyht",
            "eiyght",
            "eihght",
            "eigbht",
            "eibght",
            "eigvht",
            "eivght",
            "eighgt",
            "eighbt",
            "eighnt",
            "eignht",
            "eighjt",
            "eigjht",
            "eighut",
            "eiguht",
            "eighyt",
            "eightr",
            "eighrt",
            "eightf",
            "eighft",
            "eightg",
            "8️⃣",
        ],
        "9": [
            "9",
            "nine",
            "ine",
            "nne",
            "nie",
            "nin",
            "nnine",
            "niine",
            "ninne",
            "ninee",
            "inne",
            "nnie",
            "nien",
            "nbine",
            "bnine",
            "nhine",
            "hnine",
            "njine",
            "jnine",
            "nmine",
            "mnine",
            "niune",
            "nuine",
            "nijne",
            "nikne",
            "nkine",
            "nione",
            "noine",
            "ninbe",
            "nibne",
            "ninhe",
            "nihne",
            "ninje",
            "ninme",
            "nimne",
            "ninew",
            "ninwe",
            "nines",
            "ninse",
            "nined",
            "ninde",
            "niner",
            "9️⃣",
        ],
        "10": [
            "10",
            "ten",
            "en",
            "tn",
            "te",
            "tten",
            "teen",
            "tenn",
            "etn",
            "tne",
            "tren",
            "rten",
            "tfen",
            "ften",
            "tgen",
            "gten",
            "tyen",
            "yten",
            "tewn",
            "twen",
            "tesn",
            "tsen",
            "tedn",
            "tden",
            "tern",
            "tenb",
            "tebn",
            "tenh",
            "tehn",
            "tenj",
            "tejn",
            "tenm",
            "king",
            "ing",
            "kng",
            "kig",
            "kin",
            "kking",
            "kiing",
            "kinng",
            "kingg",
            "ikng",
            "knig",
            "kign",
            "kming",
            "mking",
            "kjing",
            "jking",
            "iking",
            "koing",
            "oking",
            "kling",
            "lking",
            "kiung",
            "kuing",
            "kijng",
            "kikng",
            "kiong",
            "kinbg",
            "kibng",
            "kinhg",
            "kihng",
            "kinjg",
            "kinmg",
            "kimng",
            "kingf",
            "kinfg",
            "kingt",
            "kintg",
            "kingy",
            "kinyg",
            "kingh",
            "kingb",
            "kingv",
            "queen",
            "ueen",
            "qeen",
            "quen",
            "quee",
            "qqueen",
            "quueen",
            "queeen",
            "queenn",
            "uqeen",
            "qeuen",
            "quene",
            "qaueen",
            "aqueen",
            "qwueen",
            "wqueen",
            "quyeen",
            "qyueen",
            "quheen",
            "qhueen",
            "qujeen",
            "qjueen",
            "quieen",
            "qiueen",
            "quewen",
            "quween",
            "quesen",
            "quseen",
            "queden",
            "qudeen",
            "queren",
            "qureen",
            "queewn",
            "queesn",
            "queedn",
            "queern",
            "queenb",
            "queebn",
            "queenh",
            "queehn",
            "queenj",
            "queejn",
            "queenm",
            "joker",
            "oker",
            "jker",
            "joer",
            "jokr",
            "joke",
            "jjoker",
            "jooker",
            "jokker",
            "jokeer",
            "jokerr",
            "ojker",
            "jkoer",
            "joekr",
            "jokre",
            "jhoker",
            "hjoker",
            "jnoker",
            "njoker",
            "jmoker",
            "mjoker",
            "jkoker",
            "kjoker",
            "jioker",
            "ijoker",
            "juoker",
            "ujoker",
            "joiker",
            "jolker",
            "jloker",
            "jopker",
            "jpoker",
            "jokmer",
            "jomker",
            "jokjer",
            "jojker",
            "jokier",
            "jokoer",
            "jokler",
            "jokewr",
            "jokwer",
            "jokesr",
            "jokser",
            "jokedr",
            "jokder",
            "jokrer",
            "jokere",
            "jokerd",
            "jokerf",
            "jokefr",
            "jokert",
            "🔟",
            "🃏",
            "👑",
        ],
    }
    return suits, values


def all_suits_list():
    x = []
    for suit_types in cards()[0]:
        x.append(suit_types)
    return x


def all_cards_list():
    x = []
    for value_types in cards()[1]:
        x.append(value_types)
    extra = ["king", "queen", "joker"]
    x.extend(extra)
    return x


if __name__ == "__main__":
    print(all_cards_list())