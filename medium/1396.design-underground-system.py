from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.duration = defaultdict(int)
        self.counter = defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin:
            stationNameFrom, tFrom = self.checkin[id]
            key = (stationNameFrom, stationName)
            self.duration[key] += t - tFrom
            self.counter[key] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.duration[key] / self.counter[key]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)