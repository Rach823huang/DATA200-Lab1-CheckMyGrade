import csv


def read_csv_file(filename):
    data = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"{filename} not found.")
    return data


def append_csv_file(filename, row):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def write_csv_file(filename, header, data):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)