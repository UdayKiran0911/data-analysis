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
  
------------------------------------
[DataDescription_DTypeConvert.py, 3,50, 18-Jun-2022], desc: The script contains function to help get the metadata or the description of data, it inludes shape, dtypes, missing value info, it also have the data spread information of int/float, categorical variables, the function prints the information
  
Example:
Shape: Rows = 28382, Columns = 21

Dtype:
 |                |   0 |
|:---------------|----:|
| float64        |  12 |
| int64          |   6 |
| object         |   2 |
| datetime64[ns] |   1 | 

Missing Value info:
 |                  |   #NA |   in% |
|:-----------------|------:|------:|
| last_transaction |  3223 | 11.36 |
| dependents       |  2463 |  8.68 |
| city             |   803 |  2.83 |
| gender           |   525 |  1.85 |
| occupation       |    80 |  0.28 | 

Integer data spread:
 |                                | type    |       min |             max |         mean |   median |       stddev |
|:-------------------------------|:--------|----------:|----------------:|-------------:|---------:|-------------:|
| customer_id                    | int64   |      1    | 30301           | 15143.5      | 15150.5  |  8746.45     |
| vintage                        | int64   |     73    |  2476           |  2091.14     |  2154    |   272.677    |
| age                            | int64   |      1    |    90           |    48.2083   |    46    |    17.8072   |
| dependents                     | float64 |      0    |    52           |     0.347236 |     0    |     0.997661 |
| city                           | float64 |      0    |  1649           |   796.11     |   834    |   432.872    |
| customer_nw_category           | int64   |      1    |     3           |     2.22553  |     2    |     0.660443 |
| branch_code                    | int64   |      1    |  4782           |   925.975    |   572    |   937.799    |
| current_balance                | float64 |  -5503.96 |     5.9059e+06  |  7380.55     |  3281.26 | 42598.7      |
| previous_month_end_balance     | float64 |  -3149.57 |     5.74044e+06 |  7495.77     |  3379.91 | 42529.3      |
| average_monthly_balance_prevQ  | float64 |   1428.69 |     5.70029e+06 |  7496.78     |  3542.86 | 41726.2      |
| average_monthly_balance_prevQ2 | float64 | -16506.1  |     5.01017e+06 |  7124.21     |  3359.6  | 44575.8      |
| current_month_credit           | float64 |      0.01 |     1.22698e+07 |  3433.25     |     0.61 | 77071.5      |
| previous_month_credit          | float64 |      0.01 |     2.36181e+06 |  3261.69     |     0.63 | 29688.9      |
| current_month_debit            | float64 |      0.01 |     7.63786e+06 |  3658.74     |    91.93 | 51985.4      |
| previous_month_debit           | float64 |      0.01 |     1.41417e+06 |  3339.76     |   109.96 | 24301.1      |
| current_month_balance          | float64 |  -3374.18 |     5.77818e+06 |  7451.13     |  3447.99 | 42033.9      |
| previous_month_balance         | float64 |  -5171.92 |     5.72014e+06 |  7495.18     |  3465.23 | 42432        |
| churn                          | int64   |      0    |     1           |     0.185329 |     0    |     0.388571 | 

Categorical data spread:
 |            | type   |   #unique |   unique% | mode          | firstvalue    |
|:-----------|:-------|----------:|----------:|:--------------|:--------------|
| gender     | object |         2 |      0.01 | Male          | Male          |
| occupation | object |         5 |      0.02 | self_employed | self_employed | 

Datetime data spread:
 |                  | type           | min                 | max                 |
|:-----------------|:---------------|:--------------------|:--------------------|
| last_transaction | datetime64[ns] | 2018-12-31 00:00:00 | 2019-12-31 00:00:00 | 

  
[DataDescription_DTypeConvert.py, 3,50, 18-Jun-2022], desc: The script contains auto data type conversion, the script takes the dataframe and datetime format as arguments, the changes are made into the original dataframe, and don't return any value
