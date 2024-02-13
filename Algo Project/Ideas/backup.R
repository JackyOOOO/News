Important<-c("biden","united states","government","china","policy")

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
  for(i in 1:length(title)){
    raw<-unlist(strsplit(title[i]," "))
    p=toupper( gsub("'s","",raw))
    if(any(gsub("[][!#$%()*,.:;<=>@^_`|~.{}]", "", p) == toupper(Important)) ){  title.sen[i]=as.matrix(sentiment(title[i])[,4])*100000 } else #Multiplier
    { title.sen[i]=as.matrix(sentiment(title[i])[,4])}
  }
  title.sen<-as.matrix(title.sen)
  which.max(abs(title.sen))
  
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
News_us("TSLA",as.character(Sys.Date()))
