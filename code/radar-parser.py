import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

tree = ET.parse('Sumo/Simulation/radar_out.xml')
root = tree.getroot()

df = pd.DataFrame(columns=["EQUIPMENTID","LANE_BUNDLE_DIRECTION","LANE","HOUR","TOTAL_VOLUME"])
for child in root:
    attribs = child.attrib
    hour = int(float(attribs['begin'])) / 3600
    id = attribs['id']
    equipment_id = id.split('_')[0]
    directionLane = id.split('_')[2]
    direction = 'C' if directionLane[0] == 'E' else 'D'
    lane = directionLane[1]
    volume = attribs['nVehEntered']

    df.loc[-1] = [equipment_id, direction, lane, hour, volume]
    df.index = df.index + 1
    df = df.sort_index()

df = df.astype({"TOTAL_VOLUME": 'int32'})

df = df.groupby(['EQUIPMENTID', 'LANE_BUNDLE_DIRECTION', 'HOUR']).agg({
    "TOTAL_VOLUME": np.sum
})

df.sort_values(by=["EQUIPMENTID", "LANE_BUNDLE_DIRECTION", "HOUR"])
df.to_csv('data/radar_info.csv')