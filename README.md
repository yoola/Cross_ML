Machine Learning Cross Platform

- Download git respositories: 
	- https://github.com/yoola/Cross_ML
	- SPL Conqueror: https://github.com/se-passau/SPLConqueror
	- SPL Conqueror extended: https://github.com/mcguenther/SPLConqueror/tree/activeLearning


Do the following steps:

* For SPL Conqueror and SPL Conqueror extended:  
	
	- For Mac OSX in the Xamarin environment:  
		- do right click on folder CommandLine -> options -> Default -> arguments  
		- type in the path .../Cross_ML/Setting_scripts/script_SPLC.a  .../Cross_ML/Setting_scripts/script_SPLCext.a  
	- Compile the program with Xamarin Studio  
	- see more instructions for other operating systems (Windows, Linux) on https://github.com/se-passau/SPLConqueror  


* For CART and Sakar:  

	- change paths in all of the files in the folder Cross_ML/ces_modified accordingly
	- the files are modified versions from https://github.com/atrisarkar/ces
	- make sure you have R installed and the packages randomForest, gbm, rattle, GTK+ and RGtk2
	

* Change all paths in .../Cross_ML/Code/path_settings.py accordingly

* Make sure you have python 3 or higher installed

* Run the file start.py in the Cross_ML/Code folder

* For more plots run the files graph_plot.py, box_plot.py, bar_chart.py and print_results.py

Note: 

* To run this program on a different operating system than OSX, change the command in start.py accordingly: os.system("your command") and all paths in .../Cross_ML/Code/path_settings.py and .../Cross_ML/ces_modified/

* For Windows you can replace all according files with the ones in the ../Cross_ML/Windows_version folder


