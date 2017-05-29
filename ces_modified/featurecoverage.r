#This is a modified copy of the file featurecoverage.r in the git repository https://github.com/atrisarkar/ces
# 
# Author: Atri
###############################################################################


library(rpart)
library(randomForest)
library(gbm)
library(rattle)

# Initialization ##################################################################################
initData <- function(testSet){

	print("\nStarting SAKAR")
	#cat("Please enter full address of the dataset (for example: /Users/Data/Dataset.csv)", '\n')
	#fileAddress <<- scan(file = "", what = " ", n = 1, quiet = TRUE)
	#fileAddress <- "/Users/jula/Github/ces/data/Benchmark/Input/Apache.csv"
	fileAddress <- testSet

	#cat("Please enter address of output folder (for example: /Useres/Data/Output)", '\n')
	#outputAddress <<- scan(file = "", what = " ", n = 1, quiet = TRUE)
	outputAddress <<- "/Users/jula/Github/ces/data/Benchmark/Output_sakar"
	# added one <
	
	#cat("Please enter output filename", "\n")
	#outputFilename <<- scan(file = "", what = " ", n = 1, quiet = TRUE)
	outputFilename <<- "output_sakar"
	
	# Load the data
	dataAddr <<- paste("file:///", fileAddress, sep="")
	crs$dataset <- read.csv(dataAddr, na.strings=c(".", "NA", "", "?"), strip.white=TRUE, encoding="UTF-8")
	
	# Calculate number of features
	#print(colnames(crs$dataset))
	featureCount <<- ncol(crs$dataset) - 1
	
	# Calculate number of observations
	obsCount <<- nrow(crs$dataset) - 1
}

initGeneralParams <- function(){
	#print("Please enter number of times experiment should be repeated")
	#seedRepetitions <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	seedRepetitions <<- 5
	crv$seed <- 1
	
	#print("Please enter name of the method that will be used for experiment")
	#methodName <<- scan(file = "", what = " ", n = 1, quiet = TRUE)
	methodName <<- "anova"
}

initSamplingParams <- function(){
	#print("Please enter sampling units (1 - observations; 2 - percentage; 3 - coefficient)")
	#samplingType <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	samplingType <<- 1
	
	#print("Please enter sampling progression (1 - arithmetic; 2 - geometric)")
	#samplingProgression <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	samplingProgression <<- 1
	
	#print("Please enter progression base")
	#samplingProgressionBase <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	samplingProgressionBase <<-1
	
	#cat("Please enter sampling range lower value", '\n')
	#samplingLower <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	samplingLower <<- 1
	
	#cat("Please enter sampling range upper value", '\n')
	#samplingUpper <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	samplingUpper <<- (floor(obsCount/2) %/%  samplingProgressionBase)*samplingProgressionBase
}

initMinSplitParams <- function(){
	#cat("Please enter minSplit range lower value", '\n')
	#minSplitLower <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	# minSplitLower <- 2
	
	#cat("Please enter minSplit range upper value", '\n')
	#minSplitUpper <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	# minSplitUpper <- 5
}

initMinBucketParams <- function(){
	#cat("Please enter minBucket range lower value", '\n')
	#minBucketLower <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	# minBucketLower <- 2
	
	#cat("Please enter minBucket range upper value", '\n')
	#minBucketUpper <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	# minBucketUpper <- 5
}

initMaxDepthParams <- function(){
	#cat("Please enter maxDepth range lower value", '\n')
	#maxDepthLower <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	maxDepthLower <<- 25
	
	#cat("Please enter maxDepth range upper value", '\n')
	#maxDepthUpper <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	maxDepthUpper <<- 30
}

initComplexityParams <- function(){
	#cat("Please enter complexity range lower value", '\n')
	#complexLower <<- scan(file = "", what = numeric(), n = 1, quiet = FALSE)
	complexLower <- 0
	
	#cat("Please enter complexity range upper value", '\n')
	#complexUpper <<- scan(file = "", what = numeric(), n = 1, quiet = FALSE)
	complexUpper <- 0.001
	
	#cat("Please enter complexity step", '\n')
	#complexStep <<- scan(file = "", what = numeric(), n = 1, quiet = FALSE)
	complexStep <- 0.0001
}

initCARTParams <- function(){
	initMinSplitParams()
	initMinBucketParams()
	initMaxDepthParams()
	initComplexityParams()
}

initParams <- function(){
	initGeneralParams()
	initSamplingParams()
	initCARTParams()
}

init <- function(){
	initData()
	initParams()
}

# Analysis ########################################################################################
analyse <- function(){
	
	# Calculate sampling progression ##############################################################
	samplingVector <<- NULL
	samplingAcc <- samplingLower
	
	while(samplingAcc <= samplingUpper)
	{
		samplingVector <<- c(samplingVector, samplingAcc)
		
		if(samplingProgression == 1) # Arithmetic progression
		{
			samplingAcc <- samplingAcc + samplingProgressionBase
		}
		else # Geometric progression
		{
			samplingAcc <- samplingAcc * samplingProgressionBase
		}
	}
	
	if(samplingType == 1) # Observations
	{
		samplingVector <<- samplingVector
	}
	if(samplingType == 2) # Percentage
	{
		samplingVector <<- round(samplingVector * obsCount / 100, digits = 0)
	}
	if(samplingType == 3) # Coefficient
	{
		samplingVector <<- samplingVector * featureCount
	}
	
	# Analyse data ################################################################################
	analyseCART()
}

