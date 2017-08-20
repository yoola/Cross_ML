import os
import random
from path_settings import init_paths
from findstring import find_value, find_value_scriptAll

path_list = init_paths()
SARKAR_script = path_list[2]
SARKAR_logAll = path_list[12]

def init_SARKAR(numberofmeas_):

	interactive_ = input("Interactive mode for script settings? (y/n): ")

	if(interactive_=="y"):

		minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
		numberOfRepPerRound_ = input("Number of repetitions per round for the same sample amount (default(5): ENTER): ")
		numberOfRounds_ = input("Maximum measurements/rounds (default: ENTER): ")

		if(minIPR_ ==""):
			minIPR_ = str("0.01")
		if(numberOfRepPerRound_ ==""):
			numberOfRepPerRound_ = str("5")
		if(numberOfRounds_==""):
			numberOfRounds_ = str(int(numberofmeas_/8))
	
		build_script_SARKAR(numberOfRepPerRound_, minIPR_, numberOfRounds_)


def change_script_SARKAR(iter, configs_):

	iter = iter -1

	if not configs_ == str(""):

		numberOfRepPerRound_ = find_value_scriptAll(configs_, "numberOfRepPerRound", iter)
		minIPR_ = find_value_scriptAll(configs_, "minImprovementPerRound", iter)
		numberOfRounds_ = find_value_scriptAll(configs_, "numberOfRounds", iter)

	else:
		minIPR_list = [0.001, 0.01, 0.1]
		numberOfRounds_list = [10, 20, 30, 40, 50, 60, 70, 80]
		numberOfRepPerRound_list = [1, 2, 3]
		len_NOR = len(numberOfRounds_list)
		len_mIPR = len(minIPR_list)
		len_nORPR = len(numberOfRepPerRound_list)
		
	
		iter_nOR = iter%len_NOR
		iter_mIPR = int(iter/len_NOR)%len_mIPR # 3*9 = 27 rounds
		iter_nORPR = int(iter/(len_NOR*len_mIPR))%len_nORPR   # 3*27 =  81 rounds

		numberOfRounds_ = numberOfRounds_list[iter_nOR]
		minIPR_ = minIPR_list[iter_mIPR]
		numberOfRepPerRound_ = numberOfRepPerRound_list[iter_nORPR]
	
		# minIPR_ = random.uniform(0.001, 0.1)
		#numberOfRepPerRound_ = random.choice(range(1,9))
		# numberOfRounds_ = random.choice(range(11,90))
	build_script_SARKAR(str(numberOfRepPerRound_), str(minIPR_), str(numberOfRounds_))


def build_script_SARKAR(numberOfRepPerRound_, minIPR_, numberOfRounds_):

	#build script_SARKAR.R 	
	str1 = str("numberOfRepPerRound <- "+numberOfRepPerRound_+"; #number of times experiment should be repeated")
	str2 = str("minImprovementPerRound <- "+minIPR_+"; #complexity step")
	str3 = str("numberOfRounds <- "+numberOfRounds_+"; #complexity step")
	str4 = str("#progression base #(default = 1)")
	str5 = str("#sampling range lower value #(default = 1)")
	str6 = str("#sampling range upper value #(default = 1)")
	str7 = str("#sampling progression #(default = 1)")
	str8 = str("#complexLower #complexity range lower value #default = 0")
	str9 = str("#complexUpper #complexity range upper value # default = 0.001")

	script_ = open(SARKAR_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8 +'\n'+str9)
	script_.close()


def write_to_log(numberOfRepPerRound_, minIPR_, numberOfRounds_, exe_time):

	script_ = open(SARKAR_logAll, 'a')
	script_.write("executionTime:"+exe_time+"; numberOfRepPerRound:"+numberOfRepPerRound_+"; minImprovementPerRound:"+minIPR_+"; numberOfRounds:"+numberOfRounds_+"; ")
	script_.close()


def parse_script_SARKAR(exe_time):

	numberOfRepPerRound_ = find_value(SARKAR_script, "numberOfRepPerRound <- ")
	minIPR_ = find_value(SARKAR_script, "minImprovementPerRound <- ")
	numberOfRounds_ = find_value(SARKAR_script, "numberOfRounds <- ")
	write_to_log(numberOfRepPerRound_, minIPR_, numberOfRounds_, exe_time)
