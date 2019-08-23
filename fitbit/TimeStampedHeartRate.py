class TimeStampedHeartRate:
    timestamp = 0
    heartrate = 0

    def __init__(self, ts, hr):
        self.timestamp = ts
        self.heartrate = hr

    def __str__(self):
        return str(self.timestamp) + " " + str(self.heartrate)
