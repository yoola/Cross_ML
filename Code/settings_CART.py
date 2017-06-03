import os

def init_CART():

	minIPR_ = input("Termination after which minimum improvement per round (e.g. 0.01)?: ")
	numberofrounds_ = input("Number of rounds (e.g. 100)): ")
	
	
	#build script_CART.R 
	
	str1 = str("numberOfRounds <- "+numberofrounds_+" #number of times experiment should be repeated")

	str2 = str("minImprovementPerRound <- "+minIPR_+" #complexity step")
	str3 = str("#progression base #(default = 1)")
	str4 = str("#sampling range lower value #(default = 1)")
	str5 = str("#sampling range upper value #(default = 1)")
	str6 = str("#sampling progression #(default = 1)")
	str7 = str("#complexLower #complexity range lower value #default = 0")
	str8 = str("#complexUpper #complexity range upper value # default = 0.001")

	
	
	script_ = open("script_CART.R", 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8)
	script_.close()
