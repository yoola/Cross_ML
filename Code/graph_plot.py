import matplotlib.pyplot as plt
import matplotlib
import statistics as stats
from findstring import find_top_faultrates_lines_logAll, find_flop_faultrates_lines_logAll, find_value_logAll, find_value_logAll2
from path_settings import init_paths
path_list = init_paths()

plot_dir = path_list[9]
SPLC_logAll = path_list[10]
SPLCext_logAll = path_list[16]
CART_logAll = path_list[11]
SARKAR_logAll = path_list[12]



def plot_top_faultrates_SPLC(title, top_faultrate_lines_, data_amount):

	#print(len(top_faultrate_lines_))

	exeTimes_list =[]
	minIPR_list = []
	numberOfRounds_list = []
	faultRate_list = []
	terminationReason_list = []
	negfw_list =[]
	featureWise_list =[]
	pairWise_list =[]
	random_list =[]

	exeTimes_list = find_value_logAll2(top_faultrate_lines_,"executionTime" )
	minIPR_list = find_value_logAll2(top_faultrate_lines_,"minImprovementPerRound" )
	numberOfRounds_list = find_value_logAll2(top_faultrate_lines_,"numberOfRounds" )
	faultRate_list = find_value_logAll2(top_faultrate_lines_,"faultRate" )
	terminationReason_list = find_value_logAll2(top_faultrate_lines_,"TerminationReason" )
	negfw_list = find_value_logAll2(top_faultrate_lines_,"negfw" )
	featureWise_list = find_value_logAll2(top_faultrate_lines_,"featureWise" )
	pairWise_list = find_value_logAll2(top_faultrate_lines_,"pairWise" )
	random_list = find_value_logAll2(top_faultrate_lines_,"random" )


	combination_list = []


	for i in range(0,len(negfw_list)):
		#1
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='True'):
			combination_list.append(' n+f+p+r')
		#2
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='False'):
			combination_list.append(' n+f+p')
		#3
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='True'):
			combination_list.append(' n+f+r')
		#4
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='True'):
			combination_list.append(' n+p+r')
		#5
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='False'):
			combination_list.append(' n+f')
		#6
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='False'):
			combination_list.append(' n+p')
		#7
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='True'):
			combination_list.append(' n+r')
		#8
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='False'):
			combination_list.append(' n')
		#9
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='True'):
			combination_list.append(' f+p+r')
		#10
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='False'):
			combination_list.append(' f+p')
		#11
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='True'):
			combination_list.append(' f+r')
		#12
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='False'):
			combination_list.append(' f')
		#13
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='True'):
			combination_list.append(' p+r')
		#14
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='False'):
			combination_list.append(' p')
		#15
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='True'):
			combination_list.append(' r')
		#16
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='False'):
			combination_list.append(' false')


	for i in range(0,len(terminationReason_list)):

		if terminationReason_list[i] == " abortError":
			terminationReason_list[i] = "-1"

		if terminationReason_list[i] == " minImprovementPerRound":
			terminationReason_list[i] = "0"

		if terminationReason_list[i] == " numberOfRounds":
			terminationReason_list[i] = "1"

	
	list_range = range(0,data_amount)
	minIPR_text = [-3]*data_amount

	fig, ax = plt.subplots()

	for i, txt in enumerate(combination_list):

		ax.annotate(txt, (list_range[i],int(numberOfRounds_list[i])+5), fontsize=8, rotation=35)

	for i, txt in enumerate(minIPR_list):

		ax.annotate(txt, (list_range[i],minIPR_text[i]), fontsize=8, rotation=45)

	#ax.plot(range(0,len(exeTimes_list)), exeTimes_list, 'o--', color = 'g', label="execution time")
	#ax.plot(range(0,len(minIPR_list)), minIPR_list, 'o--', color = 'k', label="min improvement per round")
	ax.plot(range(0,len(numberOfRounds_list)), numberOfRounds_list, '*--', color = 'b', label="number of rounds")
	ax.plot(range(0,len(faultRate_list)), faultRate_list, '^--', color = 'r', label="fault rate")
	ax.plot(range(0,len(terminationReason_list)), terminationReason_list, '*', color = 'm', label="termination reason (abortError:-1, minIPR:0, numberOfRounds:1)")
	handles, labels = ax.get_legend_handles_labels()
	lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1), fontsize=10)
	ax.grid('on')
	plt.title(title)
	plt.xlabel("Execution")
	x1,x2,y1,y2 = plt.axis()
	plt.axis((x1,x2,-10,90))
	fig.savefig(plot_dir+title, bbox_extra_artists=(lgd,), bbox_inches='tight')
	plt.gcf().clear() 



