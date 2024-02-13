run=1
EfficientFrontier=function(S1,S2,from.Date,to.Date,Rf){
  if(run==1){
  library("pdfetch")
  stock1 = S1
  from = as.Date(from.Date)
  to = as.Date(to.Date)
  data1 = pdfetch_YAHOO(stock1, fields="adjclose",from=from, to=to)
  stock2 = S2
  data2 = pdfetch_YAHOO(stock2, fields="adjclose",from=from, to=to)
  S1 = as.matrix(data1)
  S2=as.matrix(data2)
  par(mfrow=c(2,1))
  ts.plot(S1);ts.plot(S2)
  R1=diff(log(S1));R2=diff(log(S2))
  
  analyse<-array(c(mean(R1),mean(R2),sqrt(var(R1)),sqrt(var(R2))),dim = c(2,2),dimnames = list(c("S1","S2"),c("Mean","sd")))
  par(mfrow=c(1,1))
  
  w.all=seq(from=0,to=1,length=10000)
  out=array(NA,dim = c(length(w.all),2))
  for (i in 1:length(w.all)) {
    w=w.all[i]
    out[i,1]=sqrt(var(w*R1+(1-w)*R2)) 
    out[i,2]=mean(w*R1+(1-w)*R2)
  }
  colnames(out)=c("Sigma","Mean")
  plot(out[,1],out[,2],col="orange",xlab = expression(sigma),ylab = "Return",main = "Efficient Frontier",cex.main=1.5)
  
  
  legend("bottomright",c(expression(italic(CML)),expression(italic("Efficient Frontier"))),pch = c(15,15),col=c("black","orange"),cex=1.2)
    
  f=array(NA,dim = c(1,1))
  for (i in 1:length(w.all)) {
    if((out[i,2]-Rf)/out[i,1]>=max((out[,2]-Rf)/out[,1])) {f=i}}
  
  mv=array(NA,dim = c(1,1))
  for (i in 1:length(w.all)) {
    if(min(out[i,1])==min(out[,1])) {mv=i}}
  

  lines(seq(from=0,to=range(w.all)[2],length=10),max((out[,2]-Rf)/out[,1])*seq(from=0,to=range(w.all)[2],length=10)+Rf, 
        lwd=5)

array(c(w.all[f], w.all[mv],1-w.all[f],1-w.all[mv],out[f,2],out[mv,2],out[f,1],out[mv,1],cor(S1,S2,method = "k"),
       cor(S1,S2,method = "k")),dim = c(2,5),dimnames=list(c("CML","Minimum Variance"),c('S1',"S2","Mean","Sigma","cor")))

  }}

run=1
GoogleTrend=function(topic,time,alpha){
  if(run==1){
    library(gtrendsR)
    
    
    trend=gtrends(c(topic),geo="HK",time = time)$interest_over_time
    par(mfrow=c(1,1))
    plot(trend[,1],trend[,2],cex=0,ylab = "Hits",xlab = "Date",main = paste(topic,"Trend"),ylim = c(0,100));lines(trend[,1],trend[,2])}
  
   var0 = function(x){ n = length(x)
  var(x)*(n-1)/n }
  rank.stat = function(x,c,s){ R = rank(x)
  n = length(x)
  T = sum(c*s[R])
  muT = n*mean(c)*mean(s)
  varT = n^2/(n-1)*var0(c)*var0(s)
  t = (T-muT)/sqrt(varT)
  list(muT=muT,varT=varT,T=T,t=t)
  }
  n = length(trend[,2])
  c = 1:n
  s = (1:n)/(n+1)
  (t = rank.stat(trend[,2],c,s)$t)
  (pI = 1-pnorm(t));(pD=pnorm(t))
  I=if (pI<alpha){TRUE}else{FALSE}
  D=if (pD<alpha){TRUE}else{FALSE}
  list(c(
    if (I==TRUE & D==FALSE) {"Increasing Trend"} else 
      if (I==FALSE & D==TRUE) {"Decreasing Trend"} else
        if((I==TRUE & D==TRUE) | (I==FALSE & D==FALSE)) {"Not Inceasing nor Decreasing"},
    if(quantile(trend[,2],0.5)<50){"Low Hits"} else {"High Hits"}))}

