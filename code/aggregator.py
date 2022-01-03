import pandas as pd

df = pd.read_csv("data/1P2015AEDL.csv", header=0, sep=",", low_memory=False)
df['AGG_PERIOD_START'] = pd.to_datetime(df['AGG_PERIOD_START'])
df = df[(df['AGG_PERIOD_START'] >= pd.to_datetime("2015-01-01")) & (df['AGG_PERIOD_START'] < pd.to_datetime("2015-01-02"))] # Get one day of data
df = df.sort_values(by=['EQUIPMENTID','AGG_PERIOD_START'])
df = df.drop(columns=[
    'AGGREGATE_BY_LANE_BUNDLEID','AGG_ID','AGG_PERIOD_LEN_MINS','NR_LANES',
    'LIGHT_VEHICLE_RATE','VOLUME_CLASSE_A','VOLUME_CLASSE_B','VOLUME_CLASSE_C',
    'VOLUME_CLASSE_D','VOLUME_CLASSE_0','AVG_SPEED_ARITHMETIC','AVG_SPEED_HARMONIC',
    'AXLE_CLASS_VOLUMES','AVG_LENGTH','AVG_SPACING','OCCUPANCY'])
df = df.groupby(['EQUIPMENTID', 'LANE_BUNDLE_DIRECTION']).apply(lambda x: x.resample('H', on='AGG_PERIOD_START')["TOTAL_VOLUME"].sum())
print(df)
df.to_csv("data/aggregated/2015-01-01.csv")
