import csv
with open('Bill2.csv') as fileobject:
    filedata = csv.reader(fileobject)

    for row in filedata:
        print(row)

