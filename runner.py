from core.PolutantCalc import PolutantCalc
from core.util import *
from core.Converter import Converter
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
import pandas as pd

concentration, dosage = PolutantCalc().calculate_workout_polution('data/24627482886.tcx',
                                                                  'data/user_measures_20190813_20190823_1.csv')

# Create the pd table
time = []
lat_series = []
long_series = []
VE_series = []
NO2_series = []
VOC_series = []
PM10_series = []
PM25_series = []

for ts, dose in dosage.items():
    time.append(ts)
    lat_series.append(dose.lat)
    long_series.append(dose.long)
    VE_series.append(dose.minute_ventilation)
    NO2_series.append(dose.NO2)
    VOC_series.append(dose.VOC)
    PM10_series.append(dose.PM10)
    PM25_series.append(dose.PM25)


timestamp_series = pd.Series()
tmp_d = []

for ts, dose in dosage.items():
    tmp_d.append({'timestamp': ts,
                  'latitude': float(dose.lat),
                  'longitude': float(dose.long),
                  'minute_ventilation': dose.minute_ventilation,
                  'NO2_Concentration': float(concentration[round_to_multiple(float(ts))].NO2),
                  'NO2_Dosage': float(dose.NO2),
                  'NO2_AQI': Converter.aqi_no2(float(concentration[round_to_multiple(float(ts))].NO2)),
                  'VOC_Concentration': float(concentration[round_to_multiple(float(ts))].VOC),
                  'VOC_Dosage': float(dose.VOC),
                  'PM10_Concentration': float(concentration[round_to_multiple(float(ts))].PM10),
                  'PM10_Dosage': float(dose.PM10),
                  'PM10_AQI': Converter.aqi_pm10(float(concentration[round_to_multiple(float(ts))].PM10)),
                  'PM25_Concentration': float(concentration[round_to_multiple(float(ts))].PM25),
                  'PM25_Dosage': float(dose.PM25),
                  'PM25_AQI': Converter.aqi_pm25(float(concentration[round_to_multiple(float(ts))].PM25))
                  })

dosage_df = pd.DataFrame(tmp_d, index=[d.get('timestamp') for d in tmp_d])
# print(dosage_df)

#  AQI Colors

cmap = mplc.ListedColormap(['green', 'yellow', 'orange', 'red', 'purple', 'maroon'])
bounds = [50, 100, 150, 200, 300, 500]
norm = mplc.BoundaryNorm(bounds, cmap.N)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Minute Ventilation (L/min)",
               c="minute_ventilation", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="AQI",
               c="NO2_AQI", norm=norm, cmap=cmap,
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Exposure (ppb)",
               c="NO2_Concentration", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Dosage (microgram)",
               c="NO2_Dosage", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7),
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Exposure (ppb)",
               c="VOC_Concentration", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Dosage (microgram)",
               c="VOC_Dosage", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7),
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="AQI",
               c="PM25_AQI", norm=norm, cmap=cmap,
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Exposure (microgram/m3)",
               c="PM25_Concentration", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Dosage (microgram)",
               c="PM25_Dosage", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="AQI",
               c="PM10_AQI", norm=norm, cmap=cmap,
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Exposure (microgram/m3)",
               c="PM10_Concentration", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
               label="Dosage (microgram)",
               c="PM10_Dosage", cmap=plt.get_cmap("jet"),
               colorbar=True, alpha=0.4, figsize=(10, 7)
               )

plt.legend()
plt.show()

# EPA's Airnow had exposure measured at 0-100 AQI during this time period while AQI from Flow was at 100 to 175.
# Twice the exposure as the EPA knows of not including the increased ventilation from exercise on a path which
# many citizen frequent for "fresh air".

# Personally experienced eye irritation after the turn at the end of the airport runway
