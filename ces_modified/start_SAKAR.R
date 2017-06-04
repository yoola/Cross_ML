
args <- commandArgs(trailingOnly=TRUE)

# starting sakar
source(file="/Users/jula/Github/Cross_ML/ces_modified/path_settings.R")
source(file=algo_SAKAR)

initData(args[1])
initParams()
analyse()