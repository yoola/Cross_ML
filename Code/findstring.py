
def find_value(file_path, keystring):
	with open(file_path) as f:
	
				value_ = ""
				for line in f:
					if keystring in line: # Finding string to start parsing document
						cut = line.find(";")
						len_ = len(keystring)
						value_ = line[len_:cut]
						
	
	return value_

def find_value_SPLC(file_path):
	with open(file_path) as f:
	
				value_str = str()
				sub_str = str()
				counter = 0
				

				for line in f:
					if "minImprovementPerRound" in line: # Finding string to start parsing document
						
						cut1 = line.find("\n")
						cut2 = 24
						for i in range(0,2):
							
							cut3 = line[cut2:cut1].find(" ")
							sub_str = sub_str + line[cut2:cut2+cut3] + "; "
							cut2 = cut2+cut3+1
						
						value_str = sub_str + line[cut2:cut1] +"; "

					if(counter>3 and counter<10):
						cut = line.find("\n")
						if(line[0]=="#"):
							value_str = value_str + line[1:cut]+":False; "
						else:
							value_str = value_str + line[:cut]+":True; "

					counter = counter +1
							
	return value_str


def find_value_logAll(file_path, keystring):
	with open(file_path) as f:
	
				value_list = []
				for line in f:
					if keystring in line: # Finding string to start parsing document
						pos = line.find(keystring)
						cut = line[pos:].find(";")
						len_ = len(keystring)
						value_list.append(line[pos+len_:pos+cut])
						
	
	return value_list



