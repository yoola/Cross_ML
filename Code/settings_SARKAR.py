import os
import random
from path_settings import init_paths
from findstring import find_value

path_list = init_paths()
SARKAR_script = path_list[2]
SARKAR_logAll = path_list[12]

def init_SARKAR(numberofmeas_):

	interactive_ = input("Interactive mode? (y/n): ")

	if(interactive_=="y"):

		minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
		numberofrounds_ = input("Number of rounds for the same sample amount (default(5): ENTER): ")
		sampleamount_ = input("Maximum sample amount (default: ENTER): ")

		if(minIPR_ ==""):
			minIPR_ = str("0.01")
		if(numberofrounds_ ==""):
			numberofrounds_ = str("5")
		if(sampleamount_==""):
			sampleamount_ = str(int(numberofmeas_/2))
	
		build_script_SARKAR(numberofrounds_, minIPR_, sampleamount_)


def change_script_SARKAR():

	minIPR_ = random.uniform(0.001, 0.1)
	numberofrounds_ = random.choice(range(1,9))
	sampleamount_ = random.choice(range(11,90))
	build_script_SARKAR(str(numberofrounds_), str(minIPR_), str(sampleamount_))


def build_script_SARKAR(numberofrounds_, minIPR_, sampleamount_):

	#build script_SARKAR.R 	
	str1 = str("numberOfRounds <- "+numberofrounds_+"; #number of times experiment should be repeated")
	str2 = str("minImprovementPerRound <- "+minIPR_+"; #complexity step")
	str3 = str("sampleAmount <- "+sampleamount_+"; #complexity step")
	str4 = str("#progression base #(default = 1)")
	str5 = str("#sampling range lower value #(default = 1)")
	str6 = str("#sampling range upper value #(default = 1)")
	str7 = str("#sampling progression #(default = 1)")
	str8 = str("#complexLower #complexity range lower value #default = 0")
	str9 = str("#complexUpper #complexity range upper value # default = 0.001")

	script_ = open(SARKAR_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8 +'\n'+str9)
	script_.close()


def write_to_log(numberofrounds_, minIPR_, sampleamount_, exe_time):

	script_ = open(SARKAR_logAll, 'a')
	script_.write("executionTime: "+exe_time+"; numberOfRounds: "+numberofrounds_+"; minImprovementPerRound: "+minIPR_+"; sampleAmount: "+sampleamount_+"\n")
	script_.close()


def parse_script_SARKAR(exe_time):

	numberofrounds_ = find_value(SARKAR_script, "numberOfRounds <- ")
	minIPR_ = find_value(SARKAR_script, "minImprovementPerRound <- ")
	sampleamount_ = find_value(SARKAR_script, "sampleAmount <- ")
	write_to_log(numberofrounds_, minIPR_, sampleamount_, exe_time)



