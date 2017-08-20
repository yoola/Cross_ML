import os
import random
from path_settings import init_paths
from findstring import find_value_SPLC, find_value, find_value_scriptAll

path_list = init_paths()
SPLC_script = path_list[0]
SPLC_log = path_list[6]
SPLC_logAll = path_list[10]

def init_SPLC(meas_, var_, numberofmeas_):

	interactive_ = input("Interactive mode for script settings? (y/n): ")

	confignumber_ = str("")
	seed_ = str("")

	if(interactive_=="y"):

		print("Press ENTER for default values.")
		minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
		numberOfRounds_ = input("Maximum measurements/rounds (default: ENTER): ")
		hierarchy_ = input("With Hierarchy? (y/n/ENTER): ")
		nfp_ = input("Type in the non functional property (default(Measured Value): ENTER): ")
		negfw_ = input("Negative feature wise sampling? (y/n/ENTER)): ")
		fws_ = input("Feature wise sampling? (y/n/ENTER): ")
		pws_ = input("Pairwise sampling? (y/n/ENTER): ")
		rdm_ = input("Random sampling? (y/n/ENTER): ")
		binaryft_ = input("Are all features binary? (y/n/ENTER): ")

		if(rdm_ == "y"):
			confignumber_ = input("[RANDOM sampling] How many configuration do you want to include?: ")
			seed_ = input("[RANDOM sampling] Type in a round number to initialize the seed: ")
		
		build_script_SPLC(interactive_, meas_, var_, numberofmeas_, str(minIPR_), str(numberOfRounds_), hierarchy_, nfp_, negfw_
						, fws_, pws_, rdm_, binaryft_, confignumber_, seed_)

	else:

		counter = 0
		combi_str = str("")
		with open(SPLC_script) as f:
		
			for line in f:

				if not (counter == 2 or counter ==3):
					combi_str = combi_str + line

				elif counter == 2:
					combi_str = combi_str + "vm "+var_+"\n"

				elif counter == 3:
					combi_str = combi_str + "all "+meas_+"\n"

				counter = counter +1
		f.close()

		script_ = open(SPLC_script, 'w')
		script_.write(combi_str)
		script_.close()


