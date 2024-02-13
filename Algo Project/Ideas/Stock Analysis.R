#View Stocks----
stock_view=function(stocks,from,type=NULL,to=NULL){
  if(is.null(type)){type="adjclose"}else{type="volume"}
  if(is.null(to)){to=Sys.Date()}else{to=to}

 lreg = function(x,y,p=1,K=NULL,at=NULL,bw=NULL,plot=TRUE,...){
  # preliminary definitions 
  #-------------------------------------------------------------
  if(is.null(K)) K = dnorm
  n = length(x)
  X = array(1,dim=c(n,p+1))
  if(is.null(at)){ 
    at = seq(min(x),to=max(x),length=301)
  }else{
    at = sort(at)
  }
  if(is.null(bw)) bw = (max(x)-min(x))/sqrt(n)
  n.at = length(at)
  at.all = at
  out = rep(NA,n.at)
  # compute the estimate
  #-------------------------------------------------------------
  for(i.at in 1:n.at){
    at = at.all[i.at]
    if(p>0){
      for(j in 1:p){
        X[,j+1] = (x-at)^j/factorial(j)
      }
    }
    # Method 1: more transparent
    W = diag(K((x-at)/bw))
    XW = t(X)%*%W
    out[i.at] = sum(solve(XW%*%X,XW)[1,]*y)
    # Method 2: faster and easier
    # out[i.at] = lm(y~X-1, weights=K((x-at)/bw))$coef[1]
  }
  # plot the data and regression line
  #-------------------------------------------------------------
  if(plot){
    optional = list(...)
    if(is.null(optional$type)) type="l"
    if(is.null(optional$col)) col="grey"
    if(is.null(optional$lwd)) lwd=3
    if(is.null(optional$lty)) lty=1
    I = order(at.all)
    plot(x,y,type = "l", lwd=2,col="red4", bty="n",...)
    points(at.all[I], out[I], type=type, col=col,lwd=lwd, lty=lty)
    
  }
  # return estimates 
  #-------------------------------------------------------------
  list(at=at.all,fit=out,bw=bw)
 }

 library("pdfetch")
 
 if(length(stocks)>=5){ par(mfrow=c(ceiling(length(stocks)/5),5))} else{par(mfrow=c(1,length(stocks)))}
 
 
 mu_est=c()
 sig_est=c()
 cv_order=c()
mu_order=c()
 for(i in 1:length(stocks)){
 data1 = pdfetch_YAHOO(stocks[i], fields=type,from=from, to=to)
 Stock = as.matrix(data1)
 lreg(seq(1,length(Stock)),Stock,p=1,K=dnorm,at=NULL,bw=NULL,plot=TRUE,main=stocks[i]
      ,xlab="time",ylab="Stock Price")
 grid(lty = "dotted")
 legend("topleft",c(paste("Mean",round(mean(diff(log(data1))[!is.na(diff(log(data1)))]),digit=4))
                    ,paste("Volatility",round(sd(diff(log(data1))[!is.na(diff(log(data1)))]),digit=4))),
        bty="n")
 
 #Return
 mu_est[i]=mean(diff(log(data1))[!is.na(diff(log(data1)))])
 sig_est[i]=sd(diff(log(data1))[!is.na(diff(log(data1)))])
 }
 for(i in 1:length(stocks)){
   cv_order[i]=stocks[which(rank(mu_est/sig_est)==(length(mu_est)+1-i))]
   mu_order[i]=stocks[which(rank(mu_est)==(length(mu_est)+1-i))]
 }
par(mfrow=c(1,1))
 list(CV=cv_order,Return=mu_order)
 
}
#US Treasury----
US_Treasury=function(from=from,to=Sys.Date()){
  library(Quandl)
  output=Quandl("USTREASURY/YIELD", type = "xts",start_date=from, end_date=Sys.Date())
  print(plot(output, main="Treasury Yield Curve Rates"))
  
  check_rate=c()
  year_rate=output[,(5:dim(output)[2])]
  
  for(i in 1:dim(year_rate)[1])
    if(any(as.vector(year_rate[i,])!=sort(as.vector(year_rate[i,])))){check_rate[i]=
      "Inversed"}else{
        check_rate[i]="Normal"
      }
  
  list("Rate"=tail(output), State=check_rate[length(check_rate)])
}
library(Quandl)
CPI=Quandl("RATEINF/CPI_USA", type = "xts",start_date=from, end_date=Sys.Date())
plot(CPI)
#Stocks News----
News_hk=function(stock,from=NULL){
  
  library(httr)
  library(jsonlite)
  library(sentimentr)
  library(anytime)
  
  if(is.null(from)){from="0-1-1"}else{from=from}
  
  url<-"https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"
  
  link=paste(url,"/?rapidapi-key=","791228ed41msh076171c24e18cadp1671e0jsn4955f984a3d9",sep = "")
  
  qq<-GET(url = link,query=list(   category = stock,
                                   region = "HK" ))
  response<-content(qq, as = "text", encoding = "UTF-8")
  output=fromJSON(response, flatten = TRUE)
  output$items$result
  
  title=as.matrix(output$items$result$title)
  title.sen=as.matrix(sentiment(title)[,4])
  
  lookup=array()
  for(i in 1:length(output$items$result$published_at)){
    if(as.numeric(as.POSIXct(from, format="%Y-%m-%d"))<=output$items$result$published_at[i]){lookup[i]=i}
  }
  
  
  if(mean(as.numeric(as.POSIXct(from, format="%Y-%m-%d"))>output$items$result$published_at)==1)
  {
    good=sum(title.sen[1]>0)
    bad=sum(title.sen[1]<0)
    neu=sum(title.sen[1]==0)
    
    array(c(list(title[1]),list(anytime(output$items$result$published_at[1])),mean(title.sen[1])
            ,list(c(good,bad,neu))),dimnames = list(c("News","Date","Mean Sentiment","Good Bad Neutral")))}
  
  else{
    good=sum(title.sen[lookup]>0)
    bad=sum(title.sen[lookup]<0)
    neu=sum(title.sen[lookup]==0)
    array(c(list(title[lookup]),list(anytime(output$items$result$published_at[lookup])),mean(title.sen[lookup])
            ,list(c(good,bad,neu))),dimnames = list(c("News","Date","Mean Sentiment","Good Bad Neutral")))
  }
 }
