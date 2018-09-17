# coding: utf8
import csv
import argparse

data = []

parser = argparse.ArgumentParser(description='file input for parse bank information')
parser.add_argument('--file', metavar='str', type=str)
args = parser.parse_args()

with open(args.file, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    i = 0
    for row in reader:
        dataRow = dict()
        if i == 0:
            i += 1
            continue

        dataRow['Date'] = row[0].replace('września', '09').replace(' ', '-').encode('utf8')
        dataRow['Payee'] = row[1]
        dataRow['Memo'] = row[7]

        if row[2].replace(',', '').replace('\xc2\xa0', '').isdigit():
            dataRow['Outflow'] = abs(float(row[2].replace(',', '.').replace('\xc2\xa0', '')))
            dataRow['Inflow'] = ''
        else:
            dataRow['Inflow'] = abs(float(row[3].replace(',', '.').replace('\xc2\xa0', '')))
            dataRow['Outflow'] = ''

        data.append(dataRow)
        print dataRow

with open('revolut_output.csv', 'wb') as csvfile:
    fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()
    spamwriter.writerows(data)
