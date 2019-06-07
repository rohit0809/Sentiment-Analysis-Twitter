#!/usr/bin/env python3
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from pprint import pprint
import nltk
import yaml
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
if __name__ == "__main__":
    tp=79909
    tn=29274
    g= open('pos_5.0.yml', 'r')
    list_doc1= yaml.load(g)
    g= open('neg_1.0.yml', 'r')
    list_doc2= yaml.load(g)
    res_list_pos={}
    res_list_neg={}
    res_list={}
    for key in list_doc1:
        res_list_pos[key]=0
        res_list_neg[key]=0
        res_list[key]=0
    for key in list_doc2:
        res_list_pos[key]=0
        res_list_neg[key]=0
        res_list[key]=0
    for key in list_doc1:
        res_list_pos[key]=list_doc1[key]
    for key in list_doc2:
        res_list_neg[key]=(list_doc2[key])
    for key in res_list:
        res_list[key]=int(((res_list_pos[key]-res_list_neg[key]*(tp/tn))/(res_list_pos[key]+res_list_neg[key]*(tp/tn)))*2)
    with open('res.yml', 'w') as f:
        yaml.dump(res_list, f)
    
    
