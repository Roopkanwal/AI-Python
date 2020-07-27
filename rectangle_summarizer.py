import csv
from statistics import mean

# Open and read the contents of CSV file
with open("DATA475_lab_rectangles_data.csv",newline="") as f:
    reader = csv.reader(f)
    next(reader)

# Calucate the area of rectangles    
    areas=[float(line[1]) * float(line[2]) for line in reader]
    
# Calculates and print the total, average, maximum and minimum area of all rectangles
column_names = {
    "Total Count" : len(areas),
    "Total Area" : sum(areas),
    "Average Area" : mean(areas),
    "Max Area" : max(areas),
    "Min Area" : min(areas)
}
 
for key,value in column_names.items():
     print(f"{key}: {value}")

# Store the above information in another CSV file named summary.csv
with open("summary.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(column_names.keys())
    writer.writerow(column_names.values())