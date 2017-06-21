#This is a modified copy of the file CART.R in the git repository https://github.com/atrisarkar/ces
# 
# Author: Atri
###############################################################################
# rpart() function is a built in R library fuction for Recursive Partitioning and Regression Trees
# CART: building a binary tree, each node is a feature, each path is a configuration, 
# each leave is the performance of the corresponding path configuration


library(rpart)
library(randomForest)
library(gbm)
library(rattle)

source(file="/Users/jula/Github/Cross_ML/ces_modified/path_settings.R")
source(file=script_CART)

# Initialization ##################################################################################
initData <- function(testSet){

	#cat("Please enter full address of the dataset (for example: /Users/Data/Dataset.csv)", '\n')
	#fileAddress <<- scan(file = "", what = " ", n = 1, quiet = TRUE)
	#fileAddress <- "/Users/jula/Github/ces/data/Benchmark/Input/Apache.csv"
	fileAddress <- testSet

	#cat("Please enter address of output folder (for example: /Useres/Data/Output)", '\n')
	#outputAddress <<- scan(file = "", what = " ", n = 1, quiet = TRUE)
	outputAddress <<- Output_CART
	# added one <
	
	#cat("Please enter output filename", "\n")
	#outputFilename <<- scan(file = "", what = " ", n = 1, quiet = TRUE)
	outputFilename <<- "output_CART"
	
	# Load the data
	dataAddr <<- paste("file:///", fileAddress, sep="")
	crs$dataset <- read.csv(dataAddr, na.strings=c(".", "NA", "", "?"), strip.white=TRUE, encoding="UTF-8")
	
	# Calculate number of features
	featureCount <<- ncol(crs$dataset) - 1
	
	# Calculate number of observations
	obsCount <<- nrow(crs$dataset) - 1
}

initGeneralParams <- function(){
	#print("Please enter number of times experiment should be repeated")
	#seedRepetitions <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	seedRepetitions <<- numberOfRounds #5 
	
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
	samplingProgressionBase <<-1 # added one <
	
	#cat("Please enter sampling range lower value", '\n')
	#samplingLower <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	samplingLower <<- 1 # added one <
	
	#cat("Please enter sampling range upper value", '\n')
	#samplingUpper <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	samplingUpper <<- sampleAmount	
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
	# maxDepthLower <- 25
	
	#cat("Please enter maxDepth range upper value", '\n')
	#maxDepthUpper <<- scan(file = "", what = integer(), n = 1, quiet = FALSE)
	# maxDepthUpper <- 30
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
	complexStep <<- minImprovementPerRound  #0.0001
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
	initData(testSet)
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
	faultRate_old <- 0
	faultDataset <- NULL
	resultDataset <- NULL
	resultDataset <- rbind(resultDataset, c("Sampling Amount", "Fault Rate"))
	
	# Main loop ###################################################################################
		for(samplingIter in samplingVector){

					current.faultset <- NULL
					for(seedIter in 1:seedRepetitions){

							# Build the training/validate/test datasets ###############################################
							#set.seed(seedIter)
							crs$nobs <- nrow(crs$dataset)
							crs$sample <- crs$train <- sample(nrow(crs$dataset), samplingIter)
							crs$validate <- NULL
							crs$train.test.diff <- setdiff(setdiff(seq_len(nrow(crs$dataset)), crs$train), crs$validate)
							
							size<-length(crs$train)
							if(size<=100){
								mb <- floor(size/10 + 1/2)
								ms <- mb * 2
							} else {
								ms <- floor(size/10 + 1/2)
								mb <- floor(ms/2)
							}
							
							features.size <- length(colnames(crs$dataset)) - 1
							
							crs$test <- sample(crs$train.test.diff, size)
							# Select the variables
							crs$input <- setdiff(colnames(crs$dataset), "PERF") # 'PERF' -> Function to evaluate the performance
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
							#set.seed(seedIter)
							crs$rpart <- rpart(PERF ~ .,
									data=crs$dataset[crs$train, c(crs$input, crs$target)],method="anova",
									parms=list(split="information"),
									control=rpart.control(
											minsplit=ms,
											minbucket=mb,
											maxdepth=30,
											cp=0,
											usesurrogate=0,
											maxsurrogate=0))
							print("Building Done")
							# Evaluate the CART model #################################################################
							# Obtain predictions for the Decision Tree model on BerkeleyC.csv [test]
							crs$pr <- predict(crs$rpart, newdata=crs$dataset[crs$test, c(crs$input)])
							#print(crs$rpart)   # <<<<<<<<neeeew

							# Extract the relevant variables from the dataset
							sdata <- subset(crs$dataset[crs$test,], select=c("PERF"))
							faultRate <- abs(sdata - crs$pr) / sdata * 100
						
							if(is.null(faultDataset)){
								faultDataset <- faultRate
							}else{
								faultDataset <- cbind(faultDataset, faultRate)
							}
							
							if(is.null(current.faultset)){
								current.faultset <- faultRate
							}else{
								current.faultset <- cbind(current.faultset, faultRate)
							}
							
						 
						
						# Process all results #########################################################################
						#outputFilename.split <- paste(outputFilename,samplingIter, sep="_")
						#address01 <- paste(outputAddress, "/", outputFilename.split, ".csv", sep="")
						#faultSet.row <- t(as.matrix(colMeans(current.faultset)))
						#write.csv(faultSet.row, file=address01,row.names=FALSE)
						#
						
						faultRate <- mean(rowMeans(faultDataset))
						# print(faultRate)
						resultDataset <- rbind(resultDataset, c(samplingIter, faultRate))
						#print("faultRate")
						#print(faultRate)


						faultDataset <- NULL
						}# for(seedIter in 1:seedRepetitions)
						
					if(abs(faultRate-faultRate_old)<complexStep){

							print("Termination reason: minImprovementPerRound")
							break
						}

					faultRate_old <- faultRate
				
		} # for(samplingIter in samplingLower:samplingUpper)
	
		# Output the combined data ####################################################################
		address00 <- paste(outputAddress, "/", outputFilename, ".csv", sep="")
		write.csv(resultDataset, file=address00, row.names=FALSE)
}


#plot(mydata$SampleSize,100-mydata$FaultRate,type="b",col=4,main="LLVM AS",xlab="Sample Size",ylab="Prediction Accuracy")