News_us=function(stock,from=NULL){
  
  library(httr)
  library(jsonlite)
  library(sentimentr)
  library(anytime)
  
  if(is.null(from)){from="0-1-1"}else{from=from}
  
  url<-"https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"
  
  link=paste(url,"/?rapidapi-key=","791228ed41msh076171c24e18cadp1671e0jsn4955f984a3d9",sep = "")
  
  qq<-GET(url = link,query=list(   category = stock,
                                   region = "US" ))
  response<-content(qq, as = "text", encoding = "UTF-8")
  output=fromJSON(response, flatten = TRUE)
  #output$items$result
  
  title=as.matrix(output$items$result$title)
  
  title.sen=array()
  IN=array()
  ID=array()
  for(i in 1:length(title)){
    raw<-unlist(strsplit(title[i]," "))
    p=toupper( gsub("'s","",raw))
    
    for(j in 1:length(Important)){
      if(any(gsub("[][!#$%()*,.:;<=>@^_`|~.{}]", "", p) == toupper(Important[j])) ){  
        title.sen[i]=mean(as.matrix(sentiment(title[i])[,4]))*100000 #Multiplier  #take mean sentiment if multiple sentences
        IN[i]=title[i] 
        ID[i]=output$items$result$published_at[i]} else 
        { title.sen[i]=mean(as.matrix(sentiment(title[i])[,4]))} #take mean sentiment with multiple sentences
    }
  }
  Important_News<-IN[!is.na(IN)]
  Important_Date<-anytime( ID[!is.na(ID)])
  title.sen<-as.matrix(title.sen)
  
  lookup=array()
  for(i in 1:length(output$items$result$published_at)){
    if(as.numeric(as.POSIXct(from, format="%Y-%m-%d"))<=output$items$result$published_at[i]){lookup[i]=i}
  }
  
  
  if(mean(as.numeric(as.POSIXct(from, format="%Y-%m-%d"))>output$items$result$published_at)==1)
  {
    good=sum(title.sen[1]>0)
    bad=sum(title.sen[1]<0)
    neu=sum(title.sen[1]==0)
    
    array(c(list(title[1]),list(anytime(output$items$result$published_at[1])),list(Important_News),list(Important_Date),mean(title.sen[1])
            ,list(c(good,bad,neu))),dimnames = list(c("News","Date","Important News","Important Dates","Mean Sentiment","Good Bad Neutral")))}else{
              good=sum(title.sen[lookup]>0)
              bad=sum(title.sen[lookup]<0)
              neu=sum(title.sen[lookup]==0)
              array(c(list(title[lookup]),list(anytime(output$items$result$published_at[lookup])),list(Important_News),list(Important_Date),mean(title.sen[lookup])
                      ,list(c(good,bad,neu))),dimnames = list(c("News","Date","Important News","Important Dates","Mean Sentiment","Good Bad Neutral")))
            }
}

