import matplotlib.pyplot as plt
import matplotlib
import statistics as stats
from tabulate import tabulate
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


faultRate_log_lines_SPLC = find_lines_logAll(SPLC_logAll)
faultRate_log_lines_SPLCext = find_lines_logAll(SPLCext_logAll)
faultRate_log_lines_CART = find_lines_logAll(CART_logAll)
faultRate_log_lines_SARKAR = find_lines_logAll(SARKAR_logAll)


def print_faultrate_stats(log_lines_SPLC, log_lines_SPLCext, log_lines_CART, log_lines_SARKAR, meas_feature, data):

	list_SPLC = find_value_logAll_float(log_lines_SPLC,meas_feature)
	list_SPLCext = find_value_logAll_float(log_lines_SPLCext,meas_feature )
	list_CART = find_value_logAll_float(log_lines_CART,meas_feature )
	list_SARKAR = find_value_logAll_float(log_lines_SARKAR,meas_feature)


	mean_CART = str(round(stats.mean(list_CART),3))
	mean_SARKAR = str(round(stats.mean(list_SARKAR),3))
	mean_SPLC = str(round(stats.mean(list_SPLC),3))
	mean_SPLCext = str(round(stats.mean(list_SPLCext),3))

	median_CART = str(round(stats.median(list_CART),3))
	median_SARKAR = str(round(stats.median(list_SARKAR),3))
	median_SPLC = str(round(stats.median(list_SPLC),3))
	median_SPLCext = str(round(stats.median(list_SPLCext),3))

	stdev_CART = str(round(stats.stdev(list_CART),3))
	stdev_SARKAR = str(round(stats.stdev(list_SARKAR),3))
	stdev_SPLC = str(round(stats.stdev(list_SPLC),3))
	stdev_SPLCext = str(round(stats.stdev(list_SPLCext),3))

	variance_CART = str(round(stats.variance(list_CART),3))
	variance_SARKAR = str(round(stats.variance(list_SARKAR),3))
	variance_SPLC = str(round(stats.variance(list_SPLC),3))
	variance_SPLCext = str(round(stats.variance(list_SPLCext),3))

	print("\n"+data+"\n")

	print(tabulate(	[['mean', mean_CART, mean_SARKAR, mean_SPLC, mean_SPLCext], 
					['median', median_CART, median_SARKAR, median_SPLC, median_SPLCext], 
					['standard dev', stdev_CART, stdev_SARKAR, stdev_SPLC, stdev_SPLCext],
					['variance', variance_CART, variance_SARKAR, variance_SPLC, variance_SPLCext]], 
					headers=[meas_feature, 'CART', 'SARKAR', 'SPLC', 'SPLC AL']))
	print("\n")


print_faultrate_stats(faultRate_log_lines_SPLC, faultRate_log_lines_SPLCext, faultRate_log_lines_CART, faultRate_log_lines_SARKAR, "faultRate", "Apache_data")
print_faultrate_stats(faultRate_log_lines_SPLC, faultRate_log_lines_SPLCext, faultRate_log_lines_CART, faultRate_log_lines_SARKAR, "executionTime", "Apache_data")
