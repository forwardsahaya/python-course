# import the csv module
import csv

# create some data to write
data = [
  ['Name', 'Age', 'Country'],
  ['Alice', '25', 'USA'], 
  ['Bob', '30', 'Tanzania'],
  ['Charlie','35', 'Australia']
]

# open a file in write mode
with open('data.csv', 'w', newline='') as file:
    # create a writer object
    writer = csv.writer(file)
    # write each row of data
    for row in data:
        writer.writerow(row)

