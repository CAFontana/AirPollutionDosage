from core.util import roundToMultiple

class FlowData:
    timestamp = 0
    date = ""
    NO2 = 0 # (ppb)
    VOC = 0 # (ppb)
    PM10 = 0 # (ug/m3)
    PM25 = 0 # (ug/m3)
    NO2_PlumeAQI = 0
    VOC_PlumeAQI = 0
    PM10_PlumeAQI = 0
    PM25_PlumeAQI = 0

    def __init__(self, timestamp, date, NO2, VOC, PM10, PM25, NO2_PlumeAQI, VOC_PlumeAQI, PM10_PlumeAQI, PM25_PlumeAQI) -> None:
        super().__init__()
        self.timestamp = roundToMultiple(timestamp)
        self.date = date
        self.NO2 = NO2
        self.VOC = VOC
        self.PM10 = PM10
        self.PM25 = PM25
        self.NO2_PlumeAQI = NO2_PlumeAQI
        self.VOC_PlumeAQI = VOC_PlumeAQI
        self.PM10_PlumeAQI = PM10_PlumeAQI
        self.PM25_PlumeAQI = PM25_PlumeAQI

    def __str__(self):
        return str(self.timestamp) + "\n" + \
               str(self.date) + "\n" + \
               "NO2: " + str(self.NO2) + "\n" + \
               "VOC: " + str(self.VOC) + "\n" + \
               "PM10: " + str(self.PM10) + "\n" + \
               "PM25: " + str(self.PM25) + "\n" + \
               "NO2_PlumeAQI: " + str(self.NO2_PlumeAQI) + "\n" + \
               "VOC_PlumeAQI: " + str(self.VOC_PlumeAQI) + "\n" + \
               "PM10_PlumeAQI: " + str(self.PM10_PlumeAQI) + "\n" + \
               "PM25_PlumeAQI: " + str(self.PM25_PlumeAQI) + "\n"
