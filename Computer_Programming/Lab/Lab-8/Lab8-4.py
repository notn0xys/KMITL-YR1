first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()
gender = ""
while True:
    gender = input("Enter your gender(m/f)")
    print(gender)
    if gender.lower() == "m" or gender.lower() == "f":
        break
    else:
        print("Try agian")
        continue

password = gender + last[:0]
if len(first) < 6:
    password += first
else:
    password += first[:6]

print(f"Your username: {password.upper()}")
