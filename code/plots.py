import numpy as np
import matplotlib.pyplot as plt
import csv

file = open("data/aggregated/agg-weeKdays.csv")
csvreader = csv.reader(file)

setEQUIPMENTID = set()
for row in csvreader:
        if row[0] != 'EQUIPMENTID':
                setEQUIPMENTID.add(row[0])
print(setEQUIPMENTID)

daysOfWeek = {'Mon': 1, 'Tue': 2, 'Wed':3, 'Thu':4, 'Fri':5 }

for direction in ['C', 'D']:
    for equipmentID in setEQUIPMENTID:

        x = {1: [], 2: [], 3: [], 4: [], 5: []}
        y = {1: [], 2: [], 3: [], 4: [], 5: []}

        file = open("data/aggregated/agg-weeKdays.csv")
        csvreader = csv.reader(file)

        for row in csvreader:
                if row[0] == equipmentID and row[1] == direction:
                        x[daysOfWeek[row[2]]].append(row[3])
                        y[daysOfWeek[row[2]]].append(round(np.double(row[4])))

        # set width of bar
        barWidth = 0.15
        fig = plt.subplots(figsize =(20, 10))

        # Set position of bar on X axis
        br1 = np.arange(len(y[1]))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        br4 = [x + barWidth for x in br3]
        br5 = [x + barWidth for x in br4]

        # Make the plot
        plt.bar(br1, y[1], color ='r', width = barWidth,
                edgecolor ='grey', label ='Mon')
        plt.bar(br2, y[2], color ='g', width = barWidth,
                edgecolor ='grey', label ='Tue')
        plt.bar(br3, y[3], color ='b', width = barWidth,
                edgecolor ='grey', label ='Wed')
        plt.bar(br4, y[4], color ='y', width = barWidth,
                edgecolor ='grey', label ='Thu')
        plt.bar(br5, y[5], color ='c', width = barWidth,
                edgecolor ='grey', label ='Fri')

        # Adding Xticks
        plt.xlabel('Hour', fontweight ='bold', fontsize = 15)
        plt.ylabel('Total volume', fontweight ='bold', fontsize = 15)
        plt.title('Number of cars in the week days per hour in equipment id:' + equipmentID + " and direction:" + direction)
        plt.xticks([r + barWidth for r in range(len(y[1]))], x[1] )

        plt.legend()
        # plt.show()
        plt.savefig('plots/equipment_id_'+ equipmentID + '_direction_' + direction + '.png')

file.close()
