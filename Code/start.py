import io
import os
import sys
import time
from pathlib import Path
from csvToxml import conv_csv2xml
from xmlTocsv import conv_xml2csv
from parse_plot_logs import plot_results, plot_results_logAll
from settings_splc import init_SPLC, change_script_SPLC, parse_script_SPLC
from settings_splcext import init_SPLCext, change_script_SPLCext, parse_script_SPLCext
from settings_CART import init_CART, change_script_CART, parse_script_CART
from settings_SARKAR import init_SARKAR, change_script_SARKAR, parse_script_SARKAR
from path_settings import init_paths
from findstring import find_value

path_list = init_paths()
SPLC_script = path_list[0]
SPLCext_script = path_list[13]
SPLC_exe = path_list[3]
SPLCext_exe = path_list[14]
CART_exe = path_list[4]
SARKAR_exe = path_list[5]
SPLC_logAll = path_list[10]
SPLCext_logAll = path_list[16]
CART_logAll = path_list[11]
SARKAR_logAll = path_list[12]
SPLC_log = path_list[6]
SPLCext_log = path_list[15]
CART_log = path_list[7]
SARKAR_log = path_list[8]
CART_script = path_list[1]
SARKAR_script = path_list[2]
csvData_ = path_list[17]
xmlDatameas_ = path_list[18]
xmlDatavar_ = path_list[19]

def append_time_to_script(time_, script_path):

	script_ = open(script_path, 'a')
	script_.write("; executionTime: "+time_+"\n")
	script_.close()


def count_meas(file_):

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
def set_sample_opts(SPLC_, SPLCext_, CART_, SARKAR_, meas_, var_, numberofmeas_):

	if(SPLC_ =="y"):
		print("\nSampling Options for SPL Conqueror: ")
		init_SPLC(meas_, var_, numberofmeas_)

	if(SPLCext_ =="y"):
		print("\nSampling Options for SPL Conqueror ext: ")
		init_SPLCext(meas_, var_, numberofmeas_)

	if(CART_ == "y"):
		print("\nSampling Options for CART: ")
		init_CART(numberofmeas_)

	if(SARKAR_ == "y"):
		print("\nSampling Options for SARKAR: ")
		init_SARKAR(numberofmeas_)

# run algorithms if chosen
def run_xml(SPLC_, SPLCext_, meas_, var_, numberofmeas_, repeat_run_SPLC, repeat_run_SPLCext, meas_title):

	if(SPLC_ =="y"):

		for i in range(0,repeat_run_SPLC):

			if(i>0):
				change_script_SPLC(meas_, var_, numberofmeas_)
			print("\nStarting SPL Conqueror")
			print("Number of execution: "+str(i+1))
			print("See full_SPLC.log file for progress")
			start_time = time.time()
			os.system("mono "+SPLC_exe+" "+SPLC_script) # für Windows ändern
			end_time = time.time() - start_time
			print("SPLC_EXECUTION_TIME in sec: "+str(end_time))
			parse_script_SPLC(str(end_time))
			plot_results(SPLC_log, meas_title, "SPL_Conqueror", ";", 1, "Termination", 1, "number of rounds", "test error", i)
			
		plot_results_logAll(SPLC_logAll, meas_title, "SPL_Conqueror")

	if(SPLCext_ =="y"):

		for i in range(0,repeat_run_SPLCext):

			if(i>0):
				change_script_SPLCext(meas_, var_, numberofmeas_)
			print("\nStarting SPL Conqueror ext")
			print("Number of execution: "+str(i+1))
			print("See full_SPLCext.log file for progress")
			start_time = time.time()
			os.system("mono "+SPLCext_exe+" "+SPLCext_script) # für Windows ändern
			end_time = time.time() - start_time
			print("SPLCext_EXECUTION_TIME in sec: "+str(end_time))
			parse_script_SPLCext(str(end_time))
			plot_results(SPLCext_log, meas_title, "SPL_Conqueror_ext", ";", 1, "progress:", 1, "number of rounds", "test error", i)
			
		plot_results_logAll(SPLCext_logAll, meas_title, "SPL_Conqueror_ext")

