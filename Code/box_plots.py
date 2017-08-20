import matplotlib.pyplot as plt
import matplotlib
import statistics as stats
from findstring import find_value_logAll2, find_lines_logAll, find_value_logAll_float, find_value_logAll_int
from findstring import find_top_faultrates_lines_logAll, find_flop_faultrates_lines_logAll, find_explorerSPLCext_lines_logAll
from findstring import find_SPLC_feature_lines_logAll
from path_settings import init_paths
path_list = init_paths()

plot_dir = path_list[9]
SPLC_logAll = path_list[10]
SPLCext_logAll = path_list[16]
CART_logAll = path_list[11]
SARKAR_logAll = path_list[12]


# log_lines_SPLC = find_lines_logAll(SPLC_logAll)
# log_lines_SPLCext = find_lines_logAll(SPLCext_logAll)
# log_lines_CART = find_lines_logAll(CART_logAll)
# log_lines_SARKAR = find_lines_logAll(SARKAR_logAll)

exeTimes_toplog_lines_SPLC = find_top_faultrates_lines_logAll(SPLC_logAll, "executionTime:", 10)
exeTimes_toplog_lines_SPLCext = find_top_faultrates_lines_logAll(SPLCext_logAll, "executionTime:", 10)
exeTimes_toplog_lines_CART = find_top_faultrates_lines_logAll(CART_logAll, "executionTime:", 10)
exeTimes_toplog_lines_SARKAR = find_top_faultrates_lines_logAll(SARKAR_logAll, "executionTime:", 10)

exeTimes_floplog_lines_SPLC = find_flop_faultrates_lines_logAll(SPLC_logAll, "executionTime:", 10)
exeTimes_floplog_lines_SPLCext = find_flop_faultrates_lines_logAll(SPLCext_logAll, "executionTime:", 10)
exeTimes_floplog_lines_CART = find_flop_faultrates_lines_logAll(CART_logAll, "executionTime:", 10)
exeTimes_floplog_lines_SARKAR = find_flop_faultrates_lines_logAll(SARKAR_logAll, "executionTime:", 10)


faultRate_toplog_lines_SPLC = find_top_faultrates_lines_logAll(SPLC_logAll, "faultRate:", 10)
faultRate_toplog_lines_SPLCext = find_top_faultrates_lines_logAll(SPLCext_logAll, "faultRate:", 10)
faultRate_toplog_lines_CART = find_top_faultrates_lines_logAll(CART_logAll, "faultRate:", 10)
faultRate_toplog_lines_SARKAR = find_top_faultrates_lines_logAll(SARKAR_logAll, "faultRate:", 10)

faultRate_floplog_lines_SPLC = find_flop_faultrates_lines_logAll(SPLC_logAll, "faultRate:", 10)
faultRate_floplog_lines_SPLCext = find_flop_faultrates_lines_logAll(SPLCext_logAll, "faultRate:", 10)
faultRate_floplog_lines_CART = find_flop_faultrates_lines_logAll(CART_logAll, "faultRate:", 10)
faultRate_floplog_lines_SARKAR = find_flop_faultrates_lines_logAll(SARKAR_logAll, "faultRate:", 10)


faultRate_log_lines_SPLC = find_lines_logAll(SPLC_logAll)
faultRate_log_lines_SPLCext = find_lines_logAll(SPLCext_logAll)
faultRate_log_lines_CART = find_lines_logAll(CART_logAll)
faultRate_log_lines_SARKAR = find_lines_logAll(SARKAR_logAll)



expl_rdm_lines_SPLCext = find_explorerSPLCext_lines_logAll(SPLCext_logAll, "explorer-random")
expl_max_dist_lines_SPLCext = find_explorerSPLCext_lines_logAll(SPLCext_logAll, "explorer-max-distance")
expl_max_err_lines_SPLCext = find_explorerSPLCext_lines_logAll(SPLCext_logAll, "explorer-max-error")
expl_combi_lines_SPLCext = find_explorerSPLCext_lines_logAll(SPLCext_logAll, "explorer-combi")
expl_omni_lines_SPLCext = find_explorerSPLCext_lines_logAll(SPLCext_logAll, "explorer-omni")

nfpr_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'True', 'True', 'True') #1
nfp_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'True', 'True', 'False') #2
nfr_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'True', 'False', 'True') #3
npr_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'False', 'True', 'True') #4
nf_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'True', 'False', 'False') #5
np_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'False', 'True', 'False') #6
nr_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'False', 'False', 'True') #7
n_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'True', 'False', 'False', 'False') #8
fpr_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'True', 'True', 'True') #9
fp_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'True', 'True', 'False') #10
fr_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'True', 'False', 'True') #11
f_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'True', 'False', 'False') #12
pr_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'False', 'True', 'True') #13
p_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'False', 'True', 'False') #14
r_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'False', 'False', 'True') #15
false_lines_SPLC = find_SPLC_feature_lines_logAll(SPLC_logAll, 'False', 'False', 'False', 'False') #16



