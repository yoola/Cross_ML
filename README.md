- Machine Learning Cross Platform (for Mac OSX)

- Download git respositories: 
	- https://github.com/yoola/Cross_ML
	- SPL Conqueror: https://github.com/se-passau/SPLConqueror


Do the following steps:

For SPL Conqueror:  
	
	- in the Xamarin environment:  
		- do right click on folder CommandLine -> options -> Default -> arguments  
		- type in the path .../Cross_ML/Setting_scripts/script_SPLC.a  
	- Compile the program SPL Conqueror with Xamarin Studio  
	- see more instructions for SPL Conqueror on https://github.com/se-passau/SPLConqueror  
	- change paths in Cross_ML/Code/path_settings.py accordingly


For CART and Sakar:  

	- change paths in all of the files in the folder Cross_ML/ces_modified accordingly
	- the files are modified versions from https://github.com/atrisarkar/ces
	

Run the file start.py in the Cross_ML/Code folder

Note: To run this program on a different operating system than OSX, change the command in start.py accordingly: os.system("your command")
