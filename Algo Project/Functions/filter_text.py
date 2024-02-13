from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
def filter_text(text):
    X_tokenize=[word_tokenize(t) for t in text]
    sb = SnowballStemmer("english") 
    #nltk.download('stopwords')
    stop_words = set(stopwords.words("english")) 

    X_digit=[]
    for j in range(len(X_tokenize)):
        X_digit.append([X_tokenize[j][i] for i in range(len(X_tokenize[j])) if not X_tokenize[j][i].isdigit()]) 
    
    X_sw=[]
    for i in range(len(X_digit)):

        X_sw.append([w for w in X_digit[i] if not w in stop_words] )

    X_filtered=[]
    for i in range(len(X_sw)):
        X_filtered.append([sb.stem(word) for word in X_sw[i]])
    return(X_filtered)

