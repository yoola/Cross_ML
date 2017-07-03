	
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
				counter = 0
				for line in f:
					if "minImprovementPerRound" in line: # Finding string to start parsing document
						cut = line.find("\n")
						value_str = value_str + line[24:cut]+"; "

					if(counter>3 and counter<10):
						cut = line.find("\n")
						if(line[0]=="#"):
							value_str = value_str + line[1:cut]+": False; "
						else:
							value_str = value_str + line[:cut]+": True; "

					counter = counter +1
							
	return value_str

