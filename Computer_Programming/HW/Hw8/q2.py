character = input("Enter character: ").strip()
meow = dict()
for i in character:
    if i in meow:
        meow[i] += 1
    else:
        meow[i] = 1
if " " in meow:
  del meow[" "]
adjusted_length = len(character.replace(" ", ""))
for i in meow:
    print(f"Char {i} percent {meow[i]/adjusted_length:.2%}")