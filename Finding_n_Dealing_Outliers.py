# Finding int/float columns with outliers

def OutliersInfo(data):
    int_float_cols = data.select_dtypes(include=("int64","float64")).columns
    outliedf=pd.DataFrame(columns=["[min, max]", "median","[25, 75qnt]","IQR",
                                   "[l, uwisk]","#oliers_ls_lw","#oliers_gr_uw"], 
                        index=int_float_cols)
    for col in outliedf.index:
        outliedf.loc[col,"[min, max]"] = [data[col].min(), data[col].max()]
        outliedf.loc[col,"median"] = round(data[col].median(),2)
        quant25 = data[col].quantile(.25)
        quant75 = data[col].quantile(.75)
        IQR = quant75 - quant25
        outliedf.loc[col,"[25, 75qnt]"] = [quant25, quant75]
        outliedf.loc[col,"IQR"] = IQR
        outliedf.loc[col,"[l, uwisk]"] = [round(data[col].median() - (1.5*IQR),2), round(data[col].median() + (1.5*IQR),2)]
        outliedf.loc[col,"#oliers_ls_lw"] = len(data[col][data[col]>(data[col].median() - (1.5*IQR))])
        outliedf.loc[col,"#oliers_gr_uw"] = len(data[col][data[col]>(data[col].median() + (1.5*IQR))])
    
    return outliedf
  
  def OutliersVisual(data, collist, include_outlier):
    size = len(collist)
    plt.figure(figsize=(7*size, 2), dpi=100)
    if include_outlier:               
        for i, col in enumerate(collist):
            plt.subplot(1, size, i+1)            
            med =  data[col].median()
            sns.boxplot(x=data[col])
            plt.xlabel('{}'.format(col), fontsize=12)
            plt.title('Median = {}'.format(round(med,2)))
    else:              
        for i, col in enumerate(collist):
            plt.subplot(1, size, i+1)
            med =  data[col].median()         
            IQR = data[col].quantile(.75) - data[col].quantile(.25)
            lwisk = data[col].median() - (1.5*IQR)
            uwisk = data[col].median() + (1.5*IQR)
            data[col][data[col]<lwisk] = lwisk - 1            
            data[col][data[col]>uwisk] = uwisk + 1
            sns.boxplot(x=data[col])
            plt.xlabel('{}'.format(col), fontsize=12)
            plt.title('IQR = {}; Median = {} \n2nd, 3rd Quartiles = {}; \nOutliers (low/high) = {}'.format(round(IQR,2),
                                                                                                        round(med,2),
                                                                                                        (round(data[col].quantile(.25),2),
                                                                                                         round(data[col].quantile(.75),2)),
                                                                                                        (round(lwisk,2),round(uwisk,2))))
