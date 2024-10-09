import time
class Clock():
    def __init__(self,h = 0,m = 0 ,s = 0) -> None:
        self.setTime(h,m,s)
    def setTime(self,h = 0, m = 0, s = 0):
        if h > 24 or h < 0 or m > 61 or m < 0 or s < 0 or s > 61:
            print("Invalid input setting to deafult time 00:00:00")
            self.h = 0
            self.m = 0
            self.s = 0
        else:
            self.h = h
            self.m = m
            self.s = s
    def recalc(self):
        if self.s > 59:
            self.s = 0
            self.m += 1
        if self.m > 59:
            self.m = 0
            self.h += 1
        if self.h > 23:
            self.h = 0
    def run(self):
        while True:
            print(f"{self.h:02d}:{self.m:02d}:{self.s:02d}")
            time.sleep(1)
            self.s += 1
            self.recalc()
class AlarmClock(Clock):
    def __init__(self, h=0, m=0, s=0) -> None:
        super().__init__(h, m, s)
    def setAlarmtime(self,h = 0 ,m = 0, s = 0):
        if h > 24 or h < 0 or m > 61 or m < 0 or s < 0 or s > 61:
            print("Invalid input")
        else:
            self.ahh = h
            self.amm = m
            self.ass = s
            self.state = False
    def alarm_on(self):
        self.state = True
    def alarm_off(self):
        self.state = False
    def run(self):
        while True:
            print(f"{self.h:02d}:{self.m:02d}:{self.s:02d}")
            if self.state == True and self.ahh == self.h and self.amm == self.m and self.ass == self.s:
                print("timer reached")
                break
            time.sleep(1)
            self.s += 1
            self.recalc()

b = AlarmClock(12,23,5)
b.setAlarmtime(12,23,10)
b.alarm_on()
b.run()