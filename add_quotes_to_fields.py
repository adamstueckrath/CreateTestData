__author__ = 'adam.stueckrath'

import csv

newrow = []
csvFileRead = open('/Users/adam.stueckrath/Desktop/dm_test_data.csv', 'rb')
csvFileNew = open('/Users/adam.stueckrath/Desktop/new_dm_test_data.csv', 'wb')

# Open the CSV
csvReader = csv.reader(csvFileRead, delimiter=',')

# Append the rows to variable new row
for row in csvReader:
    newrow.append(row)

# Add quotes around the fourth list item
for row in newrow:
    row[1] = "'"+str(row[1])+"'"

csvFileRead.close()

# Create a new CSV file
csvWriter = csv.writer(csvFileNew, delimiter=',')

# Append the csv with rows from new row variable
for row in newrow:
    csvWriter.writerow(row)

csvFileNew.close()