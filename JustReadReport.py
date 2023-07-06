import csv
import os
from tokenize import Double


RawList = []
FilteredList = []
    
#with open(r'C:\Users\jdalis5n\Documents\Projects\Python\SpaceReport\SpaceReport.csv') as csvfile:

# Open the CSV file and dump info into RawList
with open(r'\\log-s8mo-1fs\groups\IT Support\Windows 10\Scripts\SpaceReport.csv') as csvfile:
    fileReader = csv.reader(csvfile)
    for row in fileReader:
        # The PS Script checks for storage across 3 possible drives. This removes the reading of possible D: and E: drives.
        DiskInfo = row[0] +" "+ row[1]
        RawList.append(DiskInfo)
        
# Store filtered Contents into local list FilteredList.
# Filtered Contents being any workstations (ServerName in the CSV) that start with the letter 'D' for DC
# This really only removes the ServerName line from the CSV.
for i in RawList:
    if i[0] == 'D':
        FilteredList.append(i)


    # Seperate contents into categories [Computer Name, Size Left, Size Type]
    CategoriesSplit = [item.split(' ') for item in FilteredList]


# Display all the computers that are under 20 size 
print("\n\n")
with open(r'\\log-s8mo-1fs\groups\IT Support\Windows 10\Scripts\results.txt', 'w') as file_object:
    for x in CategoriesSplit:
        # y is the Storage size left on the computer.
        y = float(x[1])
        # Change the value that you want less than 'y' for the size you are looking for the drive to have left.
        # Print the names of the computers onto the console.
        if y < 20:
            print(x)
            file_object.write(str(x))


print("\n\n")
