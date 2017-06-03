import matplotlib.pyplot as plt
import matplotlib


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
	plt.savefig(title+".png")
	plt.gcf().clear()  
	#plt.show()
		
	f.close()



def plot_results(SPLC_,CART_,SAKAR_, meas_title):

	out_CART_path = "/Users/jula/Github/ces/data/Benchmark/Output_CART/output_CART.csv"
	out_SAKAR_path = "/Users/jula/Github/ces/data/Benchmark/Output_sakar/output_sakar.csv"

	if(SPLC_ == "y"):
		plot_CS("full.log",meas_title, "SPL Conqueror", ";", 1, "Termination", "number of rounds", "test error")
	if(CART_ == "y"):
		plot_CS(out_CART_path, meas_title, "CART", ",", 2, "Sampling", "sampling amount", "fault rate")
	if(SAKAR_=="y"):
		plot_CS(out_SAKAR_path, meas_title, "Sakar", ",", 2, "Sampling", "sampling amount", "fault rate")
	