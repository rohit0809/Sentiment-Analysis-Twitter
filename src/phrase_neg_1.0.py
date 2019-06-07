from pprint import pprint
import re
import nltk
import yaml
import enchant
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer

if __name__ == "__main__":
    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()
    d = enchant.Dict("en_US")
    f=open('Neg_tweets_1.0.txt','r')
    #g= open('pos_5.0.yml', 'r')
    #list_doc= yaml.load(g)
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list_doc={}
    
    ph=[]
    operators = set(('but', 'not'))
    stop_words = set(stopwords.words('english'))-operators
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    
    for line in f:
        #word_tokens = word_tokenize(line)
        #splitted_sentences = splitter.split(splitted_sentences)
        #filtered_sentence = [w for w in word_tokens if not w in stop_words]

        #filtered_sentence = ""
        #print(1)
        #re.split(' ',line)
        fwords=[]
        c=0
        for w1 in line.split(' '):
            w1=w1.lower()
            t=""
            for ch in w1:
                if ch in letters:
                    t+=ch  
                elif t!="":
                    if not d.check(t):
                        if d.suggest(t):
                            t=d.suggest(t)[0]
                    t=''.join(filter(None,t.split(' ')))
                    if t in stop_words:
                        t=""
                        continue 
                    fwords.append(lemmatizer.lemmatize(t))
                    t=""
            if t!="":
                if not d.check(t):
                    if d.suggest(t):
                        t=d.suggest(t)[0]
                t=''.join(filter(None,t.split(' ')))
                if t in stop_words:
                    t=""
                    continue
                #print(t)
                #if t=='***Misspelt***':
                 #   #print(t)
                  #  t=""
                   # continue
                fwords.append(lemmatizer.lemmatize(t))
            t=""
            if len(fwords)==1:
                continue
            elif len(fwords)==2:
                ph.append(fwords[0]+" "+fwords[1])
            else:
                for w in range(len(fwords)-3):
                    ph.append(fwords[w]+" "+fwords[w+1]+" "+fwords[w+2])
                for w in range(len(fwords)-2):
                    ph.append(fwords[w]+" "+fwords[w+1])
    for w in ph:
        list_doc[w]=0
    for w in ph:
        c=list_doc[w]
        list_doc[w]=c+1
    with open('ph_1.0.yml', 'w') as g:
        yaml.dump(list_doc, g)
    
    f.close()
    g.close()

        