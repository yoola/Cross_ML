import os
from path_settings import init_paths

path_list = init_paths()
SARKAR_script = path_list[2]

def init_SARKAR(numberofmeas_):

	minIPR_ = input("Termination after which minimum improvement per round (default(0.01): ENTER)?: ")
	numberofrounds_ = input("Number of rounds for the same sample amount (default(5): ENTER): ")
	sampleamount_ = input("Maximum sample amount (default: ENTER): ")

	if(minIPR_ ==""):
		minIPR_ = str("0.01")
	if(numberofrounds_ ==""):
		numberofrounds_ = str("5")
	if(sampleamount_==""):
		sampleamount_ = str(int(numberofmeas_/2))
	
	#build script_SARKAR.R 	
	str1 = str("numberOfRounds <- "+numberofrounds_+" #number of times experiment should be repeated")
	str2 = str("minImprovementPerRound <- "+minIPR_+" #complexity step")
	str3 = str("sampleAmount <- "+sampleamount_+" #complexity step")
	str4 = str("#progression base #(default = 1)")
	str5 = str("#sampling range lower value #(default = 1)")
	str6 = str("#sampling range upper value #(default = 1)")
	str7 = str("#sampling progression #(default = 1)")
	str8 = str("#complexLower #complexity range lower value #default = 0")
	str9 = str("#complexUpper #complexity range upper value # default = 0.001")

	script_ = open(SARKAR_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8)
	script_.close()

	return numberofrounds_
