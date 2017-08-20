
args <- commandArgs(trailingOnly=TRUE)

# starting sarkar
source(file="C:\\Users\\Jula\\Documents\\Projekt\\Cross_ML\\ces_modified\\path_settings.R")
source(file=algo_SARKAR)

initData(args[1])
initParams()
analyse()