#________________________________________sentiment analysis without NLTK_____________________________________________________


# cleaning the text steps:
# STEP-1:create a text file and read text from it
#use encoding utf-8 as the format because the data on internet has same format
#STEP-2:convert the letter into lowercase (Apple not equal to apple)
#STEP-3:remove punctuation like .,!?etc 

import string #to remove punctuations
import matplotlib.pyplot as plt
from collections import Counter #to count the emotions



with open('read.txt','r',encoding='utf-8') as file:
    text=file.read()
#print(text)
lower_case = text.lower()

#removing punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)


#tokanization 
#it means splitting the sentence into words
tokenized_words = cleaned_text.split()
#words that dont add  any meaning can be removed , tehy are called stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words=[]
for word in tokenized_words:
    if word not in stop_words:
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

#plotting the graph for emotions
fig, ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.xlabel("emotion")
plt.ylabel("emotion count")
plt.title("emotions graph")
plt.show()

