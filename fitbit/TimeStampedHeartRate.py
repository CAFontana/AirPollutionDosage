class TimeStampedHeartRate:
    timestamp = 0
    heartrate = 0
    lat = 0
    long = 0

    def __init__(self, ts, hr, lat, long):
        self.timestamp = ts
        self.heartrate = hr
        self.lat = lat
        self.long = long

    def __str__(self):
        return str(self.timestamp) + " " + str(self.heartrate)
