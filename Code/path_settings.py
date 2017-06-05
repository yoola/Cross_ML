
def init_paths():

	# THE ORDER OF THE LIST IS IMPORTANT!!!
	# PLEASE ADD PATHS ONLY AT THE END OF THE ALREADY DEFINED LIST
	
	path_list = []
	# scripts for sampling options
	# Outputs folder must be created
	path_list.append("/Users/jula/Github/Cross_ML/Setting_scripts/script_SPLC.a") #0
	path_list.append("/Users/jula/Github/Cross_ML/Setting_scripts/script_CART.R") #1
	path_list.append("/Users/jula/Github/Cross_ML/Setting_scripts/script_SAKAR.R") #2
	
	# execution file for SPL Conqueror
	path_list.append("/Users/jula/Github/SPLConqueror/SPLConqueror/CommandLine/bin/Debug/CommandLine.exe") #3
	
	# execution files for CART and SAKAR
	path_list.append("/Users/jula/Github/Cross_ML/ces_modified/start_CART.R") #4
	path_list.append("/Users/jula/Github/Cross_ML/ces_modified/start_SAKAR.R") #5

	# output file paths
	path_list.append("/Users/jula/Github/Cross_ML/Logs/full.log") #6
	path_list.append("/Users/jula/Github/Cross_ML/Logs/output_CART.csv") #7
	path_list.append("/Users/jula/Github/Cross_ML/Logs/output_sakar.csv") #8

	# Output folder path
	# Plots folder must be created
	path_list.append("Plots/") #9

	return path_list