analyseCART <- function()
{
	# Utility variables ###########################################################################
	faultDataset <- NULL
	resultDataset <- NULL
	resultDataset <- rbind(resultDataset, c("Sampling Amount", "MaxDepth", "Fault Rate"))
	crs$dataset <- read.csv(dataAddr, na.strings=c(".", "NA", "", "?"), strip.white=TRUE, encoding="UTF-8")
	
	# Main loop ###################################################################################
	for(samplingIter in samplingVector){
		for(maxDepthIter in maxDepthLower:maxDepthUpper){
					for(seedIter in 1:seedRepetitions){
						
						# setting mandatory features for SQLite
						#mand <<- c("OperatingSystemCharacteristics","EnableFeatures","DisableFeatures","OmitFeatures","Options","SetAutoVacuum","SetCacheSize","LockingMode","PageSize","HighestPageSize","PERF")
						
						
					
						#conf <<- matrix(0,2,length(colnames(crs$dataset))-length(mand))
						conf <<- matrix(0,2,length(colnames(crs$dataset)))
						#colnames(conf) <<- setdiff(colnames(crs$dataset), mand)
						
						# Build the training/validate/test datasets ###############################################
						set.seed(seedIter)
						crs$nobs <- nrow(crs$dataset)
						crs$sample <- crs$train <- sample(nrow(crs$dataset), samplingIter)
						crs$validate <- NULL
						crs$train.test.diff <- setdiff(setdiff(seq_len(nrow(crs$dataset)), crs$train), crs$validate)
						
						#add(crs$sample)
						#print(samplingIter)
						size<-length(crs$train)
						if(size<=100){
							mb <- floor(size/10 + 1/2)
							ms <- mb * 2
						} else {
							ms <- floor(size/10 + 1/2)
							mb <- floor(ms/2)
						}
						
						crs$test <- sample(crs$train.test.diff, size)
						# Select the variables
						crs$input <- setdiff(colnames(crs$dataset), "PERF")
						crs$numeric <- NULL
						crs$categoric <- NULL
						crs$target  <- "PERF"
						crs$risk    <- NULL
						crs$ident   <- NULL
						crs$ignore  <- NULL
						crs$weights <- NULL
						print("Training Done")
						# Building a CART model ###################################################################
						require(rpart, quietly=TRUE)
						set.seed(seedIter)
						crs$rpart <- rpart(PERF ~ .,
								data=crs$dataset[crs$train, c(crs$input, crs$target)],method="anova",
								parms=list(split="information"),
								control=rpart.control(
										minsplit=ms,
										minbucket=mb,
										maxdepth=maxDepthIter,
										cp=0,
										usesurrogate=0,
										maxsurrogate=0))
						print("Building Done")
						# Evaluate the CART model #################################################################
						# Obtain predictions for the Decision Tree model on BerkeleyC.csv [test]
						crs$pr <- predict(crs$rpart, newdata=crs$dataset[crs$test, c(crs$input)])
						# Extract the relevant variables from the dataset
						sdata <- subset(crs$dataset[crs$test,], select=c("PERF"))
						faultRate <- abs(sdata - crs$pr) / sdata * 100
						if(is.null(faultDataset)){
							faultDataset <- faultRate
						}else{
							faultDataset <- cbind(faultDataset, faultRate)
						}
						
						
						
						
					} # for(seedIter in 1:seedRepetitions)
					
					# Process all results #########################################################################
					faultRate <- mean(rowMeans(faultDataset))
					# print(faultRate)
					resultDataset <- rbind(resultDataset, c(samplingIter,
									maxDepthIter, faultRate))
					
					faultDataset <- NULL
					
				} # for(maxDepthIter in maxDepthLower:maxDepthUpper)
				#complete <- complete()
				#if(complete){
				#	break;
				#}
	} # for(samplingIter in samplingLower:samplingUpper)
	
	# Output the combined data ####################################################################
	address00 <- paste(outputAddress, "/", outputFilename, ".csv", sep="")
	write.csv(resultDataset, file=address00, row.names=FALSE)
}

add <- function(x){
	for(j in 1:length(x)){
		x1 <- x[j]
		crs.validate <- NULL
		crs.train <- x1
		crs.input <- setdiff(colnames(crs$dataset), mand)
		g <<- crs$dataset[crs.train, c(crs.input)]
		for(i in 1:ncol(g)){
			row <- g[i]
			if(row=="Y"){
				conf[1,i] <<- conf[1,i] + 1
			} else {
				conf[2,i] <<- conf[2,i] + 1
			}
			
		}
	}
	
}

complete <- function(){
	print(conf)
	m <- (conf[,] >=4 )
	res <- TRUE
	for(i in 1:nrow(m)) {
		for (j in col(m)){
			if(m[i,j]==FALSE){
				res <- FALSE
				break
			}
			if(res==FALSE){
				break
			}
		}
	}
	return(res)
}

#plot(mydata$SampleSize,100-mydata$FaultRate,type="b",col=4,main="LLVM AS",xlab="Sample Size",ylab="Prediction Accuracy")
