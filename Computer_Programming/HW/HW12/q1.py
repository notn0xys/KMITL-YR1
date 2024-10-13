def textese(s:str,ref:dict):
    keys = list(ref.keys())
    reverse = keys[::-1]
    for i in reverse:
        s = s.replace(i, ref[i])
    return s
def untextese(s:str,ref:dict):
    list_of_vals = list(ref.values())
    list_of_keys = list(ref.keys())
    list_of_keys = list_of_keys[::-1]
    list_of_vals = list_of_vals[::-1]
    string_list = s.split()
    for i in range(len(string_list)):
        try:
            position = list_of_vals.index(string_list[i])
            string_list[i] = list_of_keys[position]
        except:
            continue
    e = " ".join(string_list)
    return e
abbreviations = {
    "be": "b",
    "because": "cuz",
    "see": "c",
    "the": "da",
    "okay": "ok",
    "are": "r",
    "you": "u",
    "without": "w/o",
    "why": "y",
    "see you": "cu",
    "ate": "8",
    "great": "gr8",
    "mate": "m8",
    "wait": "w8",
    "later": "l8r",
    "tomorrow": "2mro",
    "for": "4",
    "before": "b4",
    "once": "1ce",
    "and": "&",
    "Your": "ur",
    "You're": "ur",
    "As far as I know": "afaik",
    "As soon as possible": "ASAP",
    "At the moment": "atm",
    "Be right back": "brb",
    "By the way": "btw",
    "For your information": "FYI",
    "In my humble opinion": "imho",
    "In my opinion": "imo",
    "Laughing out loud": "lol",
    "Oh my god": "omg",
    "Rolling on the floor laughing": "rofl",
    "Talk to you later": "ttyl"
}
s = "be As far as I know By the way gyaaat Talk to you later"
l = textese(s,abbreviations)
print(l)
l = untextese(l,abbreviations)
print(l)