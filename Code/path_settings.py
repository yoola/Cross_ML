
def init_paths():

	# THE ORDER OF THE LIST IS IMPORTANT!!!
	# PLEASE ADD PATHS ONLY AT THE END OF THE ALREADY DEFINED LIST
	
	path_list = []
	# scripts for sampling options
	# Outputs folder must be created
	path_list.append("/Users/jula/Github/Cross_ML/Outputs/script.a") #0
	path_list.append("/Users/jula/Github/Cross_ML/Outputs/script_CART.R") #1
	path_list.append("/Users/jula/Github/Cross_ML/Outputs/script_SAKAR.R") #2
	
	# execution file for SPL Conqueror
	path_list.append("/Users/jula/Github/SPLConqueror/SPLConqueror/CommandLine/bin/Debug/CommandLine.exe") #3
	
	# execution files for CART and SAKAR
	path_list.append("/Users/jula/Github/ces/source/start_CART.R") #4
	path_list.append("/Users/jula/Github/ces/source/start_SAKAR.R") #5

	# output file paths
	path_list.append("/Users/jula/Github/Cross_ML/Outputs/full.log") #6
	path_list.append("/Users/jula/Github/ces/data/Benchmark/Output_CART/output_CART.csv") #7
	path_list.append("/Users/jula/Github/ces/data/Benchmark/Output_sakar/output_sakar.csv") #8

	# Output folder path
	# Plots folder must be created
	path_list.append("Plots/") #9

	return path_list