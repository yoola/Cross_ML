import matplotlib.pyplot as plt
import matplotlib
from path_settings import init_paths
from findstring import find_value_logAll2, find_lines_logAll, find_value_logAll_float, find_value_logAll_int, find_top_faultrates_lines_logAll, find_flop_faultrates_lines_logAll


path_list = init_paths()
plot_dir = path_list[9]
SPLC_logAll = path_list[10]
SPLCext_logAll = path_list[16]


# log_lines_SPLC = find_lines_logAll(SPLC_logAll)
# log_lines_SPLCext = find_lines_logAll(SPLCext_logAll)

toplog_lines_SPLC = find_top_faultrates_lines_logAll(SPLC_logAll, "faultRate:", 30)
toplog_lines_SPLCext = find_top_faultrates_lines_logAll(SPLCext_logAll, "faultRate:", 30)


floplog_lines_SPLC = find_flop_faultrates_lines_logAll(SPLC_logAll, "faultRate:", 30)
floplog_lines_SPLCext = find_flop_faultrates_lines_logAll(SPLCext_logAll, "faultRate:", 30)



def barchart_logs(log_lines_SPLC, log_lines_SPLCext, title):

	expl_rdm_list = find_value_logAll2(log_lines_SPLCext,"explorer-random")
	expl_max_dist_list = find_value_logAll2(log_lines_SPLCext,"explorer-max-distance")
	expl_max_err_list = find_value_logAll2(log_lines_SPLCext,"explorer-max-error")
	expl_combi_list = find_value_logAll2(log_lines_SPLCext,"explorer-combi")
	expl_omni_list = find_value_logAll2(log_lines_SPLCext,"explorer-omni")

	numberOfAppearance_list_SPLCext = [0,0,0,0,0]
	x_axis = [1,2,3,4,5]
	x_labels=['expl_rdm_','expl_max_dist', 'expl_max_err', 'expl_combi', 'expl_omni']

	#print(expl_rdm_list)
	#print(expl_max_dist_list)
	#print(expl_max_err_list)
	#print(expl_combi_list)
	#print(expl_omni_list)

	for i in range(0,len(expl_omni_list)):

		if(expl_rdm_list[i] =='True'):
			numberOfAppearance_list_SPLCext[0] = numberOfAppearance_list_SPLCext[0]+1

		if(expl_max_dist_list[i] =='True'):
			numberOfAppearance_list_SPLCext[1] = numberOfAppearance_list_SPLCext[1]+1

		if(expl_max_err_list[i] =='True'):
			numberOfAppearance_list_SPLCext[2] = numberOfAppearance_list_SPLCext[2]+1

		if(expl_combi_list[i] =='True'):
			numberOfAppearance_list_SPLCext[3] = numberOfAppearance_list_SPLCext[3]+1

		if(expl_omni_list[i] =='True'):
			numberOfAppearance_list_SPLCext[4] = numberOfAppearance_list_SPLCext[4]+1 

	plt.bar(x_axis, numberOfAppearance_list_SPLCext, align='center', alpha=0.5)
	plt.xticks(x_axis, x_labels, fontsize = 10)
	plt.title("SPLC Conqueror ext")
	plt.ylabel('Frequency')
	plt.title('Algos Appearance Rate In '+title+' Fault Rates: Apache')
	plt.savefig(plot_dir+title+"_SPLCextAlgos_freq_barchart.png")
	plt.gcf().clear()  



	negfw_list = find_value_logAll2(log_lines_SPLC,"negfw" )
	featureWise_list = find_value_logAll2(log_lines_SPLC,"featureWise" )
	pairWise_list = find_value_logAll2(log_lines_SPLC,"pairWise" )
	random_list = find_value_logAll2(log_lines_SPLC,"random" )

	combination_freq_list = [0]*16
	combination_list = ['n+f+p+r', ' n+f+p', ' n+f+r', ' n+p+r', ' n+f', ' n+p', ' n+r', 'n', 'f+p+r', 'f+p', 'f+r', 'f', 'p+r', 'p', 'r', 'false']
	combination_axis = range(0,16)


	for i in range(0,len(negfw_list)):
		#1
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='True'):
			#combination_list.append(' n+f+p+r')
			combination_freq_list[0] = combination_freq_list[0]+1
		#2
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='False'):
			#combination_list.append(' n+f+p')
			combination_freq_list[1] = combination_freq_list[1]+1
		#3
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='True'):
			#combination_list.append(' n+f+r')
			combination_freq_list[2] = combination_freq_list[2]+1
		#4
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='True'):
			#combination_list.append(' n+p+r')
			combination_freq_list[3] = combination_freq_list[3]+1
		#5
		if(negfw_list[i] =='True' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='False'):
			#combination_list.append(' n+f')
			combination_freq_list[4] = combination_freq_list[4]+1
		#6
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='False'):
			#combination_list.append(' n+p')
			combination_freq_list[5] = combination_freq_list[5]+1
		#7
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='True'):
			#combination_list.append(' n+r')
			combination_freq_list[6] = combination_freq_list[6]+1
		#8
		if(negfw_list[i] =='True' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='False'):
			#combination_list.append(' n')
			combination_freq_list[7] = combination_freq_list[7]+1
		#9
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='True'):
			#combination_list.append(' f+p+r')
			combination_freq_list[8] = combination_freq_list[8]+1
		#10
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='True' and random_list[i] =='False'):
			#combination_list.append(' f+p')
			combination_freq_list[9] = combination_freq_list[9]+1
		#11
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='True'):
			#combination_list.append(' f+r')
			combination_freq_list[10] = combination_freq_list[10]+1
		#12
		if(negfw_list[i] =='False' and featureWise_list[i] =='True' and pairWise_list[i] =='False' and random_list[i] =='False'):
			#combination_list.append(' f')
			combination_freq_list[11] = combination_freq_list[11]+1
		#13
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='True'):
			#combination_list.append(' p+r')
			combination_freq_list[12] = combination_freq_list[12]+1
		#14
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='True' and random_list[i] =='False'):
			#combination_list.append(' p')
			combination_freq_list[13] = combination_freq_list[13]+1
		#15
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='True'):
			#combination_list.append(' r')
			combination_freq_list[14] = combination_freq_list[14]+1
		#16
		if(negfw_list[i] =='False' and featureWise_list[i] =='False' and pairWise_list[i] =='False' and random_list[i] =='False'):
			#combination_list.append(' false')
			combination_freq_list[15] = combination_freq_list[15]+1


	plt.bar(combination_axis, combination_freq_list, align='center', alpha=0.5)
	plt.xticks(combination_axis, combination_list, fontsize=8, rotation=45)
	plt.title("SPLC Conqueror")
	plt.ylabel('Frequency')
	plt.title('Mixed Configs Appearance Rate In '+title+' Fault Rates: Apache')
	plt.savefig(plot_dir+title+"_SPLCMixedconfigs_freq_barchart.png")
	plt.gcf().clear()  



	numberOfAppearance_list_SPLC = [0,0,0,0]
	x_axis = [1,2,3,4]
	x_labels=['negfw','featureWise', 'pairWise', 'random']


	for i in range(0,len(negfw_list)):

		if(negfw_list[i] =='True'):
			numberOfAppearance_list_SPLC[0] = numberOfAppearance_list_SPLC[0]+1

		if(featureWise_list[i] =='True'):
			numberOfAppearance_list_SPLC[1] = numberOfAppearance_list_SPLC[1]+1

		if(pairWise_list[i] =='True'):
			numberOfAppearance_list_SPLC[2] = numberOfAppearance_list_SPLC[2]+1

		if(random_list[i] =='True'):
			numberOfAppearance_list_SPLC[3] = numberOfAppearance_list_SPLC[3]+1


	plt.bar(x_axis, numberOfAppearance_list_SPLC, align='center', alpha=0.5)
	plt.xticks(x_axis, x_labels)
	plt.title("SPLC Conqueror")
	plt.ylabel('Frequency')
	plt.title('Configs Appearance Rate In '+title+' Fault Rates: Apache')
	plt.savefig(plot_dir+title+"_SPLCconfigs_freq_barchart.png")
	plt.gcf().clear()  

barchart_logs(toplog_lines_SPLC, toplog_lines_SPLCext, "Top")
barchart_logs(floplog_lines_SPLC, floplog_lines_SPLCext, "Flop")
