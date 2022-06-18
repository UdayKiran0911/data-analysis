# function for data description

def datadescribe(data):
    # shape of the dataframe
    print("Shape: Rows = {}, Columns = {}\n".format(data.shape[0], data.shape[1]))
    
    # getting dtypes as count
    print("Dtype:\n", pd.Series(data.dtypes.values).value_counts().to_markdown(),"\n")
    
    # missing value information
    nadf = pd.DataFrame(index=data.columns[data.isnull().any()],columns=["#NA","in%"])
    for idx in data.columns[data.isnull().any()]:
        nadf.loc[idx, "#NA"] = data[idx].isnull().sum()
        nadf.loc[idx, "in%"] = round((data[idx].isnull().sum()/data.shape[0])*100,2)
    print("Missing Value info:\n",nadf.sort_values("#NA", ascending=False).to_markdown(),"\n")
    
    # Data spread
    # Numeric Data
    numcol = data.select_dtypes(include=('int','int64','int32','int16','float','float64','float32','float16')).columns
    if len(numcol)>0:
        Numspread = pd.DataFrame(columns=["type","min","max","mean","median","stddev"], index=numcol)
        for idx in numcol:
            Numspread.loc[idx, "type"] = data[idx].dtype
            Numspread.loc[idx, "min"] = data[idx].min()
            Numspread.loc[idx, "max"] = data[idx].max()
            Numspread.loc[idx, "mean"] = data[idx].mean()
            Numspread.loc[idx, "median"] = data[idx].median()
            Numspread.loc[idx, "stddev"] = data[idx].std()
        print("Integer data spread:\n",Numspread.to_markdown(),"\n")
    
    # categorical data
    objcol = data.select_dtypes(include=('object')).columns
    if len(objcol)>0:
        objspread = pd.DataFrame(columns=["type","#unique","unique%","mode","firstvalue"], index=objcol)
        for idx in objcol:
            objspread.loc[idx, "type"] = data[idx].dtype
            objspread.loc[idx, "#unique"] = data[idx].nunique()
            objspread.loc[idx, "unique%"] = round((data[idx].nunique()/data.shape[0])*100,2)
            objspread.loc[idx, "mode"] = data[idx].mode()[0]
            objspread.loc[idx, "firstvalue"] = data[idx].dropna().head(1).to_list()[0]
        print("Categorical data spread:\n",objspread.to_markdown(),"\n")
    # Datetime data
    dtcol = data.select_dtypes(include=('datetime64')).columns
    if len(dtcol)>0:
        dtspread = pd.DataFrame(columns=["type","min","max"], index=dtcol)
        for idx in dtcol:
            dtspread.loc[idx, "type"] = data[idx].dtype
            dtspread.loc[idx, "min"] = data[idx].min()
            dtspread.loc[idx, "max"] = data[idx].max()
        print("Datetime data spread:\n",dtspread.to_markdown(),"\n")
        

# function to convert data types

def cat_type_convert(data, fmt):
    for col in data2.select_dtypes(include=('object')).columns:
        try:
            data2[col] = pd.to_datetime(data2[col], format=fmt)       
        except:
            try:
                 data2[col]=data2[col].astype("float")           
            except:
                pass
