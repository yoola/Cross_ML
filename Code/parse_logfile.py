import matplotlib.pyplot as plt
import matplotlib

def plot_SPLC():
	counter = 0
	
	with open("full.log") as f:
		check = False
		fault_rate = []
		for line in f:
			if(check == True):
				pos = line.rfind(";")
				if not pos == -1:
					fault_rate.append(line[pos+1:-1])
					counter += 1
	
			if "Termination" in line:
				check = True
	
	f.close()

	plt.subplot(221)
	plt.plot(range(0,counter), fault_rate, 'r')
	plt.xlabel('number of rounds')
	plt.ylabel('test error')
	plt.title('SPL Conqueror')
	#plt.show()


def plot_CS(file_path, plot_num, title):
	counter = 0

	with open(file_path) as f:
		check = False
		fault_rate = []
		for line in f:
			if(check == True):
				pos = line.rfind(",")
				if not pos == -1:
					fault_rate.append(line[pos+2:-2])
					counter += 1
	
			if "Sampling" in line:
				check = True			
	f.close()

	plt.subplot(plot_num)
	plt.plot(range(0,counter), fault_rate, 'r')
	plt.xlabel('sampling amount')
	plt.ylabel('fault rate')
	plt.title(title)
	#plt.show()

def plot_results():

	fig = plt.figure("Results")
	plot_SPLC()
	plot_CS("/Users/jula/Github/ces/data/Benchmark/Output_CART/output_CART.csv",222, "CART")
	plot_CS("/Users/jula/Github/ces/data/Benchmark/Output_sakar/output_sakar.csv",223, "Sakar")
	plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)
	plt.savefig('faultrate.png')  
	plt.show()