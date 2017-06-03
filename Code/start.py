import io
import os
import sys
from pathlib import Path
from csvToxml import conv_csv2xml
from xmlTocsv import conv_xml2csv
from parse_plot_logs import plot_results
from settings_splc import init_SPLC
from settings_CART import init_CART
from settings_SAKAR import init_SAKAR


def Path_is_file(file_):

	if not Path(file_).is_file():
		print("No file directory.")
		sys.exit()

def get_meas_title(path_):

	pos1 = path_.rfind("/")
	pos2 = path_.rfind(".")

	meas_title = path_[pos1+1:pos2]

	return meas_title 


def run_xml(check, SPLC_):

	if check == True:      # if check is set to False, if measurement files are already read in
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

	Path_is_file(meas_)
	Path_is_file(var_)

	if(SPLC_ =="y"):

		print("Sampling Options for SPL Conqueror: ")
		init_SPLC(meas_, var_)
		print("Starting SPL Conqueror")
		print("See full.log file for progress")
		cl_dir ="/Users/jula/Github/SPLConqueror/SPLConqueror/CommandLine/bin/Debug/CommandLine.exe"
		os.system("mono "+cl_dir+" "+os.getcwd()+"/script.a")

	return xml_files


def run_csv(check, CART_, SAKAR_):

	if check == True:
		csv_ = input("Input your measurements csv file path: ")
		
		if not csv_.endswith('.csv'):
			print("You entered the wrong file format.")
			sys.exit()
	else:
		csv_ = str(os.getcwd()+"/test.csv")

	Path_is_file(csv_)

	meas_tile = get_meas_title(csv_)

	if(CART_ == "y"):

		print("Sampling Options for CART: ")
		init_CART()

		print("Starting CART")
		start_dir = str("/Users/jula/Github/ces/source/start_CART.R")
		os.system("RScript "+ start_dir+ " "+ csv_)
		
	if(SAKAR_ == "y"):

		print("Sampling Options for SAKAR: ")
		init_SAKAR()

		print("Starting SAKAR")
		start_dir = str("/Users/jula/Github/ces/source/start_SAKAR.R")
		os.system("RScript "+ start_dir+ " "+ csv_)

	return csv_

def main():

	meas_ = str()
	var_ = str()
	csv_ = str()
	meas_title = str()
	check = True


	input_ = input("Do you have your measurements as xml or csv?: ")

	print("\nWhich algorithms do you want to include in the analysis?")
	SPLC_ = input("SPL Conqueror? (y/n): ")
	CART_ = input("CART? (y/n): ")
	SAKAR_ = input("SAKAR? (y/n): ")

	
	if input_ == 'xml':
		xml_f = run_xml(check, SPLC_)
		meas_tile = get_meas_title(xml_f[1])
		print("SPL_Conqueror executed.")
		conv_xml2csv(xml_f[0],xml_f[1])
		check = False
		run_csv(check, CART_, SAKAR_)
	
	
	elif input_ == 'csv':
	
		csv_ = run_csv(check, CART_, SAKAR_)
		meas_tile = get_meas_title(csv_)
		print("CART and SAKAR executed.")	
		conv_csv2xml(csv_)
		check = False
		run_xml(check, SPLC_)
		
	
	else:
		print("No valid input format.")
		sys.exit()
	
	plot_results(SPLC_,CART_,SAKAR_, meas_tile)

main()