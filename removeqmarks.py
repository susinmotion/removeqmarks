import csv

with open('filenames.csv','rU') as filelist:
	for files in filelist:	
		f = open(files.replace("\n",""), "rU")
		csv_f = csv.reader(f, dialect=csv.excel_tab)
		colnamesstr= csv_f.next()
		colnames=colnamesstr[0].upper().split(",")

		rows=[]
		for row in csv_f:
			rowaslist=[item for item in csv.reader([row[0]],skipinitialspace=True)][0]
			arow=(dict(zip(colnames, rowaslist)))
			#row.split() etc...
			if arow["LOCATIONOFTARGET"]!="?":
				rows.append(arow)
		
		newfilename=files.replace(".csv","ed.csv")
		with open(newfilename, 'wb') as f:
			w=csv.DictWriter(f, rows[0].keys())
			print rows[0].keys()
			print type(rows)
			w.writeheader()
			w.writerows(rows)
			#this is a dictionary. needs to be printed as csv with header just once