import csv

def write_csv(data, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Course', 'Last Activity Date'])
        for row in data:
            writer.writerow(row)
