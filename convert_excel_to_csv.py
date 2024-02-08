#!/usr/bin/python3

import openpyxl 
import csv
import pandas as pd

# open the workbook and store in wb object
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
	inf = day + ".xlsx"
	print("\nOpening:", inf)
	wb = openpyxl.load_workbook(inf)
	
	# select the active sheet
	sheet = wb['Sheet1']

	# read the first line
	status = sheet.cell(sheet.min_row, 1).value

	# delete the first line
	print("First line:\n", status)
	sheet.delete_rows(sheet.min_row, 1)
	#wb.save(filename)

	# save as csv, first the writer object is created
	with open((day + ".csv"), 'w', newline="") as csvfile:
		col = csv.writer(csvfile, delimiter='\t')
  
		# write the data in the csv file
		for r in sheet.rows:
			# row by row write operation
			col.writerow([cell.value for cell in r])

	#col.close()

	print("First line was removed and file saved as " + day + ".csv'")

print("Complete.")
