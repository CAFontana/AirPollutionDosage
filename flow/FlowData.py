from core.util import round_to_multiple


class FlowData:
    timestamp = 0
    date = ""
    NO2 = 0  # (ppb)
    VOC = 0  # (ppb)
    PM10 = 0  # (ug/m3)
    PM25 = 0  # (ug/m3)
    NO2_PlumeAQI = 0
    VOC_PlumeAQI = 0
    PM10_PlumeAQI = 0
    PM25_PlumeAQI = 0

    def __init__(self, timestamp, date, no2, voc, pm10, pm25, no2_plume_aqi, voc_plume_aqi, pm10_plume_aqi,
                 pm25_plume_aqi) -> None:
        super().__init__()
        self.timestamp = round_to_multiple(timestamp)
        self.date = date
        self.NO2 = no2
        self.VOC = voc
        self.PM10 = pm10
        self.PM25 = pm25
        self.NO2_PlumeAQI = no2_plume_aqi
        self.VOC_PlumeAQI = voc_plume_aqi
        self.PM10_PlumeAQI = pm10_plume_aqi
        self.PM25_PlumeAQI = pm25_plume_aqi

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
