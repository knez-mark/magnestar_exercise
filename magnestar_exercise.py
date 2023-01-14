from csv_read import *
from filter import *
from tkinter import *

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

#Section 4

print ("sat name".ljust(25, ' '), "NORAD".ljust(10, ' '), "Frequency Band".ljust(20, ' '), "Operator")
print ()
filtered_indexes = find_filtered_indexes (possible_frequency_bands, possible_operators, frequency_band_filter, operator_filter, frequency_band_list, operator_list)

for i in filtered_indexes:
    print (sat_name_list [i].ljust(25, ' '), NORAD_list [i].ljust(10, ' '), frequency_band_list [i].ljust(20, ' '), operator_list [i])