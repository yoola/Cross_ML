import os
import random
from path_settings import init_paths
from findstring import find_value

path_list = init_paths()
CART_script = path_list[1]
CART_logAll = path_list[11]


def init_CART(numberofmeas_):

	interactive_ = input("Interactive mode? (y/n): ")

	if(interactive_=="y"):

		minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
		numberOfRepPerRound_ = input("Number of repetitions per round for the same sample amount (default(5): ENTER): ")
		numberOfRounds_ = input("Maximum measurements/rounds (default: ENTER): ")

		if(minIPR_ ==""):
			minIPR_ = str("0.01")
		if(numberOfRepPerRound_ ==""):
			numberOfRepPerRound_ = str("5")
		if(numberOfRounds_==""):
			numberOfRounds_ = str(int(numberofmeas_/2))
	
		build_script_CART(numberOfRepPerRound_, minIPR_, numberOfRounds_)


def change_script_CART():

	minIPR_ = random.uniform(0.001, 0.1)
	numberOfRepPerRound_ = random.choice(range(1,9))
	numberOfRounds_ = random.choice(range(11,90))
	build_script_CART(str(numberOfRepPerRound_), str(minIPR_), str(numberOfRounds_))


def build_script_CART(numberOfRepPerRound_, minIPR_, numberOfRounds_):

	#build script_CART.R 	
	str1 = str("numberOfRepPerRound <- "+numberOfRepPerRound_+"; #number of times experiment should be repeated")
	str2 = str("minImprovementPerRound <- "+minIPR_+"; #complexity step")
	str3 = str("numberOfRounds <- "+numberOfRounds_+"; #complexity step")
	str4 = str("#progression base #(default = 1)")
	str5 = str("#sampling range lower value #(default = 1)")
	str6 = str("#sampling range upper value #(default = 1)")
	str7 = str("#sampling progression #(default = 1)")
	str8 = str("#complexLower #complexity range lower value #default = 0")
	str9 = str("#complexUpper #complexity range upper value # default = 0.001")

	script_ = open(CART_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8 +'\n'+str9)
	script_.close()


def write_to_log(numberOfRepPerRound_, minIPR_, numberOfRounds_, exe_time):

	script_ = open(CART_logAll, 'a')
	script_.write("executionTime:"+exe_time+"; numberOfRepPerRound:"+numberOfRepPerRound_+"; minImprovementPerRound:"+minIPR_+"; numberOfRounds:"+numberOfRounds_+"; ")
	script_.close()


def parse_script_CART(exe_time):

	numberOfRepPerRound_ = find_value(CART_script, "numberOfRepPerRound <- ")
	minIPR_ = find_value(CART_script, "minImprovementPerRound <- ")
	numberOfRounds_ = find_value(CART_script, "numberOfRounds <- ")
	write_to_log(numberOfRepPerRound_, minIPR_, numberOfRounds_, exe_time)
