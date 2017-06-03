# Run model
# 
args <- commandArgs(trailingOnly=TRUE)

#starting CART
source(file="/Users/jula/Github/ces/source/CART.R")

# Benchmark input csv, Output folder, number of experiment repetitions
# arithmetic or geometric, sampling lower and upper range
# complexity range upper/lower value, complexity step
# init()
initData(args[1])
initParams()

# building sample vector
# build CART model
# reading each dataset and compare with the predicted value for evaluation -> calculating error
# output formatting
# Once rpart() function is called, you can print the CART model by calling 'print(crs$rpart)'
analyse() #calls analyseCART();







#source(file="/Users/jula/Github/ces/source/projective.r")
#output: correlationcoefficient of functions (log, weiss, power, exp)
#go();



# Outputs Sample-Size Accuracy in +10 steps
# accuracy: 100-fault rate, fault rates can be found in Output folder
#source('/Users/jula/Github/ces/source/graph_ggplot.R')

#Accuracy graph of x264 (can be for others too)
#explanation: 
#projective: black = exponentiell, green = power, 
#triangle = optimal sample size, rectangle = inital datapoints for projection
#progressiv: red
#krass hardcodiert
#source('graphplot.R') 

# histogram with accuracies for all datasets (Apache, SQLite, x264,..)
# grey = progressiv, black = projective
# krass hardcodiert
#source('/Users/jula/Github/ces/source/histogram.R') 