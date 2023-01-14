from tkinter import *

#Select operators to filter for using checkbuttons
def operator_selection_checkbox (possible_operators):

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

    return operator_filter

#Select frequency bands to filter for using checkbuttons
def frequency_band_checkbox (possible_frequency_bands):
    
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

    return frequency_band_filter