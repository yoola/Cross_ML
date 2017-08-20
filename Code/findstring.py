
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

def find_value_SPLCext(file_path):
	with open(file_path) as f:
	
				value_str = str()
				sub_str = str()
				counter = 0
				

				for line in f:
					if "minImprovementPerRound" in line: # Finding string to start parsing document
						
						cut1 = line.find("\n")
						cut2 = 24
						for i in range(0,5):
							
							cut3 = line[cut2:cut1].find(" ")
							sub_str = sub_str + line[cut2:cut2+cut3] + "; "
							cut2 = cut2+cut3+1
						
						value_str = sub_str + line[cut2:cut1] +"; "

					if(counter>3 and counter<15):
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

def find_value_logAll2(log_lines, keystring):

	value_list = []
	for line in log_lines:
		if keystring in line:
			pos = line.find(keystring)
			cut = line[pos:].find(";")
			cut2 = line[:pos+cut].rfind(":")
			value = line[cut2+1:pos+cut]
			value_list.append(value)
											
	return value_list

def find_value_logAll_float(log_lines, keystring):

	value_list = []
	for line in log_lines:
		if keystring in line:
			pos = line.find(keystring)
			cut = line[pos:].find(";")
			cut2 = line[:pos+cut].rfind(":")
			value = line[cut2+1:pos+cut]
			value_list.append(float(value))
											
	return value_list

def find_value_logAll_int(log_lines, keystring):

	value_list = []
	for line in log_lines:
		if keystring in line:
			pos = line.find(keystring)
			cut = line[pos:].find(";")
			cut2 = line[:pos+cut].rfind(":")
			value = line[cut2+1:pos+cut]
			value_list.append(int(value))
											
	return value_list

def find_top_faultrates_lines_logAll(file_path, keystring, data_amount):

	top = [100]*data_amount
	top_lines = [""]*data_amount
	with open(file_path) as f:
	
				for line in f:
					if keystring in line: # Finding string to start parsing document
						pos = line.find(keystring)
						cut = line[pos:].find(";")
						len_ = len(keystring)
						value = line[pos+len_:pos+cut]

						pos_TR = line.find("TerminationReason: ")
						cut_TR = line[pos_TR:].find(";")
						len_TR = len("TerminationReason: ")
						value_TR = line[pos_TR+len_TR:pos_TR+cut_TR]


						
						pos = top.index(max(top))

						if float(value) < max(top) and not float(value) in top and not value_TR=="abortError":
								top[pos] = float(value)
								top_lines[pos] = line
	return top_lines

def find_flop_faultrates_lines_logAll(file_path, keystring, data_amount):

	flop = [0]*data_amount
	flop_lines = [""]*data_amount
	with open(file_path) as f:
	
				for line in f:
					if keystring in line: # Finding string to start parsing document
						pos = line.find(keystring)
						cut = line[pos:].find(";")
						len_ = len(keystring)
						value = line[pos+len_:pos+cut]


						pos_TR = line.find("TerminationReason: ")
						cut_TR = line[pos_TR:].find(";")
						len_TR = len("TerminationReason: ")
						value_TR = line[pos_TR+len_TR:pos_TR+cut_TR]
						
						pos = flop.index(min(flop))

						if float(value) > min(flop) and not float(value) in flop and not value_TR=="abortError":
								flop[pos] = float(value)
								flop_lines[pos] = line
	
	return flop_lines

def find_lines_logAll(file_path):

	line_list = []
	with open(file_path) as f:

		for line in f:

			line_list.append(line)

	return line_list

def find_value_scriptAll(file_path, keystring, iter):

	with open(file_path) as f:
		counter_ = 0
		value = str("")

		for line in f:
			if keystring in line and counter_ == iter: # Finding string to start parsing document
					pos = line.find(keystring)
					cut = line[pos:].find(";")
					len_ = len(keystring)
					value = line[pos+len_+1:pos+cut]
			counter_ = counter_+1

	return value

def find_explorerSPLCext_lines_logAll(file_path, keystring):

	lines_ = []

	with open(file_path) as f:
	
				for line in f:
					if keystring in line: # Finding string to start parsing document
						pos = line.find(keystring)
						cut = line[pos:].find(";")
						cut2 = line[:pos+cut].rfind(":")
						value = line[cut2+1:pos+cut]

						pos_TR = line.find("TerminationReason: ")
						cut_TR = line[pos_TR:].find(";")
						len_TR = len("TerminationReason: ")
						value_TR = line[pos_TR+len_TR:pos_TR+cut_TR]
						

						if value=="True" and not value_TR=="abortError":
								lines_.append(line)
	
	return lines_

def find_SPLC_feature_lines_logAll(file_path, negfw_val, fw_val, pw_val, rdm_val):

	lines_ = []

	with open(file_path) as f:
	
				for line in f:
					
					pos_negfw = line.find("negfw")
					cut_negfw = line[pos_negfw:].find(";")
					cut2_negfw = line[:pos_negfw+cut_negfw].rfind(":")
					value_negfw = line[cut2_negfw+1:pos_negfw+cut_negfw]

					pos_fw = line.find("featureWise")
					cut_fw = line[pos_fw:].find(";")
					cut2_fw = line[:pos_fw+cut_fw].rfind(":")
					value_fw = line[cut2_fw+1:pos_fw+cut_fw]

					pos_pw = line.find("pairWise")
					cut_pw = line[pos_pw:].find(";")
					cut2_pw = line[:pos_pw+cut_pw].rfind(":")
					value_pw = line[cut2_pw+1:pos_pw+cut_pw]

					pos_rdm = line.find("random")
					cut_rdm = line[pos_rdm:].find(";")
					cut2_rdm = line[:pos_rdm+cut_rdm].rfind(":")
					value_rdm = line[cut2_rdm+1:pos_rdm+cut_rdm]

					pos_TR = line.find("TerminationReason: ")
					cut_TR = line[pos_TR:].find(";")
					len_TR = len("TerminationReason: ")
					value_TR = line[pos_TR+len_TR:pos_TR+cut_TR]
					

					if value_negfw==negfw_val and value_fw==fw_val and value_pw==pw_val and value_rdm==rdm_val and not value_TR=="abortError":
							lines_.append(line)
	
	return lines_

