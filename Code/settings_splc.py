import os
from path_settings import init_paths

path_list = init_paths()
SPLC_script = path_list[0]
SPLC_log = path_list[6]

def init_SPLC(meas_, var_):

	minIPR_ = input("Termination after which minimum improvement per round (e.g. 0.01)?: ")
	numberofrounds_ = input("Number of rounds (e.g. 100)): ")
	hierarchy_ = input("With Hierarchy? (y/n): ")
	if(hierarchy_=="y"):
		hierarchy_ = "True"
	else:
		hierarchy_ = "False"
	nfp_ = input("nfp Measured Value? (y/n): ")
	negfw_ = input("Negative feature wise sampling? (y/n): ")
	fws_ = input("Feature wise sampling? (y/n): ")
	pws_ = input("Pairwise sampling? (y/n): ")
	binaryft_ = input("Are all features binary? (y/n): ")

	
	#build script.a 
	
	str1 = str("log "+SPLC_log)
	#str2 = str("limitFeatureSize:False featureSizeTreshold:4")
	#str3 = str("mlSettings abortError:1 minImprovementPerRound:0.01 numberOfRounds:100 withHierarchy:false")
	str2 = str("mlSettings abortError:1 minImprovementPerRound:"+minIPR_+" numberOfRounds:"+numberofrounds_+" withHierarchy:"+hierarchy_)
	str3 = str("vm "+var_)
	str4 = str("all "+meas_)
	if(nfp_=="y"):
		str5 = str("nfp Measured Value")
	else:
		str5 = str("#nfp Measured Value")
	if(negfw_=="y"):
		str6 = str("negfw")
	else:
		str6 = str("#negfw")
	if(fws_=="y"):
		str7 = str("featureWise")
	else:
		str7 = str("#featureWise")
	if(pws_=="y"):
		str8 = str("pairWise")
	else:
		str8 = str("#pairWise")
	if(binaryft_=="y"):
		str9 = str("allBinary")
	else:
		str9 = str("#allBinary")
	str10 = str("start")
	str11 = str("analyze-learning")
	str12 = str("clean-sampling")
	str13 = str("# clean-learning")
	str14 = str("# clean-global ")
	
	
	script_ = open(SPLC_script, 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8+'\n'+str9 
		+'\n'+str10+'\n'+str11+'\n'+str12+'\n'+str13+'\n'+str14)
	script_.close()