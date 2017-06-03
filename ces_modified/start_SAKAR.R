
args <- commandArgs(trailingOnly=TRUE)

# starting sakar
source(file="/Users/jula/Github/ces/source/featurecoverage.R")

initData(args[1])
initParams()
analyse()