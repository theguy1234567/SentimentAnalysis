#________________________________________sentiment analysis with NLTK_____________________________________________________


# cleaning the text steps:
# STEP-1:create a text file and read text from it
#use encoding utf-8 as the format because the data on internet has same format
#STEP-2:convert the letter into lowercase (Apple not equal to apple)
#STEP-3:remove punctuation like .,!?etc 

import string #to remove punctuations
import matplotlib.pyplot as plt
from collections import Counter #to count the emotions
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer



with open('read.txt','r',encoding='utf-8') as file:
    text=file.read()
#print(text)
lower_case = text.lower()

#removing punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)


#tokanization 
#it means splitting the sentence into words
tokenized_words = word_tokenize(cleaned_text,"english")
#words that dont add  any meaning can be removed , tehy are called stop words

final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
#print(final_words)

# NLP emotion algorith 
# STEP-1:   check if the word in final words in also present in emotions file
# STEP-2:  if word is present -> add the emotion to emotion list
# STEP-3:   finally count each emotion in emotion list
emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        #if the word is in final_words append the corresponding emotion
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    #score will store positive and negative values in a dict
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos == neg:
        print("Neutal Sentiment")
    else:
        print("positive statement")
    
sentiment_analyse(cleaned_text)






#plotting the graph for emotions
fig, ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.xlabel("emotion")
plt.ylabel("emotion count")
plt.title("emotions graph")
plt.show()

