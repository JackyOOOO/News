import json
import requests
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import timeit

start= timeit.default_timer()
class MLP_stock:
    def build_model(self):
        model=tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(64,activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(64,activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(64,activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(64,activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(1,activation=tf.nn.relu))
        optimizer=tf.keras.optimizers.Adam(lr=0.01)
        model.compile(optimizer=optimizer,loss="mse")
        return(model)


    def train(self,X_train,y_train,bs=32,ntry=1):
        model=self.build_model()
        model.fit(X_train,y_train,batch_size=bs,epochs=30,shuffle=True)

        self.best_model=model
        best_loss=model.evaluate(X_train[-50:] ,y_train[-50:])

        for i in range(ntry):
            model=self.build_model()
            model.fit(X_train,y_train,batch_size=bs,epochs=100,shuffle=True)
            if model.evaluate(X_train, y_train) < best_loss:
                self.best_model=model
                best_loss=model.evaluate(X_train[-50:] ,y_train[-50:] )


    def predict(self,X_test):
        return(self.best_model.predict(X_test))


def generate_dataset(price, seq_len):
    X_list, y_list=[],[]
    for i in range(len(price)-seq_len):
        X=np.array(price[i:i+seq_len])
        y=np.array([price[i+seq_len]])
        X_list.append(X)
        y_list.append(y)
    return np.array(X_list), np.array(y_list)

#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo

api_token = 'XXPVD1K7F4AJ8F1E'
ticker= 'TSLA'
api_url_base = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
api_url = api_url_base + ticker+ '&interval=5min&outputsize=full&apikey=' +api_token
response = requests.get(api_url)
out= json.loads(response.content.decode('utf-8'))

close= pd.DataFrame.from_dict(out['Time Series (5min)']).iloc[3,]

close_data=[]
for i in range(len(close)):
    close_data.append(float(close[len(close)-1- i]))
    
train_len=int(np.round(len(close_data)*0.8))#900 #0.8 0.2 split set

stock_train=close_data[:train_len]
stock_train=np.squeeze(stock_train)

stock_test=close_data[train_len:]
stock_test=np.squeeze(stock_test)

minutes=4 ######
X_train,y_train=generate_dataset(stock_train,minutes)
X_test,y_test=generate_dataset(stock_test,minutes)

MLP=MLP_stock()
bs=32 #####
ntry=1 ####
MLP.train(X_train,y_train,bs=bs,ntry=ntry)
y_pred=np.squeeze(MLP.predict(X_test))
data=close_data[-minutes:]
data=np.squeeze(data)

stop = timeit.default_timer()

print("Previous",y_test[len(y_test)-1])
print("Previous Predicted",y_pred[len(y_pred)-1])
print("Predicted",MLP.predict(np.array(data).reshape(int(len(data)/minutes),minutes)))
#print("Predicted",MLP.predict(np.array(data).reshape(int(len(data)/minutes),minutes))-(y_pred[len(y_pred)-1]-y_test[len(y_test)-1]))
print('Time:', (stop-start)/60, 'minutes')

test_len=len(X_test)
plt.plot(range(test_len),y_test,label="true")
plt.plot(range(test_len),y_pred,label="predict")
plt.ylabel("price",fontsize=15)
plt.xlabel("trading minutes",fontsize=15)
plt.legend(loc="lower right",fontsize=10)
plt.title(f"""{ticker} prediction""",fontsize=25)
plt.show()

