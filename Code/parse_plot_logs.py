import matplotlib.pyplot as plt
import matplotlib
import statistics as stats
from pathlib import Path
from path_settings import init_paths
from findstring import find_value, find_value_logAll
path_list = init_paths()

CART_script = path_list[1]
SARKAR_script = path_list[2]
SPLC_log = path_list[6]
CART_log = path_list[7]
SARKAR_log = path_list[8]
plot_dir = path_list[9]
SPLC_logAll = path_list[10]
CART_logAll = path_list[11]
SARKAR_logAll = path_list[12]


def write_to_log(filepath_, faultRateMean_, terminationReason_):

	script_ = open(filepath_, 'a')
	script_.write("faultRate:"+str(faultRateMean_)+"; TerminationReason: "+terminationReason_+";\n")
	script_.close()


def plot_results(file_path, meas_title, title, key_char, cut, key_str, numberOfRepPerRound, x_axis, y_axis, iter):

	counter = 0 #count number of lines
	faultRate_list = []
	mean_ = []
	deviation_ = []
	deviation_neg_ = []
	last_elem = 0
	step = int(numberOfRepPerRound) #round number
	terminationReason = str("")

	with open(file_path) as f:
		check = False
		for line in f:
			if(check == True):
				pos = line.rfind(key_char) # finding a key string in line to get fault rate
				if not pos == -1:
					faultRate_list.append(float(line[pos+cut:-cut]))
					counter += 1
	
			if key_str in line: # Finding string to start parsing document
				check = True

			if "Termination reason" in line and (title =="CART" or title =="SARKAR"):
				pos2 = line.find(",")
				terminationReason = line[pos2+2:-2]

			if "Termination reason" in line and title == ("SPL_Conqueror"):
				pos2 = line.find(":")
				pos3 = line.find("\n")
				terminationReason = line[pos2+2:pos3]

	if(title == "SPL_Conqueror"):
		write_to_log(SPLC_logAll, stats.mean(faultRate_list[-step:]), terminationReason)

	if(title == "CART"):
		write_to_log(CART_logAll, stats.mean(faultRate_list[-step:]), terminationReason)

	if(title == "SARKAR"):
		write_to_log(SARKAR_logAll, stats.mean(faultRate_list[-step:]), terminationReason)


	numberofmeas_ = int(counter/step)

	# plotting mean and standard deviation for algos
	#  with more repetitions per rounds than 1
	if(step >1):

		for i in range(0,counter,step):
			faultRate_list[i:i+step]
			mean_.append(stats.mean(faultRate_list[i:i+step]))
			deviation_.append(stats.stdev(faultRate_list[i:i+step]))

		for i in range(0,numberofmeas_):
			deviation_neg_.append(mean_[i]+abs(mean_[i]-deviation_[i]))
	

		plt.plot(range(0,numberofmeas_), mean_, 'g', label="mean of RepPerRound with standard deviation")
		plt.legend(loc=1)
		plt.fill_between(range(0,numberofmeas_), deviation_, deviation_neg_,
    	alpha=0.2, edgecolor='#1B2ACC', facecolor='#13DF3B',
    	linewidth=4, linestyle='dashdot', antialiased=True)
    	
	
		plt.xlabel(x_axis)
		plt.ylabel(y_axis)
		plt.title(meas_title+": "+title)
		plt.savefig(plot_dir+title+"_iter_"+str(iter)+"_mean.png")
		#plt.show()
		plt.gcf().clear()  

	
	for i in range(0,step):
		plt.plot(range(0,int(counter/step)), faultRate_list[i::step], 'r')
		plt.xlabel(x_axis)
		plt.ylabel(y_axis)
		plt.title(meas_title+": "+title)
		plt.savefig(plot_dir+title+"_iter"+str(iter)+"_rep"+str(i)+".png")
		#plt.show()
		plt.gcf().clear()  
	
		
	f.close()

def plot_results_logAll(filepath_, meas_title, title):

	executionTimes_ = find_value_logAll(filepath_, "executionTime:")
	numberOfRounds_ = find_value_logAll(filepath_, "numberOfRounds:")
	faultRates_ = find_value_logAll(filepath_, "faultRate:")

	#tmp_val = len(executionTimes_)-iter

	plt.plot(range(0,len(executionTimes_)), executionTimes_, 'g', label="execution time")
	plt.plot(range(0,len(numberOfRounds_)), numberOfRounds_, 'b', label="number of rounds")
	plt.plot(range(0,len(faultRates_)), faultRates_, 'r', label="fault rate")
	plt.legend(loc=1)
	plt.xlabel("Iteration of execution")
	plt.title(meas_title+": "+title)
	plt.savefig(plot_dir+title+"_logAll.png")
	#plt.show()
	plt.gcf().clear()  


