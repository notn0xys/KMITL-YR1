class Time:
    def __init__(self,hr=0,minutes=0,sec=0):
        self.__hr = hr
        self.__minu = minutes
        self.__sec = sec
    def print(self):
        print(f"{self.__hr:02}:{self.__minu:02}:{self.__sec:02} Hrs.")
time1 = Time(9,30,0)
time1.print()

        