import csv
import xml
import xml.etree.ElementTree as ET

def conv_xml2csv(meas_path, var_path):

	# parse variability model file for feature names
	tree = ET.parse(var_path)
	root = tree.getroot()
	
	name = []
	
	for child in root:
	 	for sub_child in (child):
	
	 		name.append(sub_child.find('name').text)
	 		# outputString = sub_child.find('outputString').text
	 		# prefix = sub_child.find('prefix').text
	 		# postfix = sub_child.find('postfix').text
	 		# parent = sub_child.find('parent').text
	 		# defaultValue = sub_child.find('defaultValue').text
	 		# optional = sub_child.find('optional').text
	 		
	 		#print('name: '+ name +'\n'+ 'outputString: '+ outputString +'\n'
	 		#		 +'prefix: '+prefix +'\n'+ 'postfix:' + postfix +'\n'+ 'parent: '+parent +'\n' 
	 		#		 +'defaultValue: '+ defaultValue +'\n'+ 'optional: '+optional +'\n ---------------------------')
	 		
	
	# parse measurement file for chosen configurations and performance number
	
	tree = ET.parse(meas_path)
	root = tree.getroot()
	
	counter = 0

	
	for child in root:
		data = child.find('data').text
		counter += 1 # count configurations in file
	
	meas_values = []
	config_values = []
	
	for j in range(0,counter):

		meas_values.append(root[j][1].text)		
		config_values.append(root[j][0].text) 
	 	
	 
	
	b_name = []
	p = 0;

	# check if feature is in list (a 'Y' in csv) or not (a 'N' in csv)
	
	for config in config_values:
	
		for i in range(0,len(name)):
	
			if name[i] in config:
				b_name.append('Y')
			else:
				b_name.append('N')
		meas_values[p] = meas_values[p].replace(",", ".")
		b_name.append(meas_values[p])	
		p += 1
	
	
	# writing all selected xml data to csv file

	with open('test.csv','w', newline ='') as fp:
		a = csv.writer(fp, delimiter=',')
		name.append('PERF')
		data= [name]
		a.writerows(data)
		i=0
		j=len(name)
		for l in range(0,len(config_values)):
			a.writerows([b_name[i:j]])
			i += len(name)
			j += len(name)

	