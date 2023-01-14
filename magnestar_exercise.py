import csv
from tkinter import *

#Section 1

sat_name_list = []
NORAD_list = []
frequency_band_list = []
operator_list = []

with open('satellites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    first_line = True
    for row in csv_reader:
        if first_line:
            sat_name_index = row.index("sat name")
            NORAD_index = row.index("NORAD")
            frequency_band_index = row.index ("Frequency Band")
            operator_index = row.index ("Operator")
            first_line = False
        else:
            #Add .strip() to remove unwanted whitespace (some operators contain this)
            sat_name_list.append (row [sat_name_index].strip())
            NORAD_list.append (row [NORAD_index].strip())
            frequency_band_list.append (row [frequency_band_index].strip())
            operator_list.append (row [operator_index].strip())

#List of valid frequency bands (given)
possible_frequency_bands = ["VLF","LF","MF","HF","VHF","UHF","SHF","L","S","C","X","Ku","K","Ka","EHF"]

possible_operators = []

for operator in operator_list:
    try:
        possible_operators.index(operator)
    except ValueError: #Operator not in list already
        if operator != "":
            possible_operators.append (operator)

#Section 2

root = Tk()
root.geometry("500x425+120+120")
root.resizable(False, False)
root.title('Operator Selection')

operator_filter = []

for i in range (len (possible_operators)):
    operator_filter.append (IntVar())
    c = Checkbutton(root, text = possible_operators[i], variable=operator_filter[i])
    c.pack()

#Was included before but was causing issues, so it was removed
b = Button(root,text="Done",command=root.destroy)
b.pack()
root.mainloop()

for i in range (len(operator_filter)):
    operator_filter [i] = operator_filter [i].get()

#Section 3

root = Tk()
root.geometry("500x400+120+120")
root.resizable(False, False)
root.title('Frequency Band Selection')

frequency_band_filter = []

for i in range (len (possible_frequency_bands)):
    frequency_band_filter.append (IntVar())
    c = Checkbutton(root, text = possible_frequency_bands[i], variable=frequency_band_filter[i])
    c.pack()

b = Button(root,text="Done",command=root.destroy)
b.pack()
root.mainloop()

for i in range (len(frequency_band_filter)):
    frequency_band_filter [i] = frequency_band_filter [i].get()


def find_filtered_indexes (possible_frequency_bands, possible_operators, frequency_band_filter, operator_filter, frequency_band_list, operator_list):
    
    if sum (frequency_band_filter) == 0 and sum (operator_filter) == 0:
        return list (range (len(frequency_band_list))) #Print all satellites if no filters are applied
    
    selected_frequency_bands = []
    selected_operators = []
    
    for i in range (len (frequency_band_filter)):
        if frequency_band_filter [i] == 1:
            selected_frequency_bands.append (possible_frequency_bands [i])
    for i in range (len (operator_filter)):
        if operator_filter [i] == 1:
            selected_operators.append (possible_operators [i])
    
    filtered_indexes = []
    
    for i in range (len (frequency_band_list)):
        index_found = False
        
        if (frequency_band_list [i] != ''):
            
            frequency_band_split = frequency_band_list [i].split("/")
            
            for frequency_band in frequency_band_split:
                try:
                    selected_frequency_bands.index(frequency_band)
                    filtered_indexes.append (i)
                    index_found = True
                    break
                except ValueError:
                    continue
        
        if (index_found):
            continue
        
        if (operator_list [i] != ''):
            try:
                selected_operators.index(operator_list [i])
                filtered_indexes.append (i)
            except ValueError:
                continue
    
    return filtered_indexes

#Section 4

print ("sat name".ljust(25, ' '), "NORAD".ljust(10, ' '), "Frequency Band".ljust(20, ' '), "Operator")
print ()
filtered_indexes = find_filtered_indexes (possible_frequency_bands, possible_operators, frequency_band_filter, operator_filter, frequency_band_list, operator_list)

for i in filtered_indexes:
    print (sat_name_list [i].ljust(25, ' '), NORAD_list [i].ljust(10, ' '), frequency_band_list [i].ljust(20, ' '), operator_list [i])