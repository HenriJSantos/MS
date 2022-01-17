from fileinput import filename

name = "matrix"
fileNameRead = "Sumo/Simulation/od-matrixes/" + name + ".csv"
fileNameWrite = "Sumo/Simulation/od-matrixes-xml/" + name + ".xml"

idName = "test"
startTime = "0.00"
endTime = "3600.00"

fr = open(fileNameRead, "r")
fw = open(fileNameWrite, "w")

textToWrite = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<data xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"http://sumo.dlr.de/xsd/datamode_file.xsd\">\n"
textToWrite = textToWrite + \
    "    <interval id=\"" + idName + "\" begin=\"" + \
    startTime + "\" end=\"" + endTime + "\">\n"
destinations = []
i = 0

for line in fr:
    if i == 0:
        destinations = line.split(',')
        destinations.pop(0)
        destinations[len(destinations) -
                     1] = destinations[len(destinations) - 1].replace('\n', '')
    origins = line.split(',')

    j = 0
    origin = ''
    for o in origins:
        if i == 0:
            continue
        if j == 0:
            origin = o
        else:
            textToWrite = textToWrite + "        <tazRelation from=\"" + \
                origin + "\" to=\"" + \
                destinations[j - 1] + "\" count=\"" + \
                o.replace('\n', '') + "\"/>\n"

        j = j + 1

    print(origins)
    i = i + 1

print(destinations)

textToWrite = textToWrite + "    </interval>\n</data>"
fw.write(textToWrite)

fr.close()
fw.close()