def plot_top_faultrates_R(title, top_faultrate_lines_, data_amount):

	exeTimes_list = find_value_logAll2(top_faultrate_lines_,"executionTime" )
	minIPR_list = find_value_logAll2(top_faultrate_lines_,"minImprovementPerRound" )
	numberOfRounds_list = find_value_logAll2(top_faultrate_lines_,"numberOfRounds" )
	faultRate_list = find_value_logAll2(top_faultrate_lines_,"faultRate" )
	terminationReason_list = find_value_logAll2(top_faultrate_lines_,"TerminationReason" )



	for i in range(0,len(terminationReason_list)):

		if terminationReason_list[i] == " abortError":
			terminationReason_list[i] = "-1"

		if terminationReason_list[i] == " minImprovementPerRound":
			terminationReason_list[i] = "0"

		if terminationReason_list[i] == " numberOfRounds":
			terminationReason_list[i] = "1"

	
	list_range = range(0,data_amount)
	minIPR_text = [-3]*data_amount

	fig, ax = plt.subplots()

	for i, txt in enumerate(minIPR_list):

		ax.annotate(txt, (list_range[i],minIPR_text[i]), fontsize=8, rotation=45)

	#ax.plot(range(0,len(exeTimes_list)), exeTimes_list, 'o--', color = 'g', label="execution time")
	#ax.plot(range(0,len(minIPR_list)), minIPR_list, 'o--', color = 'k', label="min improvement per round")
	ax.plot(range(0,len(numberOfRounds_list)), numberOfRounds_list, '*--', color = 'b', label="number of rounds")
	ax.plot(range(0,len(faultRate_list)), faultRate_list, '^--', color = 'r', label="fault rate")
	ax.plot(range(0,len(terminationReason_list)), terminationReason_list, '*', color = 'm', label="termination reason (abortError:-1, minIPR:0, numberOfRounds:1)")
	handles, labels = ax.get_legend_handles_labels()
	lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1), fontsize=10)
	ax.grid('on')
	plt.title(title)
	plt.xlabel("Execution")
	x1,x2,y1,y2 = plt.axis()
	plt.axis((x1,x2,-10,90))
	fig.savefig(plot_dir+title, bbox_extra_artists=(lgd,), bbox_inches='tight')
	plt.gcf().clear() 




