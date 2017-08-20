
def init_paths():

	# THE ORDER OF THE LIST IS IMPORTANT!!!
	# PLEASE ADD PATHS ONLY AT THE END OF THE ALREADY DEFINED LIST
	
	path_list = []
	# scripts for sampling options
	# Setting_scripts folder must be already created, not so the files
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_SPLC.a") #0
	path_list.append("C:\\Users\\Jula\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_CART.R") #1
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_SARKAR.R") #2
	
	#
	# execution file for SPL Conqueror
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\SPLConqueror\\SPLConqueror\\CommandLine\\bin\\Debug\\CommandLine.exe") #3
	
	# execution files for CART and SARKAR
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\ces_modified\\start_CART.R") #4
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\ces_modified\\start_SARKAR.R") #5

	# output file paths
	# Logs folder must be already created, not so the files
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\full_SPLC.log") #6
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\output_CART.csv") #7
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\output_SARKAR.csv") #8

	# Output folder path
	# Plots folder must be created
	path_list.append("..\\Plots\\") #9

	# build summarizing log file
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\logAll_SPLC.R") #10
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\logAll_CART.R") #11
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\logAll_SARKAR.R") #12

	#----------------------
	# Adding extended version of SPL_Conqueror

	# scripts for sampling options
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_SPLCext.a") #13

	# execution file for SPL Conqueror_extended
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\SPLConqueror-activeLearning\\SPLConqueror\\CommandLine\\bin\\Debug\\CommandLine.exe") #14

	# output file paths
	# Logs folder must be already created, not so the files
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\full_SPLCext.log") #15

	# build summarizing log file
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Logs\\logAll_SPLCext.R") #16
	#----------------------


	# paths for measurement files
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Data\\Apache.csv") #17

	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Data\\measurements.xml") #18
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Data\\H264.xml") #19

	#------------------------
	
	# configuration files for script settings
	
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_CART_All.a") #20
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_SARKAR_All.a") #21
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_SPLC_All.a") #22
	path_list.append("C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\Setting_scripts\\script_SPLCext_All.a") #23


	return path_list