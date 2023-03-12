import csv


total_store = 0
with open('output/store.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for product in reader:
        quantity = int(product['Quantity'])
        total_store += quantity

print(f'Total stock: {total_store}')