def boxplot_logs_seperated(log_lines_SPLC, log_lines_SPLCext, log_lines_CART, log_lines_SARKAR, topflop, meas_feature, data):


	# Boxplot execution times

	list_SPLC = find_value_logAll_float(log_lines_SPLC,meas_feature)
	list_SPLCext = find_value_logAll_float(log_lines_SPLCext,meas_feature)
	list_CART = find_value_logAll_float(log_lines_CART,meas_feature)
	list_SARKAR = find_value_logAll_float(log_lines_SARKAR,meas_feature)

	plt.figure()
	plt.boxplot([list_CART, list_SARKAR])
	plt.xticks([1,2], ['CART','SARKAR'])
	plt.title(meas_feature+" of "+topflop+" "+data)
	plt.savefig(plot_dir+meas_feature+"_of_"+topflop+"_"+data+"_boxplot_R.png")
	plt.gcf().clear()  

	plt.figure()
	plt.boxplot([list_SPLC, list_SPLCext])
	plt.xticks([1,2], ['SPLC','SPLCext'])
	plt.title(meas_feature+" of "+topflop+" "+data)
	plt.savefig(plot_dir+meas_feature+"_of_"+topflop+"_"+data+"_boxplot_SPLC.png")
	plt.gcf().clear()  


def boxplot_logs(log_lines_SPLC, log_lines_SPLCext, log_lines_CART, log_lines_SARKAR, topflop, meas_feature, data):
	# Boxplot faultRate
	
	list_SPLC = find_value_logAll_float(log_lines_SPLC,meas_feature)
	list_SPLCext = find_value_logAll_float(log_lines_SPLCext,meas_feature )
	list_CART = find_value_logAll_float(log_lines_CART,meas_feature )
	list_SARKAR = find_value_logAll_float(log_lines_SARKAR,meas_feature)

	plt.figure()
	plt.boxplot([list_SPLC, list_SPLCext, list_CART, list_SARKAR])
	plt.xticks([1,2,3,4], ['SPLC','SPLCext','CART','SARKAR'])
	plt.title(meas_feature+" of "+topflop+" "+data)
	plt.savefig(plot_dir+meas_feature+"_of_"+topflop+"_"+data+"_boxplot_.png")
	plt.gcf().clear() 



def boxplot_logs_expl(log_lines_expl_rdm, log_lines_expl_max_dist, log_lines_expl_max_err, log_lines_expl_combi, log_lines_expl_omni, meas_feature, data):
	# Boxplot faultRate
	
	list_expl_rdm = find_value_logAll_float(log_lines_expl_rdm,meas_feature)
	list_expl_max_dist = find_value_logAll_float(log_lines_expl_max_dist,meas_feature )
	list_expl_max_err = find_value_logAll_float(log_lines_expl_max_err,meas_feature )
	list_expl_combi = find_value_logAll_float(log_lines_expl_combi,meas_feature)
	list_expl_omni = find_value_logAll_float(log_lines_expl_omni,meas_feature)

	plt.figure()
	plt.boxplot([list_expl_rdm, list_expl_max_dist, list_expl_max_err, list_expl_combi, list_expl_omni])
	plt.xticks([1,2,3,4,5], ['expl_rdm','expl_max_dist','expl_max_err','expl_combi', 'expl_omni'])
	plt.title(meas_feature+" of "+data)
	plt.savefig(plot_dir+meas_feature+"_of_"+data+"_SPLCext_boxplot_.png")
	plt.gcf().clear()  