#Date="2020-11-06" S="0005.hk"
EfficientFrontier("9988.hk","0005.hk","2020-10-06",Sys.Date(),0.001) 

#time= now 7-d, today 1-m
GoogleTrend("ai","now 7-d",0.01)

#News(useless)----

 n=100
 library(newsanchor);library(sentimentr)
 #set_api_key(path ="~/.Renviron") #dbd4572f6fd547ddb9538f681cf3d4e8
 h<-get_headlines(query = "covid-19",page_size = n)$results_df[c("title")]
 out=as.matrix(sentiment(h[1:length(as.matrix(h)),])[,4])
 list(c(mean(out),sum(out)))


 tt<-get_everything("0005.HK",language = "en",page_size = 100,domains = "yahoo.com",sort_by = "publishedAt",from = Sys.Date())
 #tt$results_df["description"]
 tt$results_df["title"]
 title=as.matrix(tt$results_df["title"])
 out.title=as.matrix(sentiment(title)[,4])

 good=sum(out.title>0)
 bad=sum(out.title<0)
 neu=sum(out.title==0)
 array(c(list(tt$results_df["title"]),list(c(good,bad,neu))),dimnames = list(c("News","Good Bad Neutral")))

#Read Sites
library(httr)
library(sentimentr)

site="https://aramariemejorada.wordpress.com/2018/02/26/3-idiots-movie-review-and-character-analysis/"

url<-"https://text-analyzer.p.rapidapi.com/analyze-text/text"
link=paste(url,"/?rapidapi-key=","791228ed41msh076171c24e18cadp1671e0jsn4955f984a3d9",sep = "")

qq<-GET(url = link,query=list(url = site ))
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
output
mean(as.matrix(sentiment(get_sentences(response))[,4]))

url2<-"https://text-analyzer.p.rapidapi.com/analyze-text/ner"
link2=paste(url2,"/?rapidapi-key=","791228ed41msh076171c24e18cadp1671e0jsn4955f984a3d9",sep = "")
qq2<-GET(url = link2,query=list(url = site ))
response<-content(qq2, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
output$Entities


#weather----
weather_hk=function(days=NULL,language=NULL){
  
  if(is.null(days)&is.null(language)){url="https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"}
  else{ if(days==9&language=="tc") {url="https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc"}
    if(days==9&language=="en") {url="https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"}
    if(days==1&language=="tc") {url="https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc"}
    if(days==1&language=="en") {url="https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"}
    }
  
  library(httr);library(jsonlite)
 qq<-GET(url = url)
 response=content(qq, as = "text", encoding = "UTF-8")
 output=fromJSON(response, flatten = TRUE)
 output
 }
#weather_hk(9,"en")
weather_hk(9,"tc")
weather_hk(1,"tc")
#bus----
route="E22"
#----
library(httr);library(jsonlite)
url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route/ctb"
link=paste(url,sep = "")
qq<-GET(url = link)
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
route_ctb=output$data$route
#route_ctb
url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route/nwfb"
link=paste(url,sep = "")
qq<-GET(url = link)
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
route_nwfb=output$data$route
#route_nwfb
if(sum(route==route_ctb)==1){

url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/CTB/"
direction=c("inbound","outbound")
link=paste(url,route,"/",direction[1],sep = "")

qq<-GET(url = link)
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
stop=output$data$stop

response=array()
output=array()
showI=array()
for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/CTB/"
link=paste(url,stop[i],"/",route,sep = "")

qq<-GET(url = link)
response[i]<-content(qq, as = "text", encoding = "UTF-8")
output[i]=list(fromJSON(response[i], flatten = TRUE))

#inbound=output$data[which(output$data$dir=="I"),][c("dest_en","eta")]
#outbound=output$data[which(output$data$dir=="O"),][c("dest_en","eta")]

showI[i]=list(output[[i]]$data[c("dest_en","eta")])
}

stop_name=array()
response=array()
output=array()

for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/"
  link=paste(url,stop[i],sep = "")
  
  qq<-GET(url = link)
  response[i]<-content(qq, as = "text", encoding = "UTF-8")
  output[i]=list(fromJSON(response[i], flatten = TRUE))

  stop_name[i]=output[[i]]$data$name_en
}

