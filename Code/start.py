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
from path_settings import init_paths

path_list = init_paths()
SPLC_script = path_list[0]
SPLC_exe = path_list[3]
CART_exe = path_list[4]
SAKAR_exe = path_list[5]

def Path_is_file(file_):

	if not Path(file_).is_file():
		print("No file directory.")
		sys.exit()

def get_meas_title(path_):

	pos1 = path_.rfind("/")
	pos2 = path_.rfind(".")

	meas_title = path_[pos1+1:pos2]

	return meas_title 

def set_sample_opts(SPLC_, CART_, SAKAR_, meas_, var_):

	if(SPLC_ =="y"):
		print("\nSampling Options for SPL Conqueror: ")
		init_SPLC(meas_, var_)

	if(CART_ == "y"):
		print("\nSampling Options for CART: ")
		init_CART()

	if(SAKAR_ == "y"):
		print("\nSampling Options for SAKAR: ")
		init_SAKAR()



def run_xml(SPLC_, meas_, var_):

	if(SPLC_ =="y"):

		print("\nStarting SPL Conqueror")
		print("See full.log file for progress")
		cl_dir = SPLC_exe
		os.system("mono "+cl_dir+" "+SPLC_script)


def run_csv(CART_, SAKAR_, csv_):


	if(CART_ == "y"):

		print("\nStarting CART")
		os.system("RScript "+ CART_exe+ " "+ csv_)
		
	if(SAKAR_ == "y"):

		print("\nStarting SAKAR")
		os.system("RScript "+ SAKAR_exe+ " "+ csv_)

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


		meas_ = input("Input your measurements xml file path: ")
		var_ = input("Input your variability model xml file path: ")

		Path_is_file(meas_)
		Path_is_file(var_)
		
		if not (meas_.endswith('.xml') and var_.endswith('.xml')):
			print("You entered the wrong file format.")
			sys.exit()

		conv_xml2csv(meas_,var_) # test.csv is created
		csv_ = str(os.getcwd()+"/test.csv")

		meas_title = get_meas_title(var_)
		set_sample_opts(SPLC_, CART_, SAKAR_, meas_, var_)

		run_xml(SPLC_, meas_, var_)
		run_csv(CART_, SAKAR_, csv_)
	
	
	elif input_ == 'csv':

		csv_ = input("Input your measurements csv file path: ")

		Path_is_file(csv_)

		if not csv_.endswith('.csv'):
			print("You entered the wrong file format.")
			sys.exit()

		conv_csv2xml(csv_) # meas.xml and var.xml are created
		meas_ = str(os.getcwd()+"/meas.xml")
		var_ = str(os.getcwd()+"/var.xml")

		meas_title = get_meas_title(csv_)
		set_sample_opts(SPLC_, CART_, SAKAR_, meas_, var_)

	
		run_csv(CART_, SAKAR_, csv_)
		run_xml(SPLC_, meas_, var_)
		
	
	else:
		print("No valid input format.")
		sys.exit()
	
	plot_results(SPLC_,CART_,SAKAR_, meas_title)

main()