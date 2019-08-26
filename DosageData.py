from util import roundToMultiple

class DosageData:
    timestamp = 0
    date = ""
    lat = 0
    long = 0
    minute_ventilation = 0 # L/min
    NO2 = 0 # ug
    VOC = 0 # ug
    PM10 = 0 # ug
    PM25 = 0 # ug

    def __init__(self, timestamp, date, lat, long, minute_ventilation, NO2, VOC, PM10, PM25) -> None:
        super().__init__()

        self.timestamp = roundToMultiple(timestamp)
        self.date = date
        self.lat = lat
        self.long = long
        self.minute_ventilation = minute_ventilation
        self.NO2 = NO2
        self.VOC = VOC
        self.PM10 = PM10
        self.PM25 = PM25

    def __str__(self):
        return str(self.timestamp) + "\n" + \
                str(self.date) + "\n" + \
                str(self.lat) + ", " + str(self.long) + "\n" + \
                "Minute Ventilation: " + str(self.minute_ventilation) + " L/min\n" + \
                "NO2: " + str(self.NO2) + " ug\n" + \
                "VOC: " + str(self.VOC) + " ug\n" + \
                "PM10: " + str(self.PM10) + " ug\n" + \
                "PM25: " + str(self.PM25) + " ug\n"
