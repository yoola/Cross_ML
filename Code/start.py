import io
import os
import sys
import time
from pathlib import Path
from csvToxml import conv_csv2xml
from xmlTocsv import conv_xml2csv
from parse_plot_logs import plot_results
from settings_splc import init_SPLC
from settings_CART import init_CART
from settings_SARKAR import init_SARKAR
from path_settings import init_paths

path_list = init_paths()
SPLC_script = path_list[0]
SPLC_exe = path_list[3]
CART_exe = path_list[4]
SARKAR_exe = path_list[5]

all_times = [] # storing all execution times

def CountMeas(file_):

	with open(file_,'r') as f:
			row_count = sum(1 for row in f)
	
	return(row_count-1)
    		

def Path_is_file(file_):

	if not Path(file_).is_file():
		print("No file directory.")
		sys.exit()

# get name of file to use it for the plot later on
def get_meas_title(path_):

	pos1 = path_.rfind("/")
	pos2 = path_.rfind(".")

	meas_title = path_[pos1+1:pos2]

	return meas_title 

# asked user for sampling options for each algorithm
def set_sample_opts_SPLC(SPLC_, meas_, var_, numberofmeas_):

	if(SPLC_ =="y"):
		print("\nSampling Options for SPL Conqueror: ")
		init_SPLC(meas_, var_, numberofmeas_)

def set_sample_opts_CART(CART_, meas_, var_, numberofmeas_):

	if(CART_ == "y"):
		print("\nSampling Options for CART: ")
		numberofrounds_ = init_CART(numberofmeas_)
		return numberofrounds_

def set_sample_opts_SARKAR(SARKAR_, meas_, var_, numberofmeas_):

	if(SARKAR_ == "y"):
		print("\nSampling Options for SARKAR: ")
		numberofrounds_ = init_SARKAR(numberofmeas_)
		return numberofrounds_

# run algorithms if chosen
def run_xml(SPLC_, meas_, var_):

	if(SPLC_ =="y"):

		print("\nStarting SPL Conqueror")
		print("See full.log file for progress")
		cl_dir = SPLC_exe
		start_time = time.time()
		os.system("mono "+cl_dir+" "+SPLC_script) # für Windows ändern
		end_time = time.time() - start_time
		all_times.append("SPLC_EXECUTION_TIME in sec: "+str(end_time))


def run_csv(CART_, SARKAR_, csv_):


	if(CART_ == "y"):

		print("\nStarting CART")
		start_time = time.time()
		os.system("RScript "+ CART_exe+ " "+ csv_)
		end_time = time.time() - start_time
		all_times.append("CART_EXECUTION_TIME in sec: "+str(end_time))
		
	if(SARKAR_ == "y"):

		print("\nStarting SARKAR")
		start_time = time.time()
		os.system("RScript "+ SARKAR_exe+ " "+ csv_)
		end_time = time.time() - start_time
		all_times.append("SARKAR_EXECUTION_TIME in sec: "+str(end_time))

	return csv_



def main():

	meas_ = str()
	var_ = str()
	csv_ = str()
	meas_title = str()
	check = True
	numberrounds_CART = 1
	numberrounds_SARKAR = 1


	input_ = input("Do you have your measurements as xml or csv?: ")

	print("\nWhich algorithms do you want to include in the analysis?")
	SPLC_ = input("SPL Conqueror? (y/n): ")
	CART_ = input("CART? (y/n): ")
	SARKAR_ = input("SARKAR? (y/n): ")


	
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
		numberofmeas =CountMeas(csv_);

		meas_title = get_meas_title(var_)
		set_sample_opts_SPLC(SPLC_, meas_, var_, numberofmeas)
		numberrounds_CART = set_sample_opts_CART(CART_, meas_, var_, numberofmeas)
		numberrounds_SAKAR = set_sample_opts_SARKAR(SARKAR_, meas_, var_, numberofmeas)

		run_xml(SPLC_, meas_, var_)
		run_csv(CART_, SARKAR_, csv_)
	
	
	elif input_ == 'csv':

		csv_ = input("Input your measurements csv file path: ")

		Path_is_file(csv_)

		if not csv_.endswith('.csv'):
			print("You entered the wrong file format.")
			sys.exit()

		numberofmeas =CountMeas(csv_);
		conv_csv2xml(csv_) # meas.xml and var.xml are created
		meas_ = str(os.getcwd()+"/meas.xml")
		var_ = str(os.getcwd()+"/var.xml")

		meas_title = get_meas_title(csv_)
		set_sample_opts_SPLC(SPLC_, meas_, var_, numberofmeas)
		numberrounds_CART = set_sample_opts_CART(CART_, meas_, var_, numberofmeas)
		numberrounds_SARKAR = set_sample_opts_SARKAR(SARKAR_, meas_, var_, numberofmeas)
	
		run_csv(CART_, SARKAR_, csv_)
		run_xml(SPLC_, meas_, var_)
		
	
	else:
		print("No valid input format.")
		sys.exit()

	plot_results(SPLC_,CART_,SARKAR_, meas_title, numberrounds_CART, numberrounds_SARKAR)
	for i in all_times:
		print(i)

main()