import csv
from flow.FlowData import FlowData
class FlowDataParser:
    def parse(self, file):
        polution_concentration = dict()
        with open(file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:

                dataRow = FlowData(int(float(row[0])), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                polution_concentration[dataRow.timestamp] = dataRow

        return polution_concentration



