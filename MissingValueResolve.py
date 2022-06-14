# Resolving Missing Value using Mean, Median, Mode and Userdefined Value

def MissingValueResolve(data, collist, replacelist):
    missdf=pd.DataFrame(columns=["#NAs","replacedby","prefill","postfill"], 
                        index=collist)
    for col, rep in zip(collist, replacelist):
        missdf.loc[col,"#NAs"] = data[col].isnull().sum()
        missdf.loc[col,"replacedby"] = rep
        if rep=="mean":
            missdf.loc[col,"prefill"] = data[col].mean()
            data[col].fillna(data[col].mean(), inplace=True)
            missdf.loc[col,"postfill"] = data[col].mean()
        elif rep=="median":
            missdf.loc[col,"prefill"] = data[col].median()
            data[col].fillna(data[col].median(), inplace=True)
            missdf.loc[col,"postfill"] = data[col].median()
        elif rep=="mode":
            missdf.loc[col,"prefill"] = data[col].mode()[0]
            data[col].fillna(data[col].mode()[0], inplace=True)
            missdf.loc[col,"postfill"] = data[col].mode()[0]
        else:
            missdf.loc[col,"prefill"] = rep
            data[col].fillna(rep, inplace=True)
            missdf.loc[col,"postfill"] = rep
    return missdf