names(showI)=stop_name

url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/CTB/"
direction=c("inbound","outbound")
link=paste(url,route,"/",direction[2],sep = "")

qq<-GET(url = link)
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
stop=output$data$stop

response=array()
output=array()
showO=array()
for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/CTB/"
  link=paste(url,stop[i],"/",route,sep = "")
  
  qq<-GET(url = link)
  response[i]<-content(qq, as = "text", encoding = "UTF-8")
  output[i]=list(fromJSON(response[i], flatten = TRUE))
  
  #inbound=output$data[which(output$data$dir=="I"),][c("dest_en","eta")]
  #outbound=output$data[which(output$data$dir=="O"),][c("dest_en","eta")]
  
  showO[i]=list(output[[i]]$data[c("dest_en","eta")])
}

stop_name=array()
response=array()
output=array()

for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/"
  link=paste(url,stop[i],sep = "")
  
  qq<-GET(url = link)
  response[i]<-content(qq, as = "text", encoding = "UTF-8")
  output[i]=list(fromJSON(response[i], flatten = TRUE))
  
  stop_name[i]=output[[i]]$data$name_en
}

names(showO)=stop_name

bus=array(list(c(showI),showO),dimnames = list(c(paste("To ",names(showI[length(showI)]),sep = ""),paste("To ",names(showO[length(showO)]),sep = ""))))
}else 
  {url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/NWFB/"
direction=c("inbound","outbound")
link=paste(url,route,"/",direction[1],sep = "")

qq<-GET(url = link)
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
stop=output$data$stop

response=array()
output=array()
showI=array()
for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/NWFB/"
  link=paste(url,stop[i],"/",route,sep = "")
  
  qq<-GET(url = link)
  response[i]<-content(qq, as = "text", encoding = "UTF-8")
  output[i]=list(fromJSON(response[i], flatten = TRUE))
  
  #inbound=output$data[which(output$data$dir=="I"),][c("dest_en","eta")]
  #outbound=output$data[which(output$data$dir=="O"),][c("dest_en","eta")]
  
  showI[i]=list(output[[i]]$data[c("dest_en","eta")])
}

stop_name=array()
response=array()
output=array()

for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/"
  link=paste(url,stop[i],sep = "")
  
  qq<-GET(url = link)
  response[i]<-content(qq, as = "text", encoding = "UTF-8")
  output[i]=list(fromJSON(response[i], flatten = TRUE))
  
  stop_name[i]=output[[i]]$data$name_en
}

names(showI)=stop_name

url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/NWFB/"
direction=c("inbound","outbound")
link=paste(url,route,"/",direction[2],sep = "")

qq<-GET(url = link)
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
stop=output$data$stop

response=array()
output=array()
showO=array()
for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/NWFB/"
  link=paste(url,stop[i],"/",route,sep = "")
  
  qq<-GET(url = link)
  response[i]<-content(qq, as = "text", encoding = "UTF-8")
  output[i]=list(fromJSON(response[i], flatten = TRUE))
  
  #inbound=output$data[which(output$data$dir=="I"),][c("dest_en","eta")]
  #outbound=output$data[which(output$data$dir=="O"),][c("dest_en","eta")]
  
  showO[i]=list(output[[i]]$data[c("dest_en","eta")])
}

stop_name=array()
response=array()
output=array()

for(i in 1:length(stop)){
  url<-"https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/"
  link=paste(url,stop[i],sep = "")
  
  qq<-GET(url = link)
  response[i]<-content(qq, as = "text", encoding = "UTF-8")
  output[i]=list(fromJSON(response[i], flatten = TRUE))
  
  stop_name[i]=output[[i]]$data$name_en
}

names(showO)=stop_name

bus=array(list(c(showI),showO),dimnames = list(c(paste("To ",names(showI[length(showI)]),sep = ""),paste("To ",names(showO[length(showO)]),sep = ""))))
}
bus

