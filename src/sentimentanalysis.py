from pprint import pprint
import nltk
import yaml
import re
import enchant
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
class Splitter(object):

    def __init__(self):
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
       
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences


class POSTagger(object):

    def __init__(self):
        pass
        
    def pos_tag(self, sentences):
               

        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        #adapt format
        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos

class DictionaryTagger(object):

    def __init__(self, dictionary_paths):
        files = [open(path, 'r') for path in dictionary_paths]
        dictionaries = [yaml.load(dict_file) for dict_file in files]
        map(lambda x: x.close(), files)
        self.dictionary = {}
        self.max_key_size = 10
        for curr_dict in dictionaries:
            for key in curr_dict:
                if key in self.dictionary:
                    self.dictionary[key].extend(curr_dict[key])
                else:
                    self.dictionary[key] = curr_dict[key]
                    #self.max_key_size = max(self.max_key_size, len(key))

    def tag(self, postagged_sentences):
        return [self.tag_sentence(sentence) for sentence in postagged_sentences]

    def tag_sentence(self, sentence, tag_with_lemmas=False):
        
        tag_sentence = []
        N = len(sentence)
        if self.max_key_size == 0:
            self.max_key_size = N
        i = 0
        while (i < N):
            j = min(i + self.max_key_size, N) #avoid overflow
            tagged = False
            while (j > i):
                expression_form = ' '.join([word[0] for word in sentence[i:j]]).lower()
                expression_lemma = ' '.join([word[1] for word in sentence[i:j]]).lower()
                if tag_with_lemmas:
                    literal = expression_lemma
                else:
                    literal = expression_form
                if literal in self.dictionary:
                    #self.logger.debug("found: %s" % literal)
                    is_single_token = j - i == 1
                    original_position = i
                    i = j
                    taggings = [tag for tag in self.dictionary[literal]]
                    tagged_expression = (expression_form, expression_lemma, taggings)
                    if is_single_token: #if the tagged literal is a single token, conserve its previous taggings:
                        original_token_tagging = sentence[original_position][2]
                        tagged_expression[2].extend(original_token_tagging)
                    tag_sentence.append(tagged_expression)
                    tagged = True
                else:
                    j = j - 1
            if not tagged:
                tag_sentence.append(sentence[i])
                i += 1
        return tag_sentence

def value_of(sentiment):
    if sentiment == 'positive': return 1
    if sentiment == 'negative': return -1
    return 0

def sentence_score(sentence_tokens, previous_token, acum_score):    
    if not sentence_tokens:
        return acum_score
    else:
        current_token = sentence_tokens[0]
        tags = current_token[2]
        token_score = sum([value_of(tag) for tag in tags])
        if previous_token is not None:
            previous_tags = previous_token[2]
            if 'inc' in previous_tags:
                token_score *= 2.0
            elif 'dec' in previous_tags:
                token_score /= 2.0
            elif 'inv' in previous_tags:
                token_score *= -1.0
        return sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])

if __name__ == "__main__":
    lemmatizer = WordNetLemmatizer()
    f=open('Automotive_5_5.0_testing.txt','r')
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = enchant.Dict("en_US")
    operators = set(('not','isnt','arent','wasnt','werent'))
    stop_words = set(stopwords.words('english'))-operators
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    #word="nothing but don't 5 headach"
    g= open('res.yml', 'r')
    list_doc1= yaml.load(g)
    p=open('ph_res.yml', 'r')
    list_doc2= yaml.load(p)
    for line in f:
        print(line)
        fwords=[]
        for w1 in line.split():
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
                
                    fwords.append(lemmatizer.lemmatize(t))
                    if t in stop_words:
                        continue 
                    t=""
            if t!="":
                if not d.check(t):
                    if d.suggest(t):
                        t=d.suggest(t)[0]
                t=''.join(filter(None,t.split(' ')))
                
                fwords.append(lemmatizer.lemmatize(t))
            if t in stop_words:
                continue 
            t=""
        score1=0
        flag=0
        for w in fwords:
            #print(w)
            if w in operators:
                flag=1
                continue
            if list_doc1.get(w) is None:
                l=0
            else:
                l=int(list_doc1.get(w));
            score1=score1+l-(1*flag)
            flag=0;
        score1=0
        for w in fwords:
            #print(w)
            if w in operators:
                flag=1
                continue
            if list_doc1.get(w) is None:
                l=0
            else:
                l=int(list_doc1.get(w));
            score1=score1+l-(1*flag)
            flag=0;
        score2=0
        for w in range(len(fwords)-3):
            temp=fwords[w]+" "+fwords[w+1]+" "+fwords[w+2]
            if list_doc2.get(temp) is None:
                l=0
            else:
                l=int(list_doc2.get(temp));
            score2=score2+l
        score3=0
        for w in range(len(fwords)-2):
            temp=fwords[w]+" "+fwords[w+1]
            if list_doc2.get(temp) is None:
                l=0
            else:
                l=int(list_doc2.get(temp));
            score3=score3+l
        print(((score1)+(score2)+(score3))/3)
    
