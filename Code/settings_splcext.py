import os
import random
from path_settings import init_paths
from findstring import find_value_SPLCext, find_value_scriptAll

path_list = init_paths()
SPLCext_script = path_list[13]
SPLCext_log = path_list[15]
SPLCext_logAll = path_list[16]

def init_SPLCext(meas_, var_, numberofmeas_):

	interactive_ = input("Interactive mode for script settings? (y/n): ")

	internalRoundsPerCycle_ = str("")
	batchSizeExploit_ = str("")
	batchSizeExplore_ = str("")
	sleepCycles_ = str("")
	sleepRoundsExplore_ = str("")
	batchsize_ = str("")


	if(interactive_=="y"):

		print("Press ENTER for default values.")

		minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
		numberOfRounds_ = input("Maximum measurements/rounds (default: ENTER): ")
		hierarchy_ = input("With Hierarchy? (y/n/ENTER): ")
		parallelization_  = input("With parallelization? (y/n/ENTER): ")
		bagging_ = input("With bagging? (y/n/ENTER): ")
		crossValidation_ = input("With crossValidation? (y/n/ENTER): ")

		expl_rdm = input("explorer-random? (y/n/ENTER): ")
		expl_max_dist = input("explorer-max-distance? (y/n/ENTER): ")
		expl_max_err = input("explorer-max-error? (y/n/ENTER): ")
		expl_combi = input("explorer-combi? (y/n/ENTER): ")	
		expl_omni = input("explorer-omni? (y/n/ENTER): ")

		if(expl_max_dist =="y"):
			internalRoundsPerCycle_ = input("[explorer-max-error] Internal Rounds Per Cycle?: ")
			batchSizeExploit_ = input("[explorer-max-error] BatchSize Exploit?: ")
			batchSizeExplore_ = input("[explorer-max-error] BatchSize Explore?: ")
			sleepCycles_ = input("[explorer-max-error] How many sleep cycles?: ")
			sleepRoundsExplore_ = input("[explorer-max-error] How many sleep rounds explore?: ")

		elif not expl_omni=="y":
			batchsize_ = input("[explorer-random] Batchsize?: ")
			sleepCycles_ = input("[explorer-random] How many sleep cycles?: ")

		
		build_script_SPLCext(interactive_, meas_, var_, numberofmeas_, str(minIPR_), str(numberOfRounds_), 
			hierarchy_, bagging_, parallelization_, crossValidation_, expl_rdm, expl_max_dist, expl_max_err, expl_combi, expl_omni,
			internalRoundsPerCycle_, batchSizeExploit_, batchSizeExplore_, sleepRoundsExplore_, batchsize_, sleepCycles_)

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

