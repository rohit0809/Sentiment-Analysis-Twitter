#!/usr/bin/env python3
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
if __name__ == "__main__":
    dictionary_paths=['Cell_Phones_and_Accessories_5_1.0.txt','Cell_Phones_and_Accessories_5_2.0.txt','Cell_Phones_and_Accessories_5_3.0.txt','Cell_Phones_and_Accessories_5_4.0.txt','Cell_Phones_and_Accessories_5_5.0.txt']
    files = [open(path, 'r') for path in dictionary_paths]
    f=0;
    for dict_file in files:
        c=0
        f=f+1
        fl='Cell_Phones_and_Accessories_5_'+str(f)+'.0'
        training=[]
        for line in dict_file:
            c=c+1 
            line = line.replace('\n','')
            training.append(line)
        sys.stdout=open(fl+"_training.txt",'a')
        for w in range(0,int(c/2)):
            print(training[w],)
        sys.stdout=open(fl+"_testing.txt",'a')
        for w in range(int(c/2),c):
            print(training[w],)
 
