#News
library(httr)
library(jsonlite)

headlines<-"http://newsapi.org/v2/top-headlines?"
country=c("hk")
category=c("business","entertainment","general" ,"health" ,"science" ,"sports" ,"technology")
api_key="dbd4572f6fd547ddb9538f681cf3d4e8"
link= paste(headlines,"country=",country[1],"&","category=",category[7],"&","pageSize=100&sortBy=publishedAt","&","apiKey=",api_key,sep="")

qq<-GET(url = link)
response<-content(qq, as = "text", encoding = "UTF-8")
output=fromJSON(response, flatten = TRUE)
output$articles$title

#----

