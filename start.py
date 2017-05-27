import io
import os
import sys
from pathlib import Path
from csvToxml import conv_csv2xml
from xmlTocsv import conv_xml2csv
from parse_logfile import plot_results

def run_xml(check):

	if check == True:
		meas_ = input("Input your measurements xml file path: ")
		var_ = input("Input your variability model xml file path: ")

		if not (meas_.endswith('.xml') and var_.endswith('.xml')):
			print("You entered the wrong file format.")
			sys.exit()

	else:
		meas_ = str(os.getcwd()+"/meas.xml")
		var_ =  str(os.getcwd()+"/var.xml")


	xml_files = []
	xml_files.append(meas_)
	xml_files.append(var_)

	if not (Path(meas_).is_file() and Path(var_).is_file()):
		print("No file directory.")
		sys.exit()

				#log /Users/jula/Github/SPLConqueror/SPLConqueror/Test/TestData/full.log
	str1 = str("log /Users/jula/Github/main_program/full.log")
	str2 = str("# limitFeatureSize:False featureSizeTrehold:4")
	str3 = str("mlSettings abortError:1 minImprovementPerRound:0.01 numberOfRounds:100 withHierarchy:false")
	str4 = str("vm "+var_)
	str5 = str("all "+meas_)
	str6 = str("nfp Measured Value")
	str7 = str("negfw")
	str8 = str("featureWise")
	str9 = str("#pairWise")
	str10 = str("allBinary")
	str11 = str("start")
	str12 = str("analyze-learning")
	str13 = str("clean-sampling")
	str14 = str("# clean-learning")
	str15 = str("# clean-global ")
	
	#path = str("/Users/jula/Github/SPLConqueror/SPLConqueror/script.a")


	script_ = open("script.a", 'w')
	script_.write(str1 +'\n'+str2+'\n'+str3 +'\n'+str4+'\n'+str5 +'\n'+str6+'\n'+str7 +'\n'+str8+'\n'+str9 
		+'\n'+str10+'\n'+str11+'\n'+str12+'\n'+str13+'\n'+str14+'\n'+str15)
	script_.close()
	print("Starting SPL Conqueror")
	print("See full.log file for progress")
	cl_dir ="/Users/jula/Github/SPLConqueror/SPLConqueror/CommandLine/bin/Debug/CommandLine.exe"
	os.system("mono "+cl_dir+" /Users/jula/Github/main_program/script.a")
	return xml_files


def run_csv(check):

	if check == True:
		csv_ = input("Input your measurements csv file path: ")
		
		if not csv_.endswith('.csv'):
			print("You entered the wrong file format.")
			sys.exit()
	else:
		csv_ = str(os.getcwd()+"/test.csv")

	if not Path(csv_).is_file():
		print("No file directory.")
		sys.exit()

	start_dir = str("/Users/jula/Github/ces/source/start_model.R")
	os.system("RScript "+ start_dir+ " "+ csv_)
	return csv_
	
def main():

	meas_ = str()
	var_ = str()
	csv_ = str()
	check = True


	input_ = input("Do you have your measurements as xml or csv?: ")
	
	
	if input_ == 'xml':
		xml_f = run_xml(check)
		print("SPL_Conqueror executed.")
		conv_xml2csv(xml_f[0],xml_f[1])
		check = False
		run_csv(check)
		print("CART and SAKAR executed.")
	
	
	elif input_ == 'csv':
	
		csv_ = run_csv(check)
		print("CART and SAKAR executed.")	
		conv_csv2xml(csv_)
		check = False
		run_xml(check)
		print("SPL_Conqueror executed.")
		
	
	else:
		print("No valid input format.")
		sys.exit()
	
	plot_results()

main()