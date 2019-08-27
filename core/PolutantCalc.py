from fitbit.FitbitDataParser import FitbitDataParser
from flow.FlowDataParser import FlowDataParser
from core.DosageData import DosageData
from core.util import *
from collections import defaultdict

class PolutantCalc:
    liter_per_m3 = 1000
    NO2_ppb_to_ug_m3 = 1.88  # https://www2.dmu.dk/AtmosphericEnvironment/Expost/database/docs/PPM_conversion.pdf
    ppb_coeff = 0.0409 * 1000  # https://cfpub.epa.gov/ncer_abstracts/index.cfm/fuseaction/display.files/fileID/14285
    average_molecular_weight_of_VOCs = 122.01  # https://www.eurofinsus.com/media/161384/unit_conversion1.xls
    tshr_interval_seconds = 5 # heart rate is captured in 5 seconds intervals

    def calculate_workout_polution(self, workout_txc, polutionConcentrations):
        tshr_map = FitbitDataParser().parse(workout_txc)
        concentration = FlowDataParser().parse(polutionConcentrations)
        dosage = defaultdict(DosageData)

        for tshr in tshr_map.values():

            minute_ventilation = 0.0063 * float(tshr.heartrate) ** 2 - 0.6253 * float(tshr.heartrate) + 28.152

            dosage[str(tshr.timestamp)] = DosageData(
                tshr.timestamp,
                concentration[roundToMultiple(tshr.timestamp)].date,
                tshr.lat,
                tshr.long,
                minute_ventilation,
                float(concentration[roundToMultiple(tshr.timestamp)].NO2) * (
                            self.NO2_ppb_to_ug_m3 / self.liter_per_m3) * minute_ventilation / (
                            60 / self.tshr_interval_seconds),  # NO2
                float(concentration[roundToMultiple(tshr.timestamp)].VOC) * (
                            self.ppb_coeff * self.average_molecular_weight_of_VOCs / self.liter_per_m3) * minute_ventilation / (
                            60 / self.tshr_interval_seconds), # VOC
                float(concentration[
                          roundToMultiple(tshr.timestamp)].PM10) * self.liter_per_m3 * minute_ventilation / (
                            60 / self.tshr_interval_seconds),  # PM10
                float(concentration[
                          roundToMultiple(tshr.timestamp)].PM25) * self.liter_per_m3 * minute_ventilation / (
                            60 / self.tshr_interval_seconds)  # PM25
            )

        return concentration, dosage
