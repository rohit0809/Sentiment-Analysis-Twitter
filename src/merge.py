#!/usr/bin/env python3
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
if __name__ == "__main__":
    dictionary_paths=['Apps_for_Android_5_1.0_testing.txt','Cell_Phones_and_Accessories_5_1.0_testing.txt','Automotive_5_1.0_testing.txt','Baby_5_1.0_testing.txt','Beauty_5_1.0_testing.txt','Musical_Instruments_5_1.0_testing.txt','Kindle_Store_5_1.0_testing.txt','Home_and_Kitchen_5_1.0_testing.txt','Health_and_Personal_Care_5_1.0_testing.txt','Grocery_and_Gourmet_Food_5_1.0_testing.txt','Digital_Music_5_1.0_testing.txt','Clothing_Shoes_and_Jewelry_5_1.0_testing.txt','Electronics_5_1.0_testing.txt','CDs_and_Vinyl_5_1.0_testing.txt','Office_Products_5_1.0_testing.txt','Patio_Lawn_and_Garden_5_1.0_testing.txt','Pet_Supplies_5_1.0_testing.txt','Sports_and_Outdoors_5_1.0_testing.txt','Tools_and_Home_Improvement_5_1.0_testing.txt','Toys_and_Games_5_1.0_testing.txt','Video_Games_5_1.0_testing.txt']
    files = [open(path, 'r') for path in dictionary_paths]
    fl='Testing_1.0.txt'
    sys.stdout=open(fl,'a')
    for dict_file in files:
        for line in dict_file:
            line = line.replace('\n','')
            print(line)
 
