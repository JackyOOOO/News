
def stock_mlp(ticker,start_date= "2016-1-1",days=3,bs=32,ntry=10):

	import numpy as np
	import pandas as pd
	import tensorflow as tf
	import matplotlib.pyplot as plt
	# from pandas_datareader import data as pdr
	from datetime import date
	import yfinance as yf

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

	        #model.save_weights("~/Desktop")
	    
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


	#for stock in STOCKS:
	ticker_list=[ticker]
	today = date.today()
	#start_date= "2016-1-1"

	#df=pdr.get_data_yahoo(ticker_list, start=start_date, end=today)#pd.read_csv("~/Desktop/STAT4012/STAT4012 Datasets/0005.HK.csv")
	df = yf.download(ticker_list,istart=start_date, end=today)
	train_len=int(np.round(len(df["Adj Close"])*0.8))#900 #0.8 0.2 split set

	stock_train=df["Adj Close"].iloc[:train_len].values
	stock_train=np.squeeze(stock_train)

	stock_test=df["Adj Close"].iloc[train_len:].values
	stock_test=np.squeeze(stock_test)

	#days=3
	X_train,y_train=generate_dataset(stock_train,days)
	X_test,y_test=generate_dataset(stock_test,days)

	MLP=MLP_stock()
	MLP.train(X_train,y_train,bs=bs,ntry=ntry)
	y_pred=np.squeeze(MLP.predict(X_test))


	data=df["Adj Close"].iloc[-days:].values
	data=np.squeeze(data)
	

	print("Previous",y_test[len(y_test)-1])
	print("Previous Predicted",y_pred[len(y_pred)-1])
	print("Predicted",MLP.predict(np.array(data).reshape(int(len(data)/days),days)))

	test_len=len(X_test)
	plt.plot(range(test_len),y_test,label="true")
	plt.plot(range(test_len),y_pred,label="predict")
	plt.ylabel("price",fontsize=15)
	plt.xlabel("trading days",fontsize=15)
	plt.legend(loc="lower right",fontsize=10)
	plt.title(f"""{ticker} prediction""",fontsize=25)
	plt.show()



