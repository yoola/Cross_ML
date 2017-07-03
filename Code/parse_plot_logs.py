import matplotlib.pyplot as plt
import matplotlib
import statistics as stats
from pathlib import Path
from path_settings import init_paths
from findstring import find_value
path_list = init_paths()

CART_script = path_list[1]
SARKAR_script = path_list[2]
SPLC_log = path_list[6]
CART_log = path_list[7]
SARKAR_log = path_list[8]
plot_dir = path_list[9]

def plot_SCS(file_path, meas_title, title, key_char, cut, key_str, numberOfRepPerRound, x_axis, y_axis):

	counter = 0 #count number of lines
	fault_rate = []
	mean_ = []
	deviation_ = []
	deviation_neg_ = []
	last_elem = 0
	step = int(numberOfRepPerRound) #round number

	with open(file_path) as f:
		check = False
		for line in f:
			if(check == True):
				pos = line.rfind(key_char) # finding a key string in line to get fault rate
				if not pos == -1:
					fault_rate.append(float(line[pos+cut:-cut]))
					counter += 1
	
			if key_str in line: # Finding string to start parsing document
				check = True



	print("counter: "+str(counter))
	print("step: "+str(step))
	numberofmeas_ = int(counter/step)
	print("numberofmeas: "+str(numberofmeas_))

	# plotting mean and standard deviation for algos
	#  with more repetitions per rounds than 1
	if(step >1):

		for i in range(0,counter,step):
			fault_rate[i:i+step]
			mean_.append(stats.mean(fault_rate[i:i+step]))
			deviation_.append(stats.stdev(fault_rate[i:i+step]))

		for i in range(0,numberofmeas_):
			deviation_neg_.append(mean_[i]+abs(mean_[i]-deviation_[i]))
	

		mean1 = plt.plot(range(0,numberofmeas_), mean_, 'g', label="mean with standard deviation")
		plt.legend(mean1, loc=1)
		dev1 = plt.fill_between(range(0,numberofmeas_), deviation_, deviation_neg_,
    	alpha=0.2, edgecolor='#1B2ACC', facecolor='#13DF3B',
    	linewidth=4, linestyle='dashdot', antialiased=True)
	
		plt.xlabel(x_axis)
		plt.ylabel(y_axis)
		plt.title(meas_title+": "+title)
		plt.savefig(plot_dir+title+"_mean.png")
		#plt.show()
		plt.gcf().clear()  

	
	for i in range(0,step):
		plt.plot(range(0,int(counter/step)), fault_rate[i::step], 'r')
		plt.xlabel(x_axis)
		plt.ylabel(y_axis)
		plt.title(meas_title+": "+title)
		plt.savefig(plot_dir+title+str(i)+".png")
		#plt.show()
		plt.gcf().clear()  
	
		
	f.close()


def plot_results(SPLC_,CART_,SARKAR_, meas_title):

	if(SPLC_ == "y"):
		plot_SCS(SPLC_log,meas_title, "SPL_Conqueror", ";", 1, "Termination", 1, "number of rounds", "test error")
	if(CART_ == "y"):
		number_of_rounds_CART = find_value(CART_script, "numberOfRounds <- ")
		plot_SCS(CART_log, meas_title, "CART", ",", 2, "Sampling", number_of_rounds_CART, "number of rounds", "fault rate")
	if(SARKAR_=="y"):
		number_of_rounds_SARKAR = find_value(SARKAR_script, "numberOfRounds <- ")
		plot_SCS(SARKAR_log, meas_title, "Sarkar", ",", 2, "Sampling", number_of_rounds_SARKAR, "number of rounds", "fault rate")