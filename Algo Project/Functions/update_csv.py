file_directory = 0
def ytd_csv(day_before, dataset):
    import time
    from time import strptime
    import pandas as pd
    from datetime import datetime, timedelta
    tim = time.time()
    time = time.localtime(tim)
    date = pd.Timestamp(year = time.tm_year, month = time.tm_mon , day = time.tm_mday)

    tmp = dataset 
    length = len(tmp)
    flag = 0
    result = pd.DataFrame()
    for i in range(length-1,-1,-1):
        if (tmp.iloc[i].name == pd.Timestamp((date.to_pydatetime() - timedelta(hours = day_before*24)).strftime('%Y-%m-%d'))): #and (not (pd.isna(tmp.iloc[i][tmp]))):
            return tmp.iloc[i]

    return result #ytd's stock & news

################################################
################################################
################################################
def append_to_csv():

    day = txt_days(txt_file)
    tmp = pd.DataFrame(columns = txt_file.columns)  
    result2 = pd.DataFrame(columns = None)

    if (day > 0):
        for i in range(day-1,0,-1):
            result2 = ytd_csv(i)
            print(result2)
            if (not result2.empty):
                result2['Date'] = result2.name
                print(result2)
                tmp = tmp.copy().append(result2 , sort = False)
                print(tmp)
    if (not tmp.empty):
        tmp = tmp.drop(columns=['Date'])
        tmp.to_csv(file_directory+'/'+Industry+'_summary_dataset.txt', sep=';', mode='a', header= False)

    return tmp


################################################
################################################

from datetime import date
import datetime
import time

def txt_days(txt_file):

    previous_time = time.mktime(datetime.datetime.strptime(txt_file.iloc[len(txt_file)-1,0], "%Y-%m-%d").timetuple())


    current_time = time.mktime(datetime.datetime.strptime(str(date.today()), "%Y-%m-%d").timetuple())

    days_to_update = (current_time - previous_time)/(24*60*60)

    return(int(days_to_update))

# append_to_csv()

def update_dataset(original_dataset, new_dataset, Industry):
    import numpy as np
    import pandas as pd
    close_position = np.where(new_dataset.copy().columns.duplicated())
    no_of_stocks = len(new_dataset.columns)/2

    assign = np.arange(no_of_stocks,step=1, dtype = int)+1
    for i in range(len(assign)):
        assign[i] = int(assign[i])

    for i in range(len(close_position[0])):
        string = str(assign[i])   
        new_dataset.columns.values[close_position[0][i]] = "Close" + "." + string
        
    day = txt_days(original_dataset)
    tmp = pd.DataFrame(columns = original_dataset.columns) 
    result2 = pd.DataFrame(columns = None)

    if (day > 0):
        for i in range(day-1,0,-1):
            result2 = ytd_csv(i,dataset=new_dataset)               
            print(result2)
            if (not result2.empty):
                result2['Date'] = result2.name
                print(result2)
                tmp = tmp.copy().append(result2 , sort = False)
                print(tmp)
    if (not tmp.empty):
        tmp = tmp.drop(columns=['Date'])
        tmp.to_csv(file_directory+'/News_Datasets/'+Industry+'_summary_dataset.txt', sep=';', mode='a', header= False)
    print(tmp)
    pass









