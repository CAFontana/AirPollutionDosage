from fitbit.FitbitDataParser import FitbitDataParser
from flow.FlowDataParser import FlowDataParser
from DosageData import DosageData
from util import roundToMultiple
from collections import defaultdict
import matplotlib.pyplot as plt


class PolutantCalc:
    polutionConcentrations = FlowDataParser().parse('flow/user_measures_20190813_20190823_1.csv')

    liter_per_m3 = 1000
    NO2_ppb_to_ug_m3 = 1.88  # https://www2.dmu.dk/AtmosphericEnvironment/Expost/database/docs/PPM_conversion.pdf
    ppb_coeff = 0.0409 * 1000  # https://cfpub.epa.gov/ncer_abstracts/index.cfm/fuseaction/display.files/fileID/14285
    average_molecular_weight_of_VOCs = 122.01  # https://www.eurofinsus.com/media/161384/unit_conversion1.xls
    tshr_interval_seconds = 5 # heart rate is captured in 5 seconds intervals

    def calculate_workout_polution(self, workout_txc):


        tshr_map = FitbitDataParser().parse(workout_txc)

        dosage = defaultdict(DosageData)

        for tshr in tshr_map.values():

            minute_ventilation = 0.0063 * float(tshr.heartrate) ** 2 - 0.6253 * float(tshr.heartrate) + 28.152

            dosage[str(tshr.timestamp)] = DosageData(
                tshr.timestamp,
                self.polutionConcentrations[roundToMultiple(tshr.timestamp)].date,
                minute_ventilation,
                float(self.polutionConcentrations[roundToMultiple(tshr.timestamp)].NO2) * (
                            self.NO2_ppb_to_ug_m3 / self.liter_per_m3) * minute_ventilation / (
                            60 / self.tshr_interval_seconds),  # NO2
                float(self.polutionConcentrations[roundToMultiple(tshr.timestamp)].VOC) * (
                            self.ppb_coeff * self.average_molecular_weight_of_VOCs / self.liter_per_m3) * minute_ventilation / (
                            60 / self.tshr_interval_seconds), # VOC
                float(self.polutionConcentrations[
                          roundToMultiple(tshr.timestamp)].PM10) * self.liter_per_m3 * minute_ventilation / (
                            60 / self.tshr_interval_seconds),  # PM10
                float(self.polutionConcentrations[
                          roundToMultiple(tshr.timestamp)].PM25) * self.liter_per_m3 * minute_ventilation / (
                            60 / self.tshr_interval_seconds)  # PM25
            )


        return dosage

dosage = PolutantCalc().calculate_workout_polution('24627482886.tcx')

time = []
VE_series = []
NO2_series = []
VOC_series = []
PM10_series = []
PM25_series = []

for ts, dose in dosage.items():
    print ( ts, dose )
    time.append(ts)
    VE_series.append(dose.minute_ventilation)
    NO2_series.append(dose.NO2*10)
    VOC_series.append(dose.VOC/100)
    PM10_series.append(dose.PM10/1000)
    PM25_series.append(dose.PM25/1000)

plt.plot(time, VE_series, c='blue')
plt.plot(time, NO2_series, c='black')
plt.plot(time, VOC_series, c='green')
plt.plot(time, PM10_series, c='orange')
plt.plot(time, PM25_series, c='red')
plt.show()


# TODO: check calculations for dosage, determine how to plot geo, use biking dataset from Aug 22.
# TODO: Review data structure efficiency
