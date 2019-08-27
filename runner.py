from core.PolutantCalc import PolutantCalc
from core.util import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

concentration, dosage = PolutantCalc().calculate_workout_polution('data/24627482886.tcx', 'data/user_measures_20190813_20190823_1.csv')

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
              'NO2_Concentration' : float(concentration[roundToMultiple(float(ts))].NO2),
              'NO2_AQI' : AQINO2(float(concentration[roundToMultiple(float(ts))].NO2)),
              'VOC_Concentration': float(concentration[roundToMultiple(float(ts))].VOC),
              'PM10_Concentration': float(concentration[roundToMultiple(float(ts))].PM10),
              'PM25_Concentration': float(concentration[roundToMultiple(float(ts))].PM25),
              'NO2' : dose.NO2,
              'VOC' : dose.VOC,
              'PM10': dose.PM10,
              'PM25': dose.PM25
              })

dosage_df = pd.DataFrame(tmp_d, index=[d.get('timestamp') for d in tmp_d])
# print(dosage_df)


dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Minute Ventilation (L/min)",
    c="minute_ventilation", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Exposure (ppb)",
    c="NO2_Concentration", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)


cmap = mpl.colors.ListedColormap(['green', 'yellow', 'orange', 'red', 'purple', 'maroon'])
bounds = [50, 100, 150, 200, 300, 500]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="AQI",
    c="NO2_AQI", norm=norm, cmap=cmap,
    colorbar=True, alpha=0.4, figsize=(10,7)
)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Exposure (ppb)",
    c="NO2_Concentration", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Dosage (microgram)",
    c="NO2", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Exposure (ppb)",
    c="VOC_Concentration", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)
dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Dosage (microgram)",
    c="VOC", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Exposure (microgram/m3)",
    c="PM25_Concentration", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)
dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Dosage (microgram)",
    c="PM25", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)

dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Exposure (microgram/m3)",
    c="PM10_Concentration", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)
dosage_df.plot(kind="scatter", x="longitude", y="latitude",
    label="Dosage (microgram)",
    c="PM10", cmap=plt.get_cmap("jet"),
    colorbar=True, alpha=0.4, figsize=(10,7),
)

plt.legend()
plt.show()


# EPA's Airnow had exposure measured at 0-100 AQI during this time period while AQI from Flow was at 100 to 175.
# Twice the exposure as the EPA knows of not including the increased ventilation from exercise on a path which
# many citizen frequent for "fresh air".

# Personally experienced eye irritation after the turn at the end of the airport runway,.

# plt.plot(time, VE_series, c='blue')
# plt.plot(time, NO2_series, c='black')
# plt.plot(time, VOC_series, c='green')
# plt.plot(time, PM10_series, c='orange')
# plt.plot(time, PM25_series, c='red')

