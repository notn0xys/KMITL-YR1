meow = input("Enter file name: ")
f = None
try:
    f = open(meow, "r")
except:
    print("file not found gg")
    quit()
old = input("Enter String to be replaced: ").strip()
new = input("Enter a new word: ").strip()
nyan = f.read()
if old == new:
    try:
        raise ValueError
    except:
        print("Cant be the same baka")
        quit()
if old not in nyan:
    try:
        raise ValueError
    except:
        print("Not a word in the file")
else:
    nyan = nyan.replace(old,new)
    f.close()
    f = open(meow, "w")
    f.write(nyan)
    f.close()
    print("Done")
