print("Please enter a time in 24hr format")
hr = int(input("HR: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
after = ""
if hr >= 12 and hr != 24:
    after = "PM"
    if hr == 12:
        hr = 12
    else:
        hr -= 12
elif hr == 24:
    after = "AM"
    hr = 0
else:
    after = "AM"
if hr < 10:
    hr = "0" + str(hr)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)

print(f"The time you just entered in 12 hour format is {hr}:{minutes}:{seconds} {after} ")