# magnestar_exercise

## Summary of Approach

The problem was broken up into six main parts: 
1)	Extract the relevant columns of data from the csv file
2)	Obtain a list of possible operators and frequency bands that could be applied as filters
3)	Obtain the desired operator filters from the user
4)	Obtain the desired frequency band filters from the user
5)	Apply the filters to determine the satellites which should be printed
6)	Print the filtered data

The first step was achieved by using the csv library in Python to read the data in row by row, appending the satellite name, NORAD ID, frequency band, and operator information into separate lists.

For the second step, the list of possible frequency bands was given. The list of possible operators was obtained by going through each operator name from the csv file and adding it to a list if the operator name was not already present in that list.

Using the tkinter library, the program opens up a window which contains checkboxes beside each of the operator names obtained in the previous step. Once the “Done” button is pressed, the program saves which boxes were selected by the user. The same method is used to save the selected frequency bands.

A simple algorithm was used to achieve the fifth step. It develops a list of all the indexes of the data that will be printed, based on the filters. First, the program checks if all boxes were unchecked, in which case it returns a list containing all the indexes. Otherwise, the program iterates through all of the rows from the csv file, and adds the index to the list if either the operator name matches one of the filters, or one of the frequency bands the satellite uses matches one of the filters.

Using the list of filtered indexes obtained in the previous step, the output is printed. The strings of each column are left justified by the same amount to line up each column.

## Steps for Running Program

Using the terminal, enter the “magnestar_exercise” directory (ensuring that the “satellites.csv” file is in that directory), and type “python3 magnestar_exercise.py”. A window called “Operator Selection” containing checkboxes should open. Select all of the operators you wish to filter for (or none) and press the “Done” button. Next, a window called “Frequency Band Selection” also containing checkboxes should open. Select all of the frequency bands you wish to filter for (or none) and press the “Done” button. The filtered output should be printed into the terminal.

Note: this program was run on a Mac using Python 3.10. Issues were experienced when running this program using Python 3.9 (specifically with the tkinter library), so the version was updated. If you encounter any problems, let me know.
