def time(x):
    new = x.split(":")
    hr = int(new[0])
    minutes = int(new[1])
    if hr > 23 or minutes > 59:
        return "Invalid hour"
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
        newhr = "0" + str(hr)
    else:
        newhr = str(hr)
    if minutes < 10:
        newminutes = "0" + str(minutes)
    else:
        newminutes = str(minutes)
    total = newhr + ":" + newminutes + " " + after
    return total
print(time("23:24"))