- Machine Learning Cross Platform (for Mac OSX)

- Download git respositories: 
	- https://github.com/yoola/Cross_ML
	- SAKAR and CART: https://github.com/atrisarkar/ces
	- SPL Conqueror: https://github.com/se-passau/SPLConqueror


Do the following steps:

For SPL Conqueror:  
	
	- in the Xamarin environment:  
		- do right click on folder CommandLine -> options -> Default -> arguments  
		- type in the path .../Cross_ML/Code/script.a  
	- Compile the program SPL Conqueror with Xamarin Studio  
	- see more instructions for SPL Conqueror on https://github.com/se-passau/SPLConqueror  
	- make sure you created/have the folder Cross_ML/Outputs and CrossML/Code/Plots
	- change paths in Cross_ML/Code/path_settings.py accordingly


For CART and Sakar:  

	- replace or add the files in the ces/source repository with the source files in Cross_ML/ces_modified  
	- create an Output folder for the CART and Sakar results  
	- change paths in all files copied from Cross_ML/ces_modified accordingly  

Note: To run this program on a different operating system than OSX, change the command in start.py accordingly: os.system("your command")
