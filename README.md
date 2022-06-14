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
  
------------------------------------
[Finding_n_Dealing_Outliers.py, 3,20, 15-Jun-2022], desc: The script contains function to find the outliers in integer/float columns, the function takes dataframe as arugument, and returns the output as dataframe
  
Example:
              [min, max]	  median	    [25, 75qnt]	          IQR	        [l, uwisk]	            #oliers_ls_lw	    #oliers_gr_uw
              -----	        -----	      -----		              -----       -----                   -----             -----
customer_id	  [1, 30301]	  15150.5	    [7557.25, 22706.75]	  15149.5	    [-7573.75, 37874.75]	  28382	            0
vintage	      [73, 2476]	  2154.0	    [1958.0, 2292.0]	    334.0	      [1653.0, 2655.0]	      26272	            0
age	          [1, 90]	      46.0	      [36.0, 60.0]	        24.0	      [10.0, 82.0]	          27981	            1306
dependents	  [0.0, 52.0]	  0.0	        [0.0, 0.0]	          0.0	        [0.0, 0.0]	            6947	            6947
  
[Finding_n_Dealing_Outliers.py, 22,47, 15-Jun-2022], desc: The script contains function to deal with outiers, a box plot is returned as a result, the function takes, the dataframe, list of columns and a include_outlier flag (True/False), if include_outlier = True, a box plot wil be returned with outliers and median value, and if the include_outlier = False, the columns will be treated for outliers, with any value lower than lower wisker replaced by lower wisker - 1, and any value grater than upper wisker replaced by upper wisker + 1, and a box plot would be returned with IQR, Median, 25th and 75th Quartiles, Lower and upper wisker values for each column
