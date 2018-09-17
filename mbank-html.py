from html.parser import HTMLParser
from bs4 import BeautifulSoup

import csv
data = []


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs: 
            print("  attr:", attr)

    def handle_endtag(self, tag):
        print("End tag :", tag)

    def handle_data(self, data):
        print("Data :", data)

with open('sample.html') as f: 
    read_data = f.read()

soup = BeautifulSoup(read_data, 'html.parser')

for span in soup.find_all('li'):
    if (span.header == None): continue


    date = span.header.find_all('div', class_="date")[0].contents[0]
    price = span.header.find_all('div', class_="amount")[0].find_all('strong')[0].contents[0].strip()
    who = span.header.find_all('div', class_="description")[0].find_all('span', class_="label")[0].contents[0]

    dataRow = dict()
    price = float(price.replace(',', '.').replace(' ', '').replace(u'\xa0', u''))

    dataRow['Date'] = date
    dataRow['Payee'] = who
    dataRow['Memo'] = ''

    if price < 0:
        dataRow['Outflow'] = abs(price)
        dataRow['Inflow'] = ''
    else:
        dataRow['Inflow'] = abs(price)
        dataRow['Outflow'] = ''

    data.append(dataRow)


with open('mbank_html.csv', 'w') as csvfile:
    fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()
    spamwriter.writerows(data)
