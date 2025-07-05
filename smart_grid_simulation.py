import csv
import random
import time

with open('smart_grid_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'Voltage', 'Current', 'Frequency', 'Load'])

    for i in range(100):  # generate 100 fake records
        voltage = round(random.uniform(210, 240), 2)
        current = round(random.uniform(5, 20), 2)
        frequency = round(random.uniform(49, 51), 2)
        load = round(voltage * current / 1000, 2)
        writer.writerow([time.time(), voltage, current, frequency, load])
        time.sleep(0.5)  # 0.5 sec delay between data points
