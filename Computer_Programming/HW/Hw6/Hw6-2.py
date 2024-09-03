from turtle import *
def go_back(l,h):
    backward(l * 7)
    right(90)
    forward(h)
    left(90)
def draw_box(l,h):
    for j in range(2):
        forward(l)
        left(90)
        forward(h)
        left(90)

def calendar_of_2024(n):
    if n > 12:
        print("Invalid Month")
        return "invalid Month"
    mo_dates = [31,29,31,30,31,30,31,31,30,31,30,31]
    tracker = 1
    start_date = [0,3,4,0,2,5,0,3,6,1,4,6]
    dates = ["Mo", "Tu", "W", "Th", "Fr", "Sa","Su"]
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", " December"]
    display_month = months[n-1] + " 2024"
    l = 30
    h = 20
    if n == 9 or n == 12:
        row = 8
    else:
        row = 7
    for i in range(row):
        if i == 0:
            for k in range(2):
                forward(l * 7)
                left(90)
                forward(h)
                left(90)
            print(len(display_month))
            forward((l * 7/2) - (len(display_month)* 2) -5 )
            write(display_month)
            backward((l * 7/2) - (len(display_month) * 2) -5)
            right(90)
            forward(h)
            left(90)
        elif i == 1:
            for k in range(7):
                draw_box(l,h)
                forward(l/4)
                write(dates[k])
                forward(3*l / 4)
            go_back(l,h)
        elif i == 2:
            for k in range(7):
                draw_box(l,h)
                forward(l/4)
                if k >= start_date[n-1]:
                    write(tracker)
                    tracker += 1
                forward(3*l / 4)
            go_back(l,h)
        else:
            for k in range(7):
                draw_box(l,h)
                forward(l/4)
                if tracker <= mo_dates[n-1]:
                    write(tracker)
                    tracker += 1
                forward(3*l / 4)
            if i != row - 1:
                go_back(l,h)
            else:
                backward(l*7)
    return None
speed("fastest")
calendar_of_2024(8)
done()