import csv
import argparse

parser = argparse.ArgumentParser(description='file input for parse bank information')
parser.add_argument('--file', metavar='str', type=str)
args = parser.parse_args()

data = []
with open(args.file, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    i = 0
    for row in reader:
        dataRow = dict()
        if i == 0:
            i += 1
            continue

        price = float(row[5].replace(',', '.').replace(' ', ''))

        dataRow['Date'] = row[3]
        dataRow['Payee'] = row[10].decode('cp1250').encode('UTF-8')
        dataRow['Memo'] = row[7].decode('cp1250').encode('UTF-8')

        if price < 0:
            dataRow['Outflow'] = abs(price)
            dataRow['Inflow'] = ''
        else:
            dataRow['Inflow'] = abs(price)
            dataRow['Outflow'] = ''

        data.append(dataRow)
        print dataRow

with open('kontomierz.csv', 'wb') as csvfile:
    fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()
    spamwriter.writerows(data)
