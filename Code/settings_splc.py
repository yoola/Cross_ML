import os
import random
from path_settings import init_paths
from findstring import find_value_SPLC

path_list = init_paths()
SPLC_script = path_list[0]
SPLC_log = path_list[6]
SPLC_logAll = path_list[10]

def init_SPLC(meas_, var_, numberofmeas_):

	interactive_ = input("Interactive mode? (y/n): ")

	if(interactive_=="y"):

		print("Press ENTER for default values.")
		minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
		numberofrounds_ = input("Maximum measurements (default: ENTER): ")
		hierarchy_ = input("With Hierarchy? (y/n/ENTER): ")
		nfp_ = input("Type in the non functional property (default(Measured Value): ENTER): ")
		negfw_ = input("Negative feature wise sampling? (y/n/ENTER)): ")
		fws_ = input("Feature wise sampling? (y/n/ENTER): ")
		pws_ = input("Pairwise sampling? (y/n/ENTER): ")
		rdm_ = input("Random sampling? (y/n/ENTER): ")
		binaryft_ = input("Are all features binary? (y/n/ENTER): ")

		build_script_SPLC(meas_, var_, numberofmeas_, str(minIPR_), str(numberofrounds_), hierarchy_, nfp_, negfw_
						, fws_, pws_, rdm_, binaryft_)

		

def change_script_SPLC(meas_, var_, numberofmeas_):

	minIPR_ = random.uniform(0.001, 0.1)
	numberofrounds_ = random.choice(range(10,int(numberofmeas_/2)))
	hierarchy_ = random.choice(["y", "n"])
	nfp_ = "Measured Value"
	negfw_ = random.choice(["y", "n"])
	if(negfw_ == "y"):
		fws_ = "n"
	else:
		fws_ = random.choice(["y", "n"])
	pws_ = random.choice(["y", "n"])
	rdm_ = str(random.choice(["1", "7"]))+" "+str(random.choice(["1", "50"]))
	binaryft_ = random.choice(["y", "n"])

	build_script_SPLC(meas_, var_, numberofmeas_, str(minIPR_), str(numberofrounds_), hierarchy_, nfp_, negfw_
						, fws_, pws_, rdm_, binaryft_)


def build_script_SPLC(meas_, var_, numberofmeas_, minIPR_, numberofrounds_, hierarchy_, nfp_, negfw_, fws_, pws_, rdm_, binaryft_):

	#build script.a 	
	str1 = str("log "+SPLC_log)
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
	if(rdm_ == "y"):
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
		
	script_ = open(SPLC_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8+'\n'+str9 
		+'\n'+str10+'\n'+str11+'\n'+str12+'\n'+str13+'\n'+str14+'\n'+str15)
	script_.close()

def write_to_log(value_str, exe_time):

	script_ = open(SPLC_logAll, 'a')
	script_.write("executionTime: "+exe_time+" "+value_str+"\n")
	script_.close()

def parse_script_SPLC(exe_time):

	value_str = find_value_SPLC(SPLC_script)
	write_to_log(value_str, exe_time)