def change_script_SPLCext(meas_, var_, numberofmeas_, iter, configs_):


	iter = iter -1

	if not configs_ == str(""):

		numberOfRounds_ = find_value_scriptAll(configs_, "numberOfRounds", iter)
		minIPR_ = find_value_scriptAll(configs_, "minIPR", iter)

		hierarchy_ = find_value_scriptAll(configs_, "hierarchy", iter)
		parallelization_ =  find_value_scriptAll(configs_, "parallelization", iter)
		bagging_ = find_value_scriptAll(configs_, "bagging", iter)
		crossValidation_ = find_value_scriptAll(configs_, "crossValidation", iter)

		expl_rdm = find_value_scriptAll(configs_, "expl_rdm", iter)
		expl_max_dist = find_value_scriptAll(configs_, "expl_max_dist", iter)
		expl_max_err = find_value_scriptAll(configs_, "expl_max_err", iter)
		expl_combi = find_value_scriptAll(configs_, "expl_combi", iter)
		expl_omni = find_value_scriptAll(configs_, "expl_omni", iter)

		sleepCycles_ = find_value_scriptAll(configs_, "sleepCycles", iter)
		batchsize_ = find_value_scriptAll(configs_, "batchsize", iter)
		internalRoundsPerCycle_ = find_value_scriptAll(configs_, "internalRoundsPerCycle", iter)
		batchSizeExploit_ = find_value_scriptAll(configs_, "batchSizeExploit", iter)
		batchSizeExplore_ = find_value_scriptAll(configs_, "batchSizeExplore", iter)
		sleepRoundsExplore_ = find_value_scriptAll(configs_, "sleepRoundsExplore", iter)
	

	else:
		minIPR_list = [0.01, 0.1]
		numberOfRounds_list = [10]
		expl_list = ["expl_rdm", "expl_max_dist", "expl_max_err", "expl_combi", "expl_omni"]
		sleepCycles_list = [0,1,2,3,4,5]
		batchsize_list = [3,5,8,10,15,20,30,40]
		internalRoundsPerCycle_list = [1,2,3,4,5,6,10,15]
		batchSizeExploit_list = [1,2,3,4,5,10,15]
		batchSizeExplore_list = [1,2,3,4,5,10,15]
		sleepRoundsExplore_list = [1,2,3,4,5,10]

		len_NOR = len(numberOfRounds_list)
		len_mIPR = len(minIPR_list)
		len_expl = len(expl_list)	
		len_sC = len(sleepCycles_list)
		len_bS = len(batchsize_list)
		len_iRPC = len(internalRoundsPerCycle_list)
		len_bSExploit = len(batchSizeExploit_list)
		len_bSExplore = len(batchSizeExplore_list)
		len_sRE = len(sleepRoundsExplore_list)
	
		iter_nOR = iter%len_NOR
		iter_mIPR = int(iter/len_NOR)%len_mIPR 
		iter_expl = int(iter/(len_NOR*len_mIPR))%len_expl 
		iter_sC = int(iter/(len_NOR*len_mIPR*len_expl))%len_sC 
		iter_bS = int(iter/(len_NOR*len_mIPR*len_expl*len_sC))%len_bS 
		iter_iRPC = int(iter/(len_NOR*len_mIPR*len_expl*len_sC*len_bS))%len_iRPC 
		iter_bSExploit = int(iter/(len_NOR*len_mIPR*len_expl*len_sC*len_bS*len_iRPC))%len_bSExploit
		iter_bSExplore = int(iter/(len_NOR*len_mIPR*len_expl*len_sC*len_bS*len_iRPC*len_bSExploit))%len_bSExplore 
		iter_sRE = int(iter/(len_NOR*len_mIPR*len_expl*len_sC*len_bS*len_iRPC*len_bSExploit*len_bSExplore))%len_sRE 


		numberOfRounds_ = numberOfRounds_list[iter_nOR]
		minIPR_ = minIPR_list[iter_mIPR]
		expl_ = expl_list[iter_expl]
		print("expl: "+str(expl_))

		hierarchy_ = str("n")
		parallelization_ =  str("n")
		bagging_ = str("n")
		crossValidation_ = str("n")

		expl_rdm = "n"
		expl_max_dist = "n"
		expl_max_err = "n"
		expl_combi = "n"
		expl_omni = "n"

		if(expl_ == "expl_rdm"):
			expl_rdm = "y"
		elif(expl_ == "expl_max_dist"):
			expl_omni = "y"
		elif(expl_ == "expl_max_err"):
			expl_max_err = "y"
		elif(expl_ == "expl_combi"):
			expl_combi = "y"
		elif(expl_ == "expl_omni"):
			expl_omni = "y"
		

		sleepCycles_ = sleepCycles_list[iter_sC]
		batchsize_ = batchsize_list[iter_bS]
		internalRoundsPerCycle_ = internalRoundsPerCycle_list[iter_iRPC]
		batchSizeExploit_ = batchSizeExploit_list[iter_bSExploit]
		batchSizeExplore_ = batchSizeExplore_list[iter_bSExplore]
		sleepRoundsExplore_ = sleepRoundsExplore_list[iter_sRE]
	
		print("expl_rdm: "+expl_rdm+", expl_max_dist: "+expl_max_dist+", expl_max_err: "+expl_max_err+", expl_combi: "+expl_combi+", expl_omni: "+expl_omni+"\n")
		print("internalRoundsPerCycle_: "+str(internalRoundsPerCycle_)+", batchSizeExploit_: "+str(batchSizeExploit_)+", batchSizeExplore_: "+str(batchSizeExplore_)
			+", sleepRoundsExplore_: "+str(sleepRoundsExplore_)+", sleepCycles_: "+str(sleepCycles_)+", batchsize_: "+str(batchsize_))
	


		# uncomment below and comment above for random choice mode

		# minIPR_ = random.uniform(0.001, 0.1)
		# numberOfRounds_ = random.choice(range(5,25)) #random.choice(range(10,int(numberofmeas_/2)))
		# hierarchy_ = str("n")
		# parallelization_ =  str("n")
		# bagging_ = str("n")
		# crossValidation_ = str("n")

		# expl_rdm = "n"
		# expl_max_dist = "n"
		# expl_max_err = "n"
		# expl_combi = "y"
		# expl_omni = "n"

	build_script_SPLCext("n", meas_, var_, numberofmeas_,  str(minIPR_), str(numberOfRounds_), 
		hierarchy_, bagging_, parallelization_, crossValidation_, expl_rdm, expl_max_dist, expl_max_err, expl_combi, expl_omni,
		internalRoundsPerCycle_, batchSizeExploit_, batchSizeExplore_, sleepRoundsExplore_, batchsize_, sleepCycles_)


