import csv

def read_csv(filepath):
    with open(filepath, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        return list(csvreader)

def write_csv(filepath, rows, fieldnames=None):
    with open(filepath, 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerows(rows)

def generate_rows(objects):
    for obj in objects:
        yield obj.to_dict()
