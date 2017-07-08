import os
import random
from path_settings import init_paths
from findstring import find_value_SPLC

path_list = init_paths()
SPLCext_script = path_list[13]
SPLCext_log = path_list[15]
SPLCext_logAll = path_list[16]

def init_SPLCext(meas_, var_, numberofmeas_):

	interactive_ = input("Interactive mode? (y/n): ")

	if(interactive_=="y"):

		print("This algorithm does not have any interactive mode yet.")

	else:

		counter = 0
		combi_str = str("")
		with open(SPLCext_script) as f:
		
			for line in f:

				if not (counter == 2 or counter ==3):
					combi_str = combi_str + line

				elif counter == 2:
					combi_str = combi_str + "vm "+var_+"\n"

				elif counter == 3:
					combi_str = combi_str + "all "+meas_+"\n"

				counter = counter +1
		f.close()

		script_ = open(SPLCext_script, 'w')
		script_.write(combi_str)
		script_.close()

def change_script_SPLCext(meas_, var_, numberofmeas_):

	minIPR_ = random.uniform(0.001, 0.1)
	numberofrounds_ = random.choice(range(10,int(numberofmeas_/2)))
	hierarchy_ = random.choice(["y", "n"])
	nfp_ = "Measured Value"
	negfw_ = random.choice(["y", "n"])
	if(negfw_ == "y"):
		fws_ = "n"
	else:
		fws_ = "y"
	pws_ = random.choice(["y", "n"])
	rdm_ = "y" #random.choice(["y", "n"])
	binaryft_ = random.choice(["y", "n"])

	build_script_SPLCext("n", meas_, var_, numberofmeas_, str(minIPR_), str(numberofrounds_), hierarchy_, nfp_, negfw_
						, fws_, pws_, rdm_, binaryft_)


def build_script_SPLCext(interactive_, meas_, var_, numberofmeas_, minIPR_, numberofrounds_, hierarchy_, nfp_, negfw_, fws_, pws_, rdm_, binaryft_):

	print("interactive: "+str(interactive_))
	#build script.a 	
	str1 = str("log "+SPLCext_log)
	#str2 = str("limitFeatureSize:False featureSizeTreshold:4")
	if(minIPR_ ==""):
		minIPR_ = str("0.01");
	if(numberofrounds_ == ""):
		numberofrounds_ = int(numberofmeas_/2);
	if(hierarchy_=="y"):
		hierarchy_ = "True"
	else:
		hierarchy_ = "False"
	str2 = str("mlSettings abortError:1 minImprovementPerRound:"+minIPR_+" numberOfRounds:"+str(numberofrounds_)+" withHierarchy:"+hierarchy_)
	str3 = str("vm "+var_)
	str4 = str("all "+meas_)
	if(nfp_ == ""):
		nfp_ = "Measured Value"
	str5 = str("nfp "+nfp_)

	if(negfw_=="y"):
		str6 = str("negfw")
	elif(negfw_=="n"):
		str6 = str("#negfw")
	else:
		str6 = str("negfw")
	if(fws_=="y"):
		str7 = str("featureWise")
	else:
		str7 = str("#featureWise")
	if(pws_=="y"):
		str8 = str("pairWise")
	else:
		str8 = str("#pairWise")
	if(rdm_ == "y" and interactive_ =="n"):
		str9 = str("random "+str(random.choice(["1", "7"]))+" "+str(random.choice(["1", "50"])))
	elif(rdm_ == "y"):
		confignumber_ = input("[RANDOM sampling] How many configuration do you want to include?: ")
		seed_ = input("[RANDOM sampling] Type in a round number to initialize the seed: ")
		str9 = str("random "+confignumber_+" "+seed_)
		if(confignumber_ == "" or seed_==""):
			str9 = str("#random")
	else:
		str9 = str("#random")
	if(binaryft_=="y"):
		str10 = str("allBinary")
	elif(binaryft_=="n"):
		str10 = str("#allBinary")
	else:
		str10 = str("allBinary")
	str11 = str("start")
	str12 = str("analyze-learning")
	str13 = str("clean-sampling")
	str14 = str("# clean-learning")
	str15 = str("# clean-global ")
		
	script_ = open(SPLCext_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8+'\n'+str9 
		+'\n'+str10+'\n'+str11+'\n'+str12+'\n'+str13+'\n'+str14+'\n'+str15)
	script_.close()

def write_to_log(value_str, exe_time):

	script_ = open(SPLCext_logAll, 'a')
	script_.write("executionTime:"+exe_time+"; "+value_str)
	script_.close()

def parse_script_SPLCext(exe_time):

	value_str = find_value_SPLC(SPLC_script)
	write_to_log(value_str, exe_time)