#Stocks Correlation----
stock_cor=function(stocks,from,to=NULL,method="p"){
  if(is.null(to)){to=Sys.Date()}else{to=to}
  

 library("pdfetch")
 length=length(pdfetch_YAHOO(stocks[1], fields="adjclose",from=from, to=to))
 out=array(dim = c(length,length(stocks)))

 for(j in 1:length(stocks)){
  out[,j] = pdfetch_YAHOO(stocks[j], fields="adjclose",from=from, to=to)
 }
  colnames(out)=stocks
 
    library(TauStar)
    BDcor = function(x, y){
      c12 = tStar(x, y, vStatistic=TRUE)
      c11 = tStar(x, x, vStatistic=TRUE)
      c22 = tStar(y, y, vStatistic=TRUE)
      c12/sqrt(c11*c22)
    }
    BDcorMatrix = function(x){
      x = as.matrix(x)
      d = ncol(x)
      out = array(1, dim=c(d, d))
      for(i in 1:(d-1)){
        for(j in (i+1):d){
          out[i,j] = out[j,i] = BDcor(x[,i], x[,j])
        }
      }
      out
    }
    cor = switch(method,
                 "p"=cor(out),
                 "s"=cor(out, method="s"),
                 "k"=cor(out, method="k"),
                 "bd"=BDcorMatrix(out))
    rownames(cor) = colnames(cor) = colnames(out)
    list(method=method, cor=cor)
  }


#GARCH----
stock_GARCH=function(stocks="3690.hk",from="2020-1-1",to=Sys.Date(),try=c(25,25)){
  library("pdfetch")
  library("rugarch")
  
  data1 = pdfetch_YAHOO(stocks, fields="adjclose",from=from, to=to)
  Stock = as.matrix(data1)
  
  library(tseries)
  
  model_selection=array(dim = c(try[1],try[2]))
  smallest=c()
  for(i in 1:try[1]){
    for(j in 1:try[2])
      model_selection[i,j]=AIC(garch(Stock,c(i,j)))
  }
  for(i in 1:try[1]){
    smallest[i]=which.min(model_selection[i,])
  }
  
  for(i in 1:try[1]){
    best_fit=which.min(model_selection[i,smallest[i]])
  }
  
  fit=garch(Stock,c(best_fit,smallest[best_fit]))
  
  spec = ugarchspec(list(model = "sGARCH", garchOrder = c(best_fit,smallest[best_fit]), 
                         submodel = NULL, external.regressors = NULL, variance.targeting = FALSE))
  fit_ug = ugarchfit(data = Stock, spec = spec)
  forc = ugarchforecast(fit_ug, n.ahead=3)
  
  plot(fit$fitted.values[,1],type="l",col="red4",lwd=2,bty="n",
       main=expression(italic(GARCH)),ylab = expression(italic("Stock Price")),
       xlab = "Time",xlim = c(0,length(fit$fitted.values[,1])+10))
  legend("topright",c("Predicted","True"),lty = 1,lwd=2,col = c("red4","grey"),bty="n")
  lines(Stock,col="grey",lwd=2)
  
  list(Model=fit ,Forecast=forc)
}
#Input----
stocks_HK=c("1799.hk","3800.hk","1810.hk","0788.hk","0293.hk","9988.hk","0700.hk","0763.hk","3690.hk","0981.hk","0813.hk","1098.hk","1211.hk","^HSI")
stocks_US=c("TSLA","AMZN","AAPL","NFLX","DIS","SBUX","^DJI","^GSPC","^IXIC")

from="2020-1-1"  

stock_view(stocks_HK,from)
stock_view(stocks_US,from)
stock_cor(stocks_HK,from,method = "k")  #Correlation k:= Kendall s:=Spearman p:=Pearson bd:=???
stock_cor(stocks_US,from,method = "k")
US_Treasury(from=from,to=Sys.Date())
#stock_GARCH("0005.hk",from="2021-1-1",try=c(1,1))

#News_hk("1810.hk","2020-1-10") #HK stock news ***Traditional Chinese output***

Important<-c("biden","government","policy","federal","china", "elon")

if(run){
  feed<-News_us("TSLA","2021-05-19")} #US stock news
feed$`Important News`;feed$`Important Dates`







