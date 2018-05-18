import csv
data = []
with open('mbank_input.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    i = 0
    for row in reader:
        dataRow = dict()
        if i == 0:
            i += 1
            continue

        price = float(row[6].replace(',', '.').replace(' ', ''))

        dataRow['Date'] = row[0]
        dataRow['Payee'] = row[4].decode('cp1250').encode('UTF-8')
        dataRow['Memo'] = row[3].decode('cp1250').encode('UTF-8')

        if price < 0:
            dataRow['Outflow'] = abs(price)
            dataRow['Inflow'] = ''
        else:
            dataRow['Inflow'] = abs(price)
            dataRow['Outflow'] = ''

        data.append(dataRow)
        print dataRow

with open('mbank.csv', 'wb') as csvfile:
    fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()
    spamwriter.writerows(data)
