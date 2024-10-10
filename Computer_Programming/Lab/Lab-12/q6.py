from abc import ABC
class Transport(ABC):
    def __init__(self,start = "",end = "", distance = 0) -> None:
        super().__init__()
        self.start = start
        self.end = end
        self.distance = distance
    def get_amount(self):
        pass
class Walk(Transport):
    def __init__(self, start="", end="", distance=0) -> None:
        super().__init__(start, end, distance)
        self.perkm = 0
    def get_amount(self):
        return self.perkm * self.distance
class Taxi(Transport):
    def __init__(self, start="", end="", distance=0) -> None:
        super().__init__(start, end, distance)
        self.perkm = 40
    def get_amount(self):
        return self.perkm * self.distance
class Train(Transport):
    def __init__(self, start="", end="", distance=0,station = 1) -> None:
        super().__init__(start, end, distance)
        self.station = station
    def get_amount(self):
        return self.station * 5