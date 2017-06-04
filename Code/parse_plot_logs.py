import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path
from path_settings import init_paths
path_list = init_paths()

SPLC_log = path_list[6]
CART_log = path_list[7]
SAKAR_log = path_list[8]
plot_dir = path_list[9]

def plot_CS(file_path, meas_title, title, key_char, cut, key_str, x_axis, y_axis):
	counter = 0
	fault_rate = []

	with open(file_path) as f:
		check = False
		for line in f:
			if(check == True):
				pos = line.rfind(key_char) # finding a key string in line to get fault rate
				if not pos == -1:
					fault_rate.append(line[pos+cut:-cut])
					counter += 1
	
			if key_str in line: # Finding string to start parsing document
				check = True

	plt.plot(range(0,counter), fault_rate, 'r')
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	plt.title(meas_title+": "+title)
	plt.savefig(plot_dir+title+".png")
	plt.gcf().clear()  
	#plt.show()
		
	f.close()



def plot_results(SPLC_,CART_,SAKAR_, meas_title):

	if(SPLC_ == "y"):
		plot_CS(SPLC_log,meas_title, "SPL Conqueror", ";", 1, "Termination", "number of rounds", "test error")
	if(CART_ == "y"):
		plot_CS(CART_log, meas_title, "CART", ",", 2, "Sampling", "sampling amount", "fault rate")
	if(SAKAR_=="y"):
		plot_CS(SAKAR_log, meas_title, "Sakar", ",", 2, "Sampling", "sampling amount", "fault rate")