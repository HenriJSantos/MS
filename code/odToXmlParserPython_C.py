from fileinput import filename

name = "matrizOD_c_Mon_12"
fileNameRead = "../code/" + name + ".csv"
fileNameWrite = "../Sumo/Simulation/od-matrixes-xml/" + name + ".xml"

idName = "sim"
startTime = "0.00"
endTime = "3600.00"

fr = open(fileNameRead, "r")
fw = open(fileNameWrite, "w")

textToWrite = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<data xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"http://sumo.dlr.de/xsd/datamode_file.xsd\">\n"
textToWrite = textToWrite + \
    "    <interval id=\"" + idName + "\" begin=\"" + \
    startTime + "\" end=\"" + endTime + "\">\n"

origin = 1
destination = 1

for line in fr:

    values = line.split(',')
    values[len(values) -
           1] = values[len(values) - 1].replace('\n', '')

    print(values)
    # reset destination
    destination = 1
    for v in values:
        textToWrite = textToWrite + "        <tazRelation from=\"EO" + \
            str(origin) + "\" to=\"ED" + \
            str(destination) + "\" count=\"" + \
            str(v).replace('\n', '') + "\"/>\n"

    origin = origin + 1

    # ignore origin 11 since it is not included on the network
    if origin == 10:
        origin = origin + 1

textToWrite = textToWrite + "    </interval>\n</data>"
fw.write(textToWrite)

fr.close()
fw.close()
