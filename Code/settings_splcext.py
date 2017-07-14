import os
import random
from path_settings import init_paths
from findstring import find_value_SPLCext

path_list = init_paths()
SPLCext_script = path_list[13]
SPLCext_log = path_list[15]
SPLCext_logAll = path_list[16]

def init_SPLCext(meas_, var_, numberofmeas_):

	interactive_ = input("Interactive mode? (y/n): ")

	if(interactive_=="y"):

		print("Press ENTER for default values.")

		minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
		numberofrounds_ = input("Maximum measurements/rounds (default: ENTER): ")
		hierarchy_ = input("With Hierarchy? (y/n/ENTER): ")
		parallelization_  = input("With parallelization? (y/n/ENTER): ")
		bagging_ = input("With bagging? (y/n/ENTER): ")
		crossValidation_ = input("With crossValidation? (y/n/ENTER): ")

		expl_rdm = input("explorer-random? (y/n/ENTER): ")
		expl_max_dist = input("explorer-max-distance? (y/n/ENTER): ")
		expl_max_err = input("explorer-max-error? (y/n/ENTER): ")
		expl_combi = input("explorer-combi? (y/n/ENTER): ")	
		expl_omni = input("explorer-omni? (y/n/ENTER): ")
		
		build_script_SPLCext(interactive_, meas_, var_, numberofmeas_, str(minIPR_), str(numberofrounds_), hierarchy_, bagging_, parallelization_, crossValidation_, expl_rdm, expl_max_dist, expl_max_err, expl_combi, expl_omni)

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
	numberofrounds_ = random.choice(range(5,25)) #random.choice(range(10,int(numberofmeas_/2)))
	hierarchy_ = random.choice(["y", "n"])
	parallelization_ =  str("n")
	bagging_ = str("n")
	crossValidation_ = str("n")

	expl_rdm = "n"
	expl_max_dist = "n"
	expl_max_err = "n"
	expl_combi = "y"
	expl_omni = "n"

	build_script_SPLCext("n", meas_, var_, numberofmeas_,  str(minIPR_), str(numberofrounds_), hierarchy_, bagging_, parallelization_, crossValidation_, expl_rdm, expl_max_dist, expl_max_err, expl_combi, expl_omni)


