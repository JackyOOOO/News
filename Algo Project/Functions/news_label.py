

def label( dataset, m = 5, r = 5, p = 0.03, dataframe = False, cumulative = False, set_index =True):
    import numpy as np
    import pandas as pd
    import math
    if (set_index == True):
        dataset = dataset.set_index('Date')

    col_list = dataset.columns.tolist()
    nstock = dataset.shape[1] / 2
    o = {}
    df = pd.DataFrame(data = o) 
    cumulative_news = pd.DataFrame(data = o) 
    nl= pd.DataFrame(data = o) 
    NewsLabel= pd.DataFrame(data = o) 
    SummaryLabel = pd.DataFrame(data = o) 

    for c in range( 1, int(nstock + 1) ):

        yy = dataset.iloc[0: ,  (2*(c-1)) : (2*c)  ]   #close and news 
        y  = dataset.iloc[0: ,  (2*(c-1)) : (2*c-1)]   # close

        y_list = []
        for i in range(len(y)-m):
            y_value=np.array([y[i:i+m]])
            y_list.append(y_value)

        label=[]
        for b in range(len(y) - m):
            for j in range(m):
                value=[]
                value.append(( (y_list[b].reshape(m,1)[j]) - (y_list[b].reshape(m,1)[0]) ) / (y_list[b].reshape(m,1)[0]) )


            down_loc=np.where(np.array(value)<- p)[0]
            if (len(down_loc) >= 1):
                down_loc = down_loc.reshape(len(down_loc),1)[0]

            up_loc=np.where(np.array(value)> p )[0]
            if (len(up_loc) >= 1):
                up_loc = up_loc.reshape(len(up_loc),1)[0]

            if (len(down_loc) >= 1) & (len(up_loc) == 0):
                label.append(-1)

            if (len(down_loc) == 0) & (len(up_loc) >= 1):
                label.append(1)

            if (len(down_loc) >= 1) & (len(up_loc) >= 1):
                if down_loc[0]>up_loc[0]:
                    label.append(1)
                if down_loc[0]<up_loc[0]:
                    label.append(-1)

            if (len(up_loc) ==0) & (len(down_loc) ==0):
                label.append(0)

        label = np.append(label, np.repeat(np.nan, m))

        n = yy.drop( columns = col_list[ (2*(c-1)) : (2*c-1)] )  
        N = n.set_axis(['news'], axis='columns').reset_index(drop=True)

        L = pd.DataFrame(label ,columns=['label']).reset_index(drop=True)

        NL = pd.concat([N, L], axis=1)
        nl = pd.concat([nl, NL ], axis=1)


        yy.insert(2, 'label',label , True)
        df = pd.concat([df, yy], axis=1)   # output of close, news, label dataset

        dd = yy.copy()
        for i in range( len(yy)-1 , (r-1), -1) : 
                if (yy.iloc[:,1].values[i] == yy.iloc[:,1].values[i]) :
                    past_news = ''
                    for s in range( 1, (r-1) ):
                        if ( dd.iloc[:,1].values[i-s] == yy.iloc[:,1].values[i-s] ) :
                            past_news = yy.iloc[:,1].values[i-s] + past_news
                    dd.iloc[:,1].values[i] =  past_news + yy.iloc[:,1].values[i]
        dd = dd[dd.iloc[:,1].values == dd.iloc[:,1].values]

        cumulative_news = pd.concat([cumulative_news, dd], axis=1)

        Label = nl['label'].to_numpy().flatten()
        News = nl['news'].to_numpy().flatten()
        NewsLabel = pd.concat([pd.DataFrame(News ,columns=['news']), pd.DataFrame(Label ,columns=['label']) ], axis=1)

    r = range(1, int((nstock)*3 + 1) , 3)
    summary = cumulative_news.iloc[:,r].to_numpy().flatten()
    SummaryLabel = pd.concat([pd.DataFrame( summary ,columns=['news']), pd.DataFrame(Label ,columns=['label']) ], axis=1)

    if (dataframe == True) & ( cumulative == False): 
        return(df)
    if (dataframe == True) & ( cumulative == True): 
        return( cumulative_news )
    if (dataframe == False) & ( cumulative == False): 
        return( NewsLabel)
    if (dataframe == False) & ( cumulative == True): 
        return( SummaryLabel )

