import csv
import itertools

def conv_csv2xml(filepath):

	with open(filepath, 'r') as csvfile:
		r = csv.reader(csvfile, delimiter=',')
		csv_list =[]
		for row in r:
			csv_list.append(row) # get values of csv file, put them in a list
		csvfile.close()
	
	csv_size = len(csv_list[0])
	
	
	# create variability xml
	# check for relationships between features
	# e.g. rc_lookahead, rc_lookahead_40 => rc_lookahead is in rc_lookahead_40 => True (appending rc_lookahead_40 to child list)
	
	script1 = open("var.xml", 'w')
	
	elem_old = str()
	check = False
	elem_childs = []
	
	# csv_list[0][:] contains feature names
	for elem in csv_list[0][0:csv_size-1]:
	
		if elem_old:
			if elem_old in elem:
				elem_childs.append(elem)
				check = True
			else:
				check = False
	
		if check == False:
			elem_old = elem
	
	# write elements into script
	script1.write("<vm name=\"var_model\"> \n\t <binaryOptions>")
	elem_old = str()
	
	check = False
	for elem in csv_list[0][0:csv_size-1]:
	
		# feature has children
		if ((elem_old in elem) and elem_old):
	
			script1.write("\n\t\t <configurationOption> \n\t\t\t<name>"+elem.lower()+"</name>\n\t\t\t<outputString>"+elem.lower()+"</outputString>"
				+"\n\t\t\t<prefix>\n\t\t\t</prefix>\n\t\t\t<postfix>\n\t\t\t</postfix>\n\t\t\t<parent>"+elem_old.lower()+"</parent>\n\t\t\t<children />"
				+"\n\t\t\t<impliedOptions />\n\t\t\t<excludedOptions>")
	
			for p in elem_childs:
				if ((elem_old in p) and (p!=elem)):
					script1.write("\n\t\t\t\t<options>"+p.lower()+"</options>")
	
	
			script1.write("\n\t\t\t</excludedOptions>\n\t\t\t<defaultValue>Selected</defaultValue>"
				+"\n\t\t\t<optional>False</optional>\n\t\t</configurationOption>")
	
			check = True

		# feature has no children
		else:
			check = False
			script1.write("\n\t\t <configurationOption> \n\t\t\t<name>"+elem.lower()+"</name>\n\t\t\t<outputString>"+elem.lower()+"</outputString>"
				+"\n\t\t\t<prefix>\n\t\t\t</prefix>\n\t\t\t<postfix>\n\t\t\t</postfix>\n\t\t\t<parent>\n\t\t\t</parent>\n\t\t\t<children />"
				+"\n\t\t\t<impliedOptions />\n\t\t\t<excludedOptions /> \n\t\t\t<defaultValue>Selected</defaultValue>")

			check2 = False
			for q in elem_childs:
				if(elem in q):
					check2 = True

			if(check2 == True):
				script1.write("\n\t\t\t<optional>False</optional>\n\t\t</configurationOption>")

			else:
				script1.write("\n\t\t\t<optional>True</optional>\n\t\t</configurationOption>")
	
		if check==False:
			elem_old = elem
	
	script1.write( "\n\t </binaryOptions> \n\t<numericOptions /> \n </vm>")
	script1.close()
	
	
	
	# create measurement xml	
	script2 = open("meas.xml", 'w')
	script2.write("<results>")
	
	for i in range(1,len(csv_list)):
		j = 0
		config = str()
		
		# get chosen features ('Y') for each configuration
		for elem in csv_list[i][0:csv_size-1]:
			if elem == 'Y':
				config += csv_list[0][j].lower()+","
			j += 1
		#print(config)
	
		#replace . with , in performance number
		csv_list[i][csv_size-1] = csv_list[i][csv_size-1].replace(".", ",")
	
		# write down configuration with related performance number
		script2.write("\n\t<row>\n\t\t<data columname=\"Configuration\">"+config+"</data>"
						+"\n\t\t<data columname=\"Measured Value\">"+csv_list[i][csv_size-1]+"</data>\n\t</row>")
	
	script2.write( "\n</results>")
	script2.close()