def time24hrto12hr(time):
    split = time.split(":")
    new = int(split[0])
    if new > 12:
        hr = new - 12
        hr = str(hr)
    else:
        hr = split[0]
    if new in range(0, 13) or int(split[0]) == 24:
        date = "AM"
    else:
        date = "PM"
    Full_Time = hr + ":" + split[1] + " " + date 
    return Full_Time

print(time24hrto12hr("23:24"))
