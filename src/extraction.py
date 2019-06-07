#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import re
import sys
shakes = open("C:\\Users\\Shri89\\Desktop\\fyp\\Video_Games_5.json", "r")
sys.stdout  = open("C:\\Users\\Shri89\\Desktop\\fyp\\Video_Games_5_5.0.txt", "a")

c=0
flag=0
cr=0
#print(sys.version)
for line in shakes:
        words=line.split(" ")
        flag=0
        fl=0
        wrd=""
        fin=""
        for ch in words:
            if(ch=="5.0,"):
                fl=1
            elif(ch=="3.0," or ch=="1.0," or ch=="4.0," or ch=="2.0,"):
                break
            if(fl==1):
                
                if(ch=="\"unixReviewTime\":"):
                    
                    fin=""
                    for chr in wrd:
                        if(chr=='"' or chr==","):
                            continue
                        fin+=chr
                    print(fin)
                    c=c+1
                    break
                if(flag==1):
                    
                   wrd+=ch
                   wrd+=" "
                   continue
                if(ch=="\"summary\":"):
                   flag=1
                   wrd=""
        if(c==10000):
            break
