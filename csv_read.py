import csv

#Read data from csv file
def read_csv_data ():

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
    
    return sat_name_list, NORAD_list, frequency_band_list, operator_list