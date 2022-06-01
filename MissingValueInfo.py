# Missing Value Information

def MissingValueInfo(data):
    missdf=pd.DataFrame(columns=["dtype","#NAs","NA_pcnt", "head"], index=data.columns[data.isnull().any()])
    totalnas = data.isnull().sum().sum() 
    for i in missdf.index:
        missdf.loc[i,"dtype"] = data[i].dtype
        missdf.loc[i,"#NAs"] = data[i].isnull().sum()
        missdf.loc[i,"NA_pcnt"] = round((data[i].isnull().sum()/totalnas)*100, 2)
        missdf.loc[i,"head"] = [data[i][0:5]]
    return missdf
