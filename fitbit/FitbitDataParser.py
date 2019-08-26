
import xml.etree.ElementTree as ET
from datetime import datetime
import time
from fitbit.TimeStampedHeartRate import TimeStampedHeartRate

class FitbitDataParser:
        fitbit_time_format = '%Y-%m-%dT%H:%M:%S.%f%z'

        def parse(self, file):
                tree = ET.parse(file)
                track = tree.getroot()[0][0][1][5]

                tsmap = dict()

                for trackpoint in track:
                        tshr = TimeStampedHeartRate(time.mktime(
                                datetime.strptime(trackpoint[0].text, self.fitbit_time_format).timetuple()),
                                trackpoint[4][0].text,
                                trackpoint[1][0].text,
                                trackpoint[1][1].text)

                        tsmap[tshr.timestamp] = tshr

                return tsmap
