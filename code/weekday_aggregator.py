import pandas as pd

df = pd.read_csv("data/aggregated/agg.csv", header=0, sep=",", low_memory=False)
df['AGG_PERIOD_START'] = pd.to_datetime(df['AGG_PERIOD_START'])
df = df[df['AGG_PERIOD_START'].dt.dayofweek < 5]
days = {0: 'Mon', 1: 'Tue', 2: "Wed", 3: "Thu", 4: "Fri"}
df['WEEK_DAY'] = df['AGG_PERIOD_START'].apply(lambda x: days[x.dayofweek])
df['HOUR'] = df['AGG_PERIOD_START'].dt.hour
df = df.groupby(['EQUIPMENTID','LANE_BUNDLE_DIRECTION','WEEK_DAY','HOUR']).TOTAL_VOLUME.agg('mean')

df.to_csv("data/aggregated/agg-weekdays.csv")