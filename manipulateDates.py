__author__ = 'adam.stueckrath'

import csv
from datetime import date, timedelta
from random import randrange

newrow = []
csvFileRead = open('/Users/adam.stueckrath/Documents/Projects/ScrubbingSample.txt', 'rU')
csvFileNew = open('/Users/adam.stueckrath/Documents/Projects/NewScrubbingSample.txt', 'wb')

# Open the CSV
csvReader = csv.reader(csvFileRead)
# header = next(csvReader, None)

# Append the rows to variable new row
for row in csvReader:
    newrow.append(row)


#randomlist = [ '1','2','3','4','6','15','18','23','27','45','96','97','119','131','133','150','165','187','197','252','256','A1','B13' ]
#random_index = randrange(0,len(randomlist))
for row in newrow:
    row[0] = date.today() - timedelta(days=180)
    #row[6] = randomlist[random_index]
    #row[53] = date.today()
csvFileRead.close()

# Create a new CSV file
csvWriter = csv.writer(csvFileNew, delimiter='\t')
# if header:
#     csvWriter.writerow(header)
# Append the csv with rows from new row variable
for row in newrow:
    csvWriter.writerow(row)
csvFileNew.close()