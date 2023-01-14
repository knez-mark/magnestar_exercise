from csv_read import *
from filter import *
from checkbutton import *

sat_name_list, NORAD_list, frequency_band_list, operator_list = read_csv_data ()

#List of valid frequency bands (given)
possible_frequency_bands = ["VLF","LF","MF","HF","VHF","UHF","SHF","L","S","C","X","Ku","K","Ka","EHF"]

#Obtain list of valid operators from csv file
possible_operators = []
for operator in operator_list:
    try:
        possible_operators.index(operator)
    except ValueError: #Operator not in list already
        if operator != "":
            possible_operators.append (operator)

operator_filter = operator_selection_checkbox (possible_operators)
frequency_band_filter = frequency_band_checkbox (possible_frequency_bands)

print ("sat name".ljust(25, ' '), "NORAD".ljust(10, ' '), "Frequency Band".ljust(20, ' '), "Operator")
print ()
filtered_indexes = find_filtered_indexes (possible_frequency_bands, possible_operators, frequency_band_filter, operator_filter, frequency_band_list, operator_list)

#Print data based on filter
for i in filtered_indexes:
    print (sat_name_list [i].ljust(25, ' '), NORAD_list [i].ljust(10, ' '), frequency_band_list [i].ljust(20, ' '), operator_list [i])