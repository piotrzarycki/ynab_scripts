import csv
import argparse 
data = []

parser = argparse.ArgumentParser(description='file input for parse bank information')
parser.add_argument('--file', metavar='str', type=str)
args = parser.parse_args()
 
with open(args.file, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        dataRow = dict()
        if i == 0:
            i += 1
            continue

        dataRow['Date'] = row[1]
        dataRow['Payee'] = row[6]
        dataRow['Memo'] = row[5]

        if row[7].replace('-', '').replace('.', '').isdigit():
            dataRow['Outflow'] = abs(float(row[7]))
            dataRow['Inflow'] = ''
        else:
            dataRow['Inflow'] = abs(float(row[8]))
            dataRow['Outflow'] = ''

        data.append(dataRow)
        print dataRow

with open('millenium.csv', 'wb') as csvfile:
    fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()
    spamwriter.writerows(data)
