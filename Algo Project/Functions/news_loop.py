import urllib.request
import re
import string
from time import strptime
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import requests
import numpy as np

key_list = ["361641b2f2msh6a1b4170174acf0p13d27djsnde179ff3425e",
        "791228ed41msh076171c24e18cadp1671e0jsn4955f984a3d9",
        'bb8aae838bmsh9cb690e56d7ebccp1912e2jsnd4b483a2bb10',
        "922444c625msha88428c1ec962d8p152a98jsnfa36f2c612cf",
        "c55bd52aaemshf6e2a17f87b9d3cp1ac760jsn4f2ef3d7b794",
        "70bb92444dmshe58b851a37c079cp14b8a8jsn4f9233b1c2dc",
        "451de061fbmsh0afa863a647a725p17fae7jsnaef51ecf97b6",
        'fab70f7b83msh65d5eb52a12aa69p146f11jsn06992e5c075d',
        'a663bcf142msh49b2b20c895b9ecp16e75cjsnb1dd5014a02e']



def loop(sector_list, function):
    o = {}
    p = pd.DataFrame(data = o) 
    for i in range(len(sector_list)):
        print(int((i /len(sector_list))*100),'%')
        y = function(sector_list[i])        
        p = pd.concat([p, y], axis=1) 
    return(p)


def get_summary(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"
    querystring = {"category": ticker ,"region":"US"}

    api = iter(key_list)

    while True:
        try:
            api_use = next(api)
            headers = {
                'x-rapidapi-key': api_use,
                'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            raw_data = response.json() 

            for i in range(len(raw_data['items']['result'])):
                data1 = re.sub('</p> \n<p>', '', raw_data['items']['result'][i]['summary'])
                data2 = re.sub('</p>', '', data1)
                data3 = re.sub('<p>', '', data2)
                raw_data['items']['result'][i]['summary'] = data3
            break
            
        except Exception: #KeyError 
            print(api_use, 'gged')
            # print(len(key_list)-api)


    summary2 = [None]*len(raw_data['items']['result'])
    for i in range(len(raw_data['items']['result'])) :
        summary2[i] = pd.concat( [pd.DataFrame ( [raw_data['items']['result'][i]['summary'] ] )])
    summary = pd.DataFrame(np.reshape(summary2, -1) )

    title2 = [None]*len(raw_data['items']['result'])
    for i in range(len(raw_data['items']['result'])) :
        title2[i] = pd.concat( [pd.DataFrame ( [raw_data['items']['result'][i]['title'] ] )])
    title = pd.DataFrame(np.reshape(title2, -1) )

    content2 = [None]*len(raw_data['items']['result'])
    for i in range(len(raw_data['items']['result'])) :
        content2[i] = pd.concat( [pd.DataFrame ( [raw_data['items']['result'][i]['content'] ] )])
    content = pd.DataFrame(np.reshape(content2, -1) )


    time2 = [None]*len(raw_data['items']['result'])
    for i in range(len(raw_data['items']['result'])) :
        time2[i] = pd.concat( [pd.DataFrame ( [raw_data['items']['result'][i]['published_at'] ] )])
    time = pd.DataFrame(np.reshape(time2, -1) )

    DataTime = [None]*len(time)
    for i in range(len(time)):
            DataTime[i] = datetime.fromtimestamp(time.iloc[i,0])
    Time = pd.Series(DataTime, name = 'Time')


    news_data = pd.concat([Time], axis=1)    
    news_data['Title'] = title
    news_data['Summary'] = summary
    news_data['Content'] = content

    a = news_data
    Date = [None] * len(a['Time'])
    for i in range(len(a['Time'])):
        Date[i] = pd.Timestamp( a['Time'][i]).strftime('%Y-%m-%d')
    a.insert(0, 'Date', Date)
    a = a.drop(columns= 'Time')
    a = a.groupby('Date').sum()
    a.index = pd.to_datetime(a.index.values.astype('datetime64[D]'))

    d = yf.download( ticker , interval = "1d", period = "1mo")
    d.insert(6, ticker +'_Title', a['Title'])
    d.insert(7, ticker +'_Summary', a['Summary'])

    for i in range(len(d)-1):
        if (d['Close'].values[i] != d['Close'].values[i]) :
            if (d['Volume'].values[i] != d['Volume'].values[i]) :
                if (d[ticker +'_Title'][i + 1] == d[ticker +'_Title'][i + 1]) :
                    d.copy(deep=False)[ ticker +'_Title'][i + 1] += ','+ d[ ticker +'_Title'][i]
                    d.copy(deep=False)[ ticker +'_Title'][i] = ""
                    d.copy(deep=False)[ ticker +'_Summary'][i + 1] += ','+ d[ ticker +'_Summary'][i]
                    d.copy(deep=False)[ ticker +'_Summary'][i] = ""
                else:
                    d.copy(deep=False)[ ticker +'_Title'][i + 1] = d[ ticker +'_Title'][i]
                    d.copy(deep=False)[ ticker +'_Title'][i] = ""

                    d.copy(deep=False)[ ticker +'_Summary'][i + 1] = d[ ticker +'_Summary'][i]
                    d.copy(deep=False)[ ticker +'_Summary'][i] = ""


    d = d.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume', ticker +'_Title'])

    return(d)

