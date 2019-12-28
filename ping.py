import csv
import os

#reading the CSV file
f = open('host.csv', 'r')
read = csv.reader(f)

for line in read:
    if line[0] == 'name':
        pass
    else:
        print("Starting Ping on {}".format(line[0]))
        ping = os.system("ping -c 1 " + line[1] + " > /dev/null 2>&1")
        if ping == 0:
            print("{} is alive".format(line[0]))
        else:
            print("{} is down".format(line[0]))

f.close()
