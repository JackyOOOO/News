import numpy as np
import pandas as pd
def picky(data, typ=np.nan, num=np.nan, criteria=np.nan, num_type = np.nan, order=np.nan, index=False):
    #if pd.isna(num)==False:
    import numpy as np
    import pandas as pd
    if type(data)==type([]):
        D = np.array(data)
    elif (type(data)==type(pd.DataFrame())) or (type(data)==type(pd.DataFrame(['g']).iloc[:,0])):
        D = data.to_numpy()
        
    else:
        D = data
        
    if pd.isna(criteria) == False:
        if criteria == 'pos':
            D = D.copy()[D>0]
        if criteria == 'neg':
            D = D.copy()[D<0]           
            
    if pd.isna(typ) ==False:    
        if typ=='g':
            D = D.copy()[np.where(D>num)[0]]

        elif typ=='e':
            D = D.copy()[np.where(D=num)[0]]

        elif typ=='ge':
            D = D.copy()[np.where(D>=num)[0]]

        elif typ=='s':
            D = D.copy()[np.where(D<num)[0]]

        elif typ=='se':
            D = D.copy()[np.where(D<=num)[0]]
        
    loc=[]
    for i in range(len(D)):
        loc.append(float(D[i]).is_integer())
    if num_type == 'integer':
        D=D.copy()[loc]    
    elif num_type == 'decimal':
        D=D.copy()[np.array(loc)==False]
        
    if order=='a':
        D=list(D.copy())
        D.sort(reverse=False)
        D=np.array(D.copy()) 
            
    if order=='d':
        D=list(D.copy())
        D.sort(reverse=True)
        D=np.array(D.copy())
    
    if index:
        DD = D[~np.isnan(D)]
        index = data.index
        
        ordered = []
        for i in range(len(DD)):
            ordered.append(np.where(data==DD[i])[0][0])

        ticker_ordered = []
        for i in range(len(ordered)-1):
            ticker_ordered.append(index[ordered[i]])
        D=ticker_ordered
    return(D)  