def change_script_SPLC(meas_, var_, numberofmeas_, iter, configs_):

	iter = iter -1

	if not configs_ == str(""):

		numberOfRounds_ = find_value_scriptAll(configs_, "numberOfRounds", iter)
		minIPR_ = find_value_scriptAll(configs_, "minIPR", iter)
		hierarchy_ = find_value_scriptAll(configs_, "hierarchy", iter)
		nfp_ = find_value_scriptAll(configs_, "nfp", iter)
		negfw_ = find_value_scriptAll(configs_, "negfw", iter)
		fws_ = find_value_scriptAll(configs_, "fws", iter)
		pws_ = find_value_scriptAll(configs_, "pws", iter)
		rdm_ = find_value_scriptAll(configs_, "rdm", iter)
		binaryft_ = find_value_scriptAll(configs_, "binaryft", iter)
		confignumber_ = find_value_scriptAll(configs_, "confignumber", iter)
		seed_ = find_value_scriptAll(configs_, "seed", iter)


	else:
		minIPR_list = [0.001, 0.01]
		numberOfRounds_list = [10,30,60,80] # 2*4 = 8
		negfw_list = ["y", "n"] # 8*2 = 16
		fws_list = ["y", "n"] # 16*2 = 32
		pws_list = ["y", "n"] # 32*2= 64
		rdm_list = ["y", "n"] # 64*2 = 128
		config_list = [1,5] # 128 * 2 = 256
		seed_list = [1,10] # 256*2 = 512 
	


		len_NOR = len(numberOfRounds_list)
		len_mIPR = len(minIPR_list)
		len_nfw = len(negfw_list)
		len_fws = len(fws_list)
		len_pws = len(pws_list)
		len_rdm = len(rdm_list)
		len_config = len(config_list)
		len_seed = len(seed_list)

		
		iter_nOR = iter%len_NOR
		iter_mIPR = int(iter/len_NOR)%len_mIPR # 3*8 = 24 rounds
		iter_nfw = int(iter/(len_NOR*len_mIPR))%len_nfw # 3*8*2 = 48 rounds
		iter_fws = int(iter/(len_NOR*len_mIPR*len_nfw))%len_fws # 3*8*2*2 = 96 rounds
		iter_pws = int(iter/(len_NOR*len_mIPR*len_nfw*len_fws))%len_pws # 3*8*2*2*2 = 192 rounds
		iter_rdm = int(iter/(len_NOR*len_mIPR*len_nfw*len_fws*len_pws))%len_rdm # 3*8*2*2*2*2 = 384 rounds
		iter_config = int(iter/(len_NOR*len_mIPR*len_nfw*len_fws*len_pws*len_rdm))%len_config # 3*8*2*2*2*3 = 1152 rounds
		iter_seed = int(iter/(len_NOR*len_mIPR*len_nfw*len_fws*len_pws*len_rdm*len_config))%len_seed # 3*8*2*2*2*2 = 4608 rounds


		numberOfRounds_ = numberOfRounds_list[iter_nOR]
		minIPR_ = minIPR_list[iter_mIPR]
		hierarchy_ = "n"
		nfp_ = "Measured Value"
		negfw_ = negfw_list[iter_nfw]
		fws_ = fws_list[iter_fws]
		pws_ = pws_list[iter_pws]
		rdm_ = rdm_list[iter_rdm]
		binaryft_ = "y"
		confignumber_ = config_list[iter_config]
		seed_ = seed_list[iter_seed]


		# uncomment below and comment above for random choice mode
		
		#minIPR_ = random.uniform(0.001, 0.1)
		#numberOfRounds_ = random.choice(range(5,25))#random.choice(range(10,int(numberofmeas_/2)))
		# hierarchy_ = random.choice(["y", "n"])
		# nfp_ = "Measured Value"
		# negfw_ = random.choice(["y", "n"])
		# if(negfw_ == "y"):
		# 	fws_ = "n"
		# else:
		# 	fws_ = "y"
		#pws_ = random.choice(["y", "n"])
		#rdm_ = "y" #random.choice(["y", "n"])
		#binaryft_ = random.choice(["y", "n"])

	build_script_SPLC("n", meas_, var_, numberofmeas_, str(minIPR_), str(numberOfRounds_), hierarchy_, nfp_, negfw_,
						fws_, pws_, rdm_, binaryft_, confignumber_, seed_)


def build_script_SPLC(interactive_, meas_, var_, numberofmeas_, minIPR_, numberOfRounds_, hierarchy_, 
						nfp_, negfw_, fws_, pws_, rdm_, binaryft_, confignumber_, seed_):

	#build script.a 	
	str1 = str("log "+SPLC_log)
	#str2 = str("limitFeatureSize:False featureSizeTreshold:4")
	if(minIPR_ ==""):
		minIPR_ = str("0.01");
	if(numberOfRounds_ == ""):
		numberOfRounds_ = int(numberofmeas_/2);
	if(hierarchy_=="y"):
		hierarchy_ = "True"
	else:
		hierarchy_ = "False"
	str2 = str("mlSettings abortError:1 minImprovementPerRound:"+minIPR_+" numberOfRounds:"+str(numberOfRounds_)+" withHierarchy:"+hierarchy_)
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
	if(interactive_== "y" and rdm_ =="y" and (confignumber_=="" or seed_=="")):
		str9 = str("random 2 3")
	elif(rdm_ == "y"):
		str9 = str("random "+str(confignumber_)+" "+str(seed_))	
	else:
		str9 = str("#random 2 3")
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
	script_.write("executionTime:"+exe_time+"; "+value_str)
	script_.close()

def parse_script_SPLC(exe_time):

	value_str = find_value_SPLC(SPLC_script)
	write_to_log(value_str, exe_time)

