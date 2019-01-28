import csv

csvFileName = "remainders\\remainders.csv" 
with open(csvFileName, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = [['Time', 'Remainder'],
            ['10.00', 'finish remainder'],
            ['10.10', 'check remainder']]
    a.writerows(data)
print 'csv file created'
