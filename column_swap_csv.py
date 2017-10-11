import csv

with open('merged.csv', 'r') as infile, open('reorder.csv', 'wb') as outfile:
    fieldnames = ['created_at', 'screen_name', 'id', 'text', 'contributors', 'is quote', 'in reply to', 'in reply to id', \
        'favorited', 'favorite count', 'retweet count']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv.DictReader(infile):
        writer.writerow(row)