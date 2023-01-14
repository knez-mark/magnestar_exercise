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