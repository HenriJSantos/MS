from typing import Match
import pandas as pd
import numpy as np
from pandas.tseries.offsets import Hour

df = pd.read_csv("../data/aggregated/2015-01-01.csv",
                 header=0, sep=",", low_memory=False)
df2 = pd.read_csv("../sensors_location.csv",
                  header=0, sep=",", low_memory=False)
# change equipment id for the road section id
df['EQUIPMENTID'] = df['EQUIPMENTID'].replace(
    df2['EQUIPMENTID'].to_numpy(),
    df2['roadsectionId'].to_numpy())

# create a file for each hour, and for each hout count how many occurencies on each id
# counters for each sensor:
counter = {161: 0, 163: 0, 165: 0, 165: 0, 166: 0, 167: 0, 169: 0, 170: 0, 171: 0, 172: 0, 173: 0, 175: 0, 177: 0, 178: 0, 179: 0, 182: 0, 183: 0, 184: 0,
           186: 0, 187: 0, 188: 0, 189: 0, 192: 0, 193: 0, 194: 0}


def parse_hour(hour, array):
    aux = array

    for index, row in df.iterrows():
        if hour in row['AGG_PERIOD_START']:
            if row['EQUIPMENTID'] == 161:
                aux[161] = aux[161] + 1
            elif row['EQUIPMENTID'] == 163:
                aux[163] = aux[163] + 1
            elif row['EQUIPMENTID'] == 165:
                aux[165] = aux[165] + 1
            elif row['EQUIPMENTID'] == 166:
                aux[166] = aux[166] + 1
            elif row['EQUIPMENTID'] == 167:
                aux[167] = aux[167] + 1
            elif row['EQUIPMENTID'] == 169:
                aux[169] = aux[169] + 1
            elif row['EQUIPMENTID'] == 170:
                aux[170] = aux[170] + 1
            elif row['EQUIPMENTID'] == 171:
                aux[171] = aux[171] + 1
            elif row['EQUIPMENTID'] == 172:
                aux[172] = aux[172] + 1
            elif row['EQUIPMENTID'] == 173:
                aux[173] = aux[173] + 1
            elif row['EQUIPMENTID'] == 175:
                aux[175] = aux[175] + 1
            elif row['EQUIPMENTID'] == 177:
                aux[177] = aux[177] + 1
            elif row['EQUIPMENTID'] == 178:
                aux[178] = aux[178] + 1
            elif row['EQUIPMENTID'] == 179:
                aux[179] = aux[179] + 1
            elif row['EQUIPMENTID'] == 182:
                aux[182] = aux[182] + 1
            elif row['EQUIPMENTID'] == 183:
                aux[183] = aux[183] + 1
            elif row['EQUIPMENTID'] == 184:
                aux[184] = aux[184] + 1
            elif row['EQUIPMENTID'] == 186:
                aux[186] = aux[186] + 1
            elif row['EQUIPMENTID'] == 187:
                aux[187] = aux[187] + 1
            elif row['EQUIPMENTID'] == 188:
                aux[188] = aux[188] + 1
            elif row['EQUIPMENTID'] == 189:
                aux[189] = aux[189] + 1
            elif row['EQUIPMENTID'] == 192:
                aux[192] = aux[192] + 1
            elif row['EQUIPMENTID'] == 193:
                aux[193] = aux[193] + 1
            elif row['EQUIPMENTID'] == 194:
                aux[194] = aux[194] + 1

    data = []
    for key in aux:
        data.append([key, '?', aux[key]])

    res = pd.DataFrame(data, columns=['ORIGIN', 'DESTINATION', 'OCCURRENCES'])
    return res


# 00:00 - 01:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-0.1.csv", index=False)

# 01:00 - 02:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-1.2.csv", index=False)

# 02:00 - 03:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-2.3.csv", index=False)

# 03:00 - 04:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-3.4.csv", index=False)

# 04:00 - 05:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-4.5.csv", index=False)

# 05:00 - 06:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-5.6.csv", index=False)

# 06:00 - 07:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-6.7.csv", index=False)

# 07:00 - 08:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-7.8.csv", index=False)

# 08:00 - 09:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-8.9.csv", index=False)

# 09:00 - 10:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-9.10.csv", index=False)

# 10:00 - 11:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-10.11.csv", index=False)

# 11:00 - 12:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-11.12.csv", index=False)

# 12:00 - 13:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-12.13.csv", index=False)

# 13:00 - 14:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-13.14.csv", index=False)

# 14:00 - 15:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-14.15.csv", index=False)

# 15:00 - 16:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-15.16.csv", index=False)

# 16:00 - 17:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-16.17.csv", index=False)

# 17:00 - 18:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-17.18.csv", index=False)

# 18:00 - 19:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-18.19.csv", index=False)

# 19:00 - 20:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-19.20.csv", index=False)

# 20:00 - 21:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-20.21.csv", index=False)

# 21:00 - 22:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-21.22.csv", index=False)

# 22:00 - 23:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-22.23.csv", index=False)

# 23:00 - 00:00
parse_hour('00:00', counter).to_csv(
    "../data/od_matrixes/od_matrix-23.0.csv", index=False)
