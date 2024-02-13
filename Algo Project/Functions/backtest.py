def backtest( initial, Open, Close, prediction , tran_cost = 0 ):   
                         
    signal = []
    position = []
    cash = [] 
    balance = []
    action = []
    profit_n_loss = []
    n_trade = 0

    for i in range( len( prediction) ):          

        if (prediction[i] == 1):
            signal = signal + ['Buy']

        if (prediction[i] == 0):
            signal = signal + ['Sell']

        if (prediction[i] == 2):
            signal = signal + ['Hold']

    for i in range(len( prediction ) ) :     # cannot test the last day, cus we need to trade at the second day Open

        if (i == 0):
            cash = [initial]
            position = [0]
            action = ['Hold']

        if (i >= 1):
            position = position  + [position[i-1]]
            cash     = cash + [cash[i-1]]
            action   = action + ['Hold']

            if (signal[i-1] == 'Buy'):                
                if (position[i-1] == 0):               # yesterday position
                    n_trade = n_trade + 1
                    position[i] = 1
                    action[i] = 'Buy'
                    cash[i] = cash[i-1] - ( 1 + tran_cost ) * Open[i] #  today open

            if (signal[i-1] == 'Sell'):
                if (position[i-1] == 1):
                    n_trade = n_trade + 1
                    position[i] = 0
                    action[i] = 'Sell'
                    cash[i] = cash[i-1] + ( 1 - tran_cost ) * Open[i] 

    for i in range(len( prediction )) :

        if (position[i] == 1):
            balance = balance + [ Close[i] + cash[i] ] 

        if (position[i] == 0):
            balance = balance + [ cash[i] ] 

    for i in range(len( prediction )) :
        if (i == 0):
            profit_n_loss = profit_n_loss + [0]

        if (i >= 1):
            profit_n_loss = profit_n_loss + [balance[i] - balance[i-1]]

    backtest = pd.DataFrame()
    backtest['Open'] = Open
    backtest['Close'] = Close
    backtest['pred'] = prediction
    backtest['signal'] = signal           
    backtest['position'] = position
    backtest['action'] = action
    backtest['cash'] = cash
    backtest['balance'] = balance
    backtest['profit_n_loss'] = profit_n_loss
  
    sharpe_ratio = pd.DataFrame(profit_n_loss).mean() / pd.DataFrame(profit_n_loss).std()
    
    annualised_return_model = ( balance[-1] / Open[0] )**(252/len( prediction ))
    annualised_return_asset = ( Open[-1] / Open[0] )**(252/len( prediction ))
    return_model = ( balance[-1] / Open[0] )
    return_asset = ( Open[-1] / Open[0] )
    
    print( 'no. of trade :', n_trade)
    print( 'sharpe_ratio (daily) :', sharpe_ratio.values[0] )   
#    print( 'max. drawdown(daily) :' , pd.DataFrame(profit_n_loss).min().values[0])
#    print( 'volatility (Balance) :' , pd.DataFrame(balance).std().values[0]) 
#    print( 'volatility (Underlying) :' , pd.DataFrame(Open).std().values[0]) 
    print('')
    print( 'Annualised Return (model) :' , annualised_return_model)
    print( 'Annualised Return (Underlying) :' , annualised_return_asset)
#     print( 'Return (model) :' , return_model)
#     print( 'Return (Underlying) :' , return_btc)
    
    return( backtest)