def build_script_SPLCext(interactive_, meas_, var_, numberofmeas_,  minIPR_, numberOfRounds_, 
	hierarchy_, bagging_, parallelization_, crossValidation_, expl_rdm, expl_max_dist, expl_max_err, expl_combi, expl_omni,
	internalRoundsPerCycle_, batchSizeExploit_, batchSizeExplore_, sleepRoundsExplore_, batchsize_, sleepCycles_):

	#build script.a 	
	str1 = str("log "+SPLCext_log)
	#str2 = str("limitFeatureSize:False featureSizeTreshold:4")
	if(minIPR_ ==""):
		minIPR_ = str("0.01");
	if(numberOfRounds_ == ""):
		numberOfRounds_ = int(numberofmeas_/16);
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
		+str(numberOfRounds_)+" withHierarchy:"+hierarchy_+" parallelization:"+parallelization_
		+" bagging:"+bagging_+" crossValidation:"+crossValidation_)
	str3 = str("vm "+var_)
	str4 = str("all "+meas_)
	str5 = str("nfp Measured Value")
	str6 = str("#negfw")
	str7 = str("#featureWise")
	str8 = str("#pairWise")
	str9 = str("#random")
	str10 = str("allBinary")

	if not(expl_rdm =="y"):
		expl_rdm = str("n")
	if not(expl_max_dist =="y"):
		expl_max_dist = str("n")
	if not(expl_max_err =="y"):
		expl_max_err = str("n")
	if not(expl_combi =="y"):
		expl_combi = str("n")
	if not(expl_omni =="y"):
		expl_omni = str("n")

	if(interactive_== "y" and expl_rdm =="y" and (batchsize_=="" or sleepCycles_=="")):
		str11 = str("explorer-random batchSize:10 sleepCycles:1")
	elif(expl_rdm == "y"):
		str11 = str("explorer-random batchSize:"+str(batchsize_)+" sleepCycles:"+str(sleepCycles_))	
	elif(expl_rdm == "n"):
		str11 = str("#explorer-random batchSize:10 sleepCycles:1")

	
	if(interactive_ == "y" and expl_max_dist =="y" and (batchsize_=="" or sleepCycles_=="")):
		str12 = str("explorer-max-distance batchSize:10 sleepCycles:1")
	elif(expl_max_dist == "y"):
		str12 = str("explorer-max-distance batchSize:"+str(batchsize_)+" sleepCycles:"+str(sleepCycles_))
	else:
		str12 = str("#explorer-max-distance batchSize:10 sleepCycles:1")


	if(interactive_=="y" and expl_max_err=="y" and (internalRoundsPerCycle_=="" or batchSizeExploit_=="" or batchSizeExplore_=="" or sleepCycles_=="" or sleepRoundsExplore_=="")):
		str13 = str("explorer-max-error internalRoundsPerCycle:2 batchSizeExploit:3 batchSizeExplore:4 sleepCycles:1 sleepRoundsExplore:1")
	elif(expl_max_err == "y"):
		str13 = str("explorer-max-error internalRoundsPerCycle:"+str(internalRoundsPerCycle_)
			+" batchSizeExploit:"+str(batchSizeExploit_)+" batchSizeExplore:"
			+str(batchSizeExplore_)+" sleepCycles:"+str(sleepCycles_)+ " sleepRoundsExplore:"+str(sleepRoundsExplore_))
	else:
		str13 = str("#explorer-max-error internalRoundsPerCycle:2 batchSizeExploit:3 batchSizeExplore:4 sleepCycles:1 sleepRoundsExplore:1")


	if(interactive_=="y" and expl_combi=="y" and (batchsize_=="" or sleepCycles_=="")):
		str14 = str("explorer-combi batchSize:20 sleepCycles:2")
	elif(expl_combi == "y"):
		str14 = str("explorer-combi batchSize:"+str(batchsize_)+" sleepCycles:"+str(batchsize_))
	else:
		str14 = str("#explorer-combi batchSize:20 sleepCycles:2")


	if(expl_omni == "y"):
		str15 = str("explorer-omni")
	else:
		str15 = str("#explorer-omni")
	
	str16 = str("start")
	str17 = str("analyze-learning")
	str18 = str("clean-sampling")
	str19 = str("#clean-learning")
	str20 = str("#clean-global ")
		
	script_ = open(SPLCext_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8+'\n'+str9 
		+'\n'+str10+'\n'+str11+'\n'+str12+'\n'+str13+'\n'+str14+'\n'+str15+'\n\n'+str16+'\n'+str17+'\n'+str18
		+'\n'+str19+'\n'+str20)
	script_.close()

def write_to_log(value_str, exe_time):

	script_ = open(SPLCext_logAll, 'a')
	script_.write("executionTime:"+exe_time+"; "+value_str)
	script_.close()

def parse_script_SPLCext(exe_time):

	value_str = find_value_SPLCext(SPLCext_script)
	write_to_log(value_str, exe_time)

