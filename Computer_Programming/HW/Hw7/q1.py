class Clock:
    def __init__(self):
        self.__h = 0
        self.__mins = 0
        self.__s = 0
    def set_time(self,time):
        time_split = time.split(":")
        while True:
            if len(time_split) == 3:
                break
            time_split.append("0")
        self.__h = int(time_split[0])
        self.__mins = int(time_split[1])
        self.__s = int(time_split[2])
    def get_time(self):
        return(f"{self.__h:02}:{self.__mins:02}:{self.__s:02}")
    def tick(self):
        self.__s += 1
    def display_12hr(self):
        after = ""
        if int(self.__h) >= 12:
            after = "PM"
            if self.__h != 12:
                self.__h -= 12
        else:
            after = "AM"
        print(f"{self.__h:02}:{self.__mins:02}:{self.__s:02} {after}")
clock = Clock()
clock.set_time("23:04")
print(clock.get_time())
clock.display_12hr()
