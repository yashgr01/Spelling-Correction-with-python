#Spelling correction with python program 

from textblob import TextBlob
import textblob
words = ["Data Scence","Mahine learnin","Dicionary"]#Incorrect spellings
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
    print("Wrong word: ",words)
    print("corrected words are: ")
for i in corrected_words:
    print(i.correct(),end=" ")
