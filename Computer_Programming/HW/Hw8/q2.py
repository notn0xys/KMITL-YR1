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
print(character)
print(meow)
for i in meow:
    print(f"Letter {i} percent {meow[i]/adjusted_length:.2%}")