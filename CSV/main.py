import csv

with open('text.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([545, 'alex', 5 ])
    writer.writerow([55, 'aloce', 23 ])
    writer.writerow([54, 'aall', 54 ])
    writer.writerow([5452, 'aldfex', 52 ])

with open('text.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    print(reader)
    print(type(reader))
    for line in reader:
        print(line)