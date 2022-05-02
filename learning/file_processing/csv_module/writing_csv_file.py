import csv

with open('exported_contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")

    writer.writerow(['name', 'phone'])
    writer.writerow((['matthew', '99999999']))