def run_csv(CART_, SARKAR_, csv_, repeat_run_CART, repeat_run_SARKAR, meas_title):


	if(CART_ == "y"):

		for i in range(0,repeat_run_CART):

			if(i>0):
				change_script_CART()
			print("\nStarting CART")
			print("Number of execution: "+str(i+1))
			start_time = time.time()
			os.system("RScript "+ CART_exe+ " "+ csv_)
			end_time = time.time() - start_time
			print("CART_EXECUTION_TIME in sec: "+str(end_time))
			parse_script_CART(str(end_time))
			numberOfRepPerRound_CART = find_value(CART_script, "numberOfRepPerRound <- ")
			plot_results(CART_log, meas_title, "CART", ",", 2, "Sampling", numberOfRepPerRound_CART, "number of rounds", "fault rate", i)

		plot_results_logAll(CART_logAll, meas_title, "CART")
		
	if(SARKAR_ == "y"):

		for i in range(0,repeat_run_SARKAR):
			
			if(i>0):
				change_script_SARKAR()
			print("\nStarting SARKAR")
			print("Number of execution: "+str(i+1))
			start_time = time.time()
			os.system("RScript "+ SARKAR_exe+ " "+ csv_)
			end_time = time.time() - start_time
			print("SARKAR_EXECUTION_TIME in sec: "+str(end_time))
			parse_script_SARKAR(str(end_time))
			numberOfRepPerRound_SARKAR = find_value(SARKAR_script, "numberOfRepPerRound <- ")
			plot_results(SARKAR_log, meas_title, "SARKAR", ",", 2, "Sampling", numberOfRepPerRound_SARKAR, "number of rounds", "fault rate", i)
			
		plot_results_logAll(SARKAR_logAll, meas_title, "SARKAR")

	return csv_



def main():

	meas_ = str()
	var_ = str()
	csv_ = str()
	meas_title = str()
	check = True
	repeat_run_SPLC = 0
	repeat_run_SPLCext = 0
	repeat_run_CART = 0
	repeat_run_SARKAR = 0


	input_ = input("Do you have your measurements as xml or csv?: ")

	print("\nWhich algorithms do you want to include in the analysis?")
	SPLC_ = input("SPL Conqueror? (y/n): ")
	if SPLC_ == "y":
		repeat_run_SPLC = int(input("How often do you want to run it?: "))
	SPLCext_ = input("SPL Conqueror ext? (y/n): ")
	if SPLCext_ == "y":
		repeat_run_SPLCext = int(input("How often do you want to run it?: "))
	CART_ = input("CART? (y/n): ")
	if CART_ =="y":
		repeat_run_CART = int(input("How often do you want to run it?: "))
	SARKAR_ = input("SARKAR? (y/n): ")
	if SARKAR_ =="y":
		repeat_run_SARKAR = int(input("How often do you want to run it?: "))
		
	
	if input_ == 'xml':

		meas_ = xmlDatameas_
		var_ = xmlDatavar_ 

		which_path = input("Do you want to use standard data path? (y/n): ")
		if which_path == "n":
			meas_ = input("Input your measurements xml file path: ")
			var_ = input("Input your variability model xml file path: ")

		Path_is_file(meas_)
		Path_is_file(var_)
		
		if not (meas_.endswith('.xml') and var_.endswith('.xml')):
			print("You entered the wrong file format.")
			sys.exit()

		conv_xml2csv(meas_,var_) # test.csv is created
		csv_ = str(os.getcwd()+"/test.csv")
		numberofmeas =count_meas(csv_);

		meas_title = get_meas_title(var_)
		set_sample_opts(SPLC_, SPLCext_, CART_, SARKAR_, meas_, var_, numberofmeas)

		run_xml(SPLC_, SPLCext_, meas_, var_, numberofmeas, repeat_run_SPLC, repeat_run_SPLCext, meas_title)
		run_csv(CART_, SARKAR_, csv_, repeat_run_CART, repeat_run_SARKAR, meas_title)
	
	
	elif input_ == 'csv':

		csv_ = csvData_

		which_path = input("Do you want to use standard data path? (y/n): ")
		if which_path == "n":
			csv_ = input("Input your measurements csv file path: ")


		Path_is_file(csv_)

		if not csv_.endswith('.csv'):
			print("You entered the wrong file format.")
			sys.exit()

		numberofmeas =count_meas(csv_);
		conv_csv2xml(csv_) # meas.xml and var.xml are created
		meas_ = str(os.getcwd()+"/meas.xml")
		var_ = str(os.getcwd()+"/var.xml")

		meas_title = get_meas_title(csv_)
		set_sample_opts(SPLC_, SPLCext_, CART_, SARKAR_, meas_, var_, numberofmeas)
	
		run_csv(CART_, SARKAR_, csv_, repeat_run_CART, repeat_run_SARKAR, meas_title)
		run_xml(SPLC_, SPLCext_, meas_, var_, numberofmeas, repeat_run_SPLC, repeat_run_SPLCext, meas_title)
		
	
	else:
		print("No valid input format.")
		sys.exit()


main()