def plot_top_faultrates_SPLCext(title, top_faultrate_lines_, data_amount):

	#print(top_faultrate_lines_)

	exeTimes_list = find_value_logAll2(top_faultrate_lines_,"executionTime" )
	minIPR_list = find_value_logAll2(top_faultrate_lines_,"minImprovementPerRound" )
	numberOfRounds_list = find_value_logAll2(top_faultrate_lines_,"numberOfRounds" )
	faultRate_list = find_value_logAll2(top_faultrate_lines_,"faultRate" )
	terminationReason_list = find_value_logAll2(top_faultrate_lines_,"TerminationReason" )
	expl_rdm_list = find_value_logAll2(top_faultrate_lines_,"explorer-random" )
	expl_max_dist_list = find_value_logAll2(top_faultrate_lines_,"explorer-max-distance" )
	expl_max_err_list = find_value_logAll2(top_faultrate_lines_,"explorer-max-error" )
	expl_combi_list = find_value_logAll2(top_faultrate_lines_,"explorer-combi" )
	expl_omni_list = find_value_logAll2(top_faultrate_lines_,"explorer-omni" )

	combination_list = []

	for i in range(0,len(expl_omni_list)):

		if(expl_rdm_list[i] =='True'):
			combination_list.append(' xp_rdm')
		if(expl_max_dist_list[i] =='True'):
			combination_list.append(' xp_max_dist')
		if(expl_max_err_list[i] =='True'):
			combination_list.append(' xp_max_err')
		if(expl_combi_list[i] =='True'):
			combination_list.append(' xp_combi')
		if(expl_omni_list[i] =='True'):
			combination_list.append(' xp_omni')

	for i in range(0,len(terminationReason_list)):

		if terminationReason_list[i] == " abortError":
			terminationReason_list[i] = "-1"

		if terminationReason_list[i] == " minImprovementPerRound":
			terminationReason_list[i] = "0"

		if terminationReason_list[i] == " numberOfRounds":
			terminationReason_list[i] = "1"

	list_range = range(0,data_amount)
	minIPR_text = [-3]*data_amount

	fig, ax = plt.subplots()

	for i, txt in enumerate(combination_list):

		ax.annotate(txt, (list_range[i],int(numberOfRounds_list[i])+5), fontsize=8, rotation=35)

	for i, txt in enumerate(minIPR_list):

		ax.annotate(txt, (list_range[i],minIPR_text[i]), fontsize=8, rotation=45)

	#ax.plot(range(0,len(exeTimes_list)), exeTimes_list, 'o--', color = 'g', label="execution time")
	#ax.plot(range(0,len(list_range)), numberOfRounds_list, '*', color = 'k', label="configurations")
	#ax.plot(range(0,len(minIPR_list)), minIPR_list, 'o--', color = 'k', label="min improvement per round")
	ax.plot(range(0,len(numberOfRounds_list)), numberOfRounds_list, '*--', color = 'b', label="number of rounds")
	ax.plot(range(0,len(faultRate_list)), faultRate_list, '^--', color = 'r', label="fault rate")
	ax.plot(range(0,len(terminationReason_list)), terminationReason_list, '*', color = 'm', label="termination reason (abortError:-1, minIPR:0, numberOfRounds:1)")
	handles, labels = ax.get_legend_handles_labels()
	lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1), fontsize=10)
	ax.grid('on')
	plt.title(title)
	plt.xlabel("Execution")
	x1,x2,y1,y2 = plt.axis()
	plt.axis((x1,x2,-10,90))
	fig.savefig(plot_dir+title, bbox_extra_artists=(lgd,), bbox_inches='tight')
	plt.gcf().clear() 



top_faultrate_lines_SPLCext = find_top_faultrates_lines_logAll(SPLCext_logAll, "faultRate:", 20)
flop_faultrates_lines_SPLCext = find_flop_faultrates_lines_logAll(SPLCext_logAll, "faultRate:", 20)
plot_top_faultrates_SPLCext('top20_faultrates_SPLCext_Apache', top_faultrate_lines_SPLCext,20)
plot_top_faultrates_SPLCext('flop20_faultrate_lines_SPLCext_Apache', flop_faultrates_lines_SPLCext,20)

top_faultrate_lines_SPLC = find_top_faultrates_lines_logAll(SPLC_logAll, "faultRate:", 10)
flop_faultrates_lines_SPLC = find_flop_faultrates_lines_logAll(SPLC_logAll, "faultRate:", 10)
plot_top_faultrates_SPLC('top10_faultrates_SPLC_Apache', top_faultrate_lines_SPLC,10)
plot_top_faultrates_SPLC('flop10_faultrates_lines_SPLC_Apache', flop_faultrates_lines_SPLC,10)


top_faultrate_lines_CART = find_top_faultrates_lines_logAll(CART_logAll, "faultRate:", 10)
flop_faultrates_lines_CART = find_flop_faultrates_lines_logAll(CART_logAll, "faultRate:", 10)
plot_top_faultrates_R('top10_faultrates_CART_Apache', top_faultrate_lines_CART,10)
plot_top_faultrates_R('flop10_faultrates_lines_CART_Apache', flop_faultrates_lines_CART,10)

top_faultrate_lines_SARKAR = find_top_faultrates_lines_logAll(SARKAR_logAll, "faultRate:", 10)
flop_faultrates_lines_SARKAR = find_flop_faultrates_lines_logAll(SARKAR_logAll, "faultRate:", 10)
plot_top_faultrates_R('top10_faultrates_SARKAR_Apache', top_faultrate_lines_SARKAR,10)
plot_top_faultrates_R('flop10_faultrates_lines_SARKAR_Apache', flop_faultrates_lines_SARKAR,10)

