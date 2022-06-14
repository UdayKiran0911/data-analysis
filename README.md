# data-analysis
A repository consisting of python scripts useful for data walkthrough, preprocessing, exploration and predictive Machine Learning

Created on: 1 June 2022

-----------------------------------

File Editing Rules:

Format >> "["file name", #start line num.", "end line num.", "date of edit"], desc:<description>"
  
Example >> "[getNaNInfo.py, 12,25, 1-Jun-2022], desc: script to get the dataset NaN Information
  
-----------------------------------

[MissingValueInfo.py, 3,13, 1-Jun-2022], desc:The script contains function to find the missing values information, <dtype>: <dtype>: the type of the variable, <#NAs>: the number of missing values in the variable, <NA_byTNA_pct>: Missing value percentage with respect to total missing values in the dataset, <NA_byRows_pct>: Missing value percentage with respect to total rows in dataset, <head>: first 5 values of the variable, and returns a dataframe

Example:
dtype	  #NAs	  NA_byTNA_pct	NA_byRows_pct	  head
-----	  -----	  -----		      -----		        -----
object	525	    7.4	          1.85	          ['Male' 'Male' 'Male']
float64	2463	  34.72	        8.68	          [0. 0. 0.]
object	80	    1.13	        0.28	          ['self_employed' 'self_employed' 'salaried']
float64	803	    11.32	        2.83	          [187.  nan 146.]
object	3223	  45.43	        11.36	          ['5/21/2019' '11/1/2019' nan]
  

------------------------------------
[MissingValueResolve.py, 3,25, 15-Jun-2022], desc: The script contains function to replace the missing values by Mean, Median, Mode and Userdefined constant value, the function takes data (dataframe), list of columns (columns containing missing values) and the list of Substitutes ("Mean", "Median", "Mode", <constant>), the function will return a summary of the execution as dataframe, with list of columns as index
  
Example:
            #NAs	      replacedby	prefill	        postfill
            -----	      -----	      -----		        -----
gender	    525	        mode	      Male	          Male
dependents	2463	      mean	      0.347236	      0.347236
occupation	80	        mode	      self_employed	  self_employed
city	      803	        mode	      1020.0	        1020.0