def build_script_SPLCext(interactive_, meas_, var_, numberofmeas_,  minIPR_, numberofrounds_, hierarchy_, bagging_, parallelization_, crossValidation_, expl_rdm, expl_max_dist, expl_max_err, expl_combi, expl_omni):

	#build script.a 	
	str1 = str("log "+SPLCext_log)
	#str2 = str("limitFeatureSize:False featureSizeTreshold:4")
	if(minIPR_ ==""):
		minIPR_ = str("0.01");
	if(numberofrounds_ == ""):
		numberofrounds_ = int(numberofmeas_/16);
	if(hierarchy_=="y"):
		hierarchy_ = "True"
	else:
		hierarchy_ = "False"
	if(parallelization_=="y"):
		parallelization_ = "True"
	else:
		parallelization_ = "False"
	if(bagging_=="y"):
		bagging_ = "True"
	else:
		bagging_ = "False"
	if(crossValidation_=="y"):
		crossValidation_ = "True"
	else:
		crossValidation_ = "False"
	str2 = str("mlSettings abortError:1 minImprovementPerRound:"+minIPR_+" numberOfRounds:"
		+str(numberofrounds_)+" withHierarchy:"+hierarchy_+" parallelization:"+parallelization_
		+" bagging:"+bagging_+" crossValidation:"+crossValidation_)
	str3 = str("vm "+var_)
	str4 = str("all "+meas_)
	str5 = str("nfp Measured Value")
	str6 = str("#negfw")
	str7 = str("#featureWise")
	str8 = str("#pairWise")
	str9 = str("#random")
	str10 = str("allBinary")


	if(expl_rdm == "y" and interactive_ =="n"):
		str11 = str("explorer-random batchSize:"+str(random.choice(["5", "20"]))+" sleepCycles:"
			+str(random.choice(["1", "5"])))
	elif(expl_rdm == "y"):
		batchsize_ = input("[explorer-random] Batchsize?: ")
		sleepCycles_ = input("[explorer-random] How many sleep cycles?: ")
		str11 = str("explorer-random batchsize:"+batchsize_+" sleepCycles:"+sleepCycles_)
		if(batchsize_ == "" or sleepCycles_==""):
			str11 = str("explorer-random batchSize:10 sleepCycles:1")
	else:
		str11 = str("#explorer-random batchSize:10 sleepCycles:1")
	


	if(expl_max_dist == "y" and interactive_ =="n"):
		str12 = str("explorer-max-distance batchSize:"+str(random.choice(["5", "20"]))+" sleepCycles:"
			+str(random.choice(["1", "5"])))
	elif(expl_max_dist == "y"):
		batchsize_ = input("[explorer-max-distance] BatchSize?: ")
		sleepCycles_ = input("[explorer-max-distance] How many sleep cycles?: ")
		str12 = str("explorer-max-distance batchsize:"+batchsize_+" sleepCycles:"+sleepCycles_)
		if(batchsize_ == "" or sleepCycles_==""):
			str12 = str("explorer-max-distance batchSize:10 sleepCycles:1")
	else:
		str12 = str("#explorer-max-distance batchSize:10 sleepCycles:1")


	if(expl_max_err == "y" and interactive_ =="n"):
		str13 = str("explorer-max-error internalRoundsPerCycle:"+str(random.choice(["1", "5"]))
			+" batchSizeExploit:"+str(random.choice(["1", "5"]))+" batchSizeExplore:"
			+str(random.choice(["1", "5"]))+" sleepCycles:"+str(random.choice(["1", "5"])) + "sleepRoundsExplore:"+str(random.choice(["1", "5"])))
	elif(expl_max_err  == "y"):
		internalRoundsPerCycle_ = input("[explorer-max-error] Internal Rounds Per Cycle?: ")
		batchSizeExploit_ = input("[explorer-max-error] BatchSize Exploit?: ")
		batchSizeExplore_ = input("[explorer-max-error] BatchSize Explore?: ")
		sleepCycles_ = input("[explorer-max-error] How many sleep cycles?: ")
		sleepRoundsExplore_ = input("[explorer-max-error] How many sleep rounds explore?: ")
		str13 = str("explorer-max-error internalRoundsPerCycle:"+internalRoundsPerCycle_+" batchSizeExploit:"
			+batchSizeExploit_+" batchSizeExplore:"+batchSizeExplore_ +" sleepCycles:"+sleepCycles_ 
			+"sleepRoundsExplore:"+sleepRoundsExplore_)
		if(internalRoundsPerCycle_ == "" or batchSizeExploit_=="" or batchSizeExplore_ == "" or sleepCycles_=="" or sleepRoundsExplore_==""):
			str13 = str("explorer-max-error internalRoundsPerCycle:2 batchSizeExploit:3 batchSizeExplore:4 sleepCycles:1 sleepRoundsExplore:1")
	else:
		str13 = str("#explorer-max-error internalRoundsPerCycle:2 batchSizeExploit:3 batchSizeExplore:4 sleepCycles:1 sleepRoundsExplore:1")


	if(expl_combi == "y" and interactive_ =="n"):
		str14 = str("explorer-combi batchSize:"+str(random.choice(["5", "20"]))+" sleepCycles:"
			+str(random.choice(["1", "5"])))
	elif(expl_combi == "y"):
		batchsize_ = input("[explorer-combi] Batchsize?: ")
		sleepCycles_ = input("[explorer-combi] How many sleep cycles?: ")
		str14 = str("explorer-combi batchsize:"+batchsize_+" sleepCycles:"+sleepCycles_)
		if(batchsize_ == "" or sleepCycles_==""):
			str14 = str("explorer-combi batchSize:20 sleepCycles:2")
	else:
		str14 = str("#explorer-combi batchSize:20 sleepCycles:2")


	if(expl_omni == "y"):
		str15 = str("explorer-omni")
	else:
		str15 = str("#explorer-omni")
	
	str16 = str("start")
	str17 = str("#analyze-learning")
	str18 = str("clean-sampling")
	str19 = str("#clean-learning")
	str20 = str("#clean-global ")
		
	script_ = open(SPLCext_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8+'\n'+str9 
		+'\n'+str10+'\n\n'+str11+'\n'+str12+'\n'+str13+'\n'+str14+'\n'+str15+'\n\n'+str16+'\n'+str17+'\n'+str18
		+'\n'+str19+'\n'+str20)
	script_.close()

def write_to_log(value_str, exe_time):

	script_ = open(SPLCext_logAll, 'a')
	script_.write("executionTime:"+exe_time+"; "+value_str)
	script_.close()

def parse_script_SPLCext(exe_time):

	value_str = find_value_SPLCext(SPLCext_script)
	write_to_log(value_str, exe_time)

