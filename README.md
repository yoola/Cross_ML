Machine Learning Cross Platform (for Mac OSX)

- Download git respositories: 
	- https://github.com/yoola/Cross_ML
	- SPL Conqueror: https://github.com/se-passau/SPLConqueror
	- SPL Conqueror extended: https://github.com/mcguenther/SPLConqueror/tree/activeLearning


Do the following steps:

* For SPL Conqueror and SPL Conqueror extended:  
	
	- in the Xamarin environment:  
		- do right click on folder CommandLine -> options -> Default -> arguments  
		- type in the path .../Cross_ML/Setting_scripts/script_SPLC.a  .../Cross_ML/Setting_scripts/script_SPLCext.a  
	- Compile the program with Xamarin Studio  
	- see more instructions for SPL Conqueror on https://github.com/se-passau/SPLConqueror  


* For CART and Sakar:  

	- change paths in all of the files in the folder Cross_ML/ces_modified accordingly
	- the files are modified versions from https://github.com/atrisarkar/ces
	

* Change all paths in .../Cross_ML/Code/path_settings.py accordingly

* Run the file start.py in the Cross_ML/Code folder

Note: To run this program on a different operating system than OSX, change the command in start.py accordingly: os.system("your command")