def boxplot_logs_features_SPLC(nfpr_lines_SPLC, nfp_lines_SPL, nfr_lines_SPL, npr_lines_SPL, nf_lines_SPL, np_lines_SPL, 
	nr_lines_SPL, n_lines_SPL, fpr_lines_SPL, fp_lines_SPL, fr_lines_SPL, f_lines_SPL, pr_lines_SPL, p_lines_SPL, 
	r_lines_SPL, false_lines_SPLC, meas_feature, data):
	
	list_nfpr = find_value_logAll_float(nfpr_lines_SPLC,meas_feature)
	list_nfp = find_value_logAll_float(nfp_lines_SPL,meas_feature )
	list_nfr = find_value_logAll_float(nfr_lines_SPL,meas_feature )
	list_npr = find_value_logAll_float(npr_lines_SPL,meas_feature)
	list_nf = find_value_logAll_float(nf_lines_SPL,meas_feature)
	list_np = find_value_logAll_float(np_lines_SPL,meas_feature)
	list_nr = find_value_logAll_float(nr_lines_SPL,meas_feature)
	list_n = find_value_logAll_float(n_lines_SPL,meas_feature)
	list_fpr = find_value_logAll_float(fpr_lines_SPL,meas_feature)
	list_fp = find_value_logAll_float(fp_lines_SPL,meas_feature)
	list_fr = find_value_logAll_float(fr_lines_SPL,meas_feature)
	list_f = find_value_logAll_float(f_lines_SPL,meas_feature)
	list_pr = find_value_logAll_float(pr_lines_SPL,meas_feature)
	list_p = find_value_logAll_float(p_lines_SPL,meas_feature)
	list_r = find_value_logAll_float(r_lines_SPL,meas_feature)
	list_false = find_value_logAll_float(false_lines_SPLC,meas_feature)


	plt.figure()
	plt.boxplot([list_nfpr, list_nfp, list_nfr, list_npr, list_nf, list_np, list_nr, list_n, list_fpr, list_fp, list_fr, list_f, list_pr, list_p, list_r, list_false])
	plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], ['nfpr', 'nfp', 'nfr', 'npr', 'nf', 'np', 'nr', 'n', 'fpr', 'fp', 'fr', 'f', 'pr', 'p', 'r', 'false'])
	plt.title(meas_feature+" of "+data)
	plt.savefig(plot_dir+meas_feature+"_of_"+data+"_SPLC_boxplot_.png")
	plt.gcf().clear()  




boxplot_logs_seperated(exeTimes_toplog_lines_SPLC, exeTimes_toplog_lines_SPLCext, exeTimes_toplog_lines_CART, exeTimes_toplog_lines_SARKAR, "Top10", "executionTime", "executionTime_Apache_data")
boxplot_logs_seperated(exeTimes_floplog_lines_SPLC, exeTimes_floplog_lines_SPLCext, exeTimes_floplog_lines_CART, exeTimes_floplog_lines_SARKAR, "Flop10", "executionTime", "executionTime_Apache_data")

boxplot_logs_seperated(exeTimes_toplog_lines_SPLC, exeTimes_toplog_lines_SPLCext, exeTimes_toplog_lines_CART, exeTimes_toplog_lines_SARKAR, "Top10", "faultRate", "executionTime_Apache_data")
boxplot_logs_seperated(exeTimes_floplog_lines_SPLC, exeTimes_floplog_lines_SPLCext, exeTimes_floplog_lines_CART, exeTimes_floplog_lines_SARKAR, "Flop10", "faultRate", "executionTime_Apache_data")

boxplot_logs(faultRate_toplog_lines_SPLC, faultRate_toplog_lines_SPLCext, faultRate_toplog_lines_CART, faultRate_toplog_lines_SARKAR, "Top10", "faultRate", "faultRate_Apache_data")
boxplot_logs(faultRate_floplog_lines_SPLC, faultRate_floplog_lines_SPLCext, faultRate_floplog_lines_CART, faultRate_floplog_lines_SARKAR, "Flop10", "faultRate", "faultRate_Apache_data")

boxplot_logs(faultRate_log_lines_SPLC, faultRate_log_lines_SPLCext, faultRate_log_lines_CART, faultRate_log_lines_SARKAR, "ALL", "faultRate", "Apache_data")
boxplot_logs_seperated(faultRate_log_lines_SPLC, faultRate_log_lines_SPLCext, faultRate_log_lines_CART, faultRate_log_lines_SARKAR, "ALL", "executionTime", "Apache_data")

boxplot_logs_expl(expl_rdm_lines_SPLCext, expl_max_dist_lines_SPLCext, expl_max_err_lines_SPLCext, expl_combi_lines_SPLCext, expl_omni_lines_SPLCext, "faultRate", "Apache_data")

boxplot_logs_features_SPLC(nfpr_lines_SPLC, nfp_lines_SPLC, nfr_lines_SPLC, npr_lines_SPLC, nf_lines_SPLC, np_lines_SPLC, 
	nr_lines_SPLC, n_lines_SPLC, fpr_lines_SPLC, fp_lines_SPLC, fr_lines_SPLC, f_lines_SPLC, pr_lines_SPLC, 
	p_lines_SPLC, r_lines_SPLC, false_lines_SPLC, "faultRate", "Apache_data")