# -*- coding: utf-8 -*-
"""
#Header Comments
#file created 02/02/2020 by Marissa Cubbage for ABE65100
#This file reads in a comma separated text file named 2008Male0006.txt which documents many variables concerning a model of a monkey named George
#The contents from the text file are stored in a dictionary, some simple analyses is done on some variables, and then a text file named georges_life.txt is created with results from analysiis and some data from the 2008Males0006.txt file

"""
#open the file 
Males= open("/home/mcubbage/ABE65100/03-working-with-files-in-python-mcubbage12/2008Male00006.txt", "r")

# read in first 45 bytes of the file
x=Males.read(45)
print (x)

#take the cursor back to begining of the file
Males.seek(0)

# reads single line depending on where the pointer is in the file
columns=Males.readline()
print(columns)

#read entire file 
Racc_file=Males.readlines()
print(Racc_file)

#close the file 
Males.close()

#create objec of zeros that has same length as number of lines in the racc_file
data=[0]*len(Racc_file)

#inserting Racc_file data into the object data, should create list of lists, where each list within the list is a line from the original file
#also in this code we convert certain fields into useful data types
for lidx in range(len(Racc_file)-1):
    data[lidx]=Racc_file[lidx].split(",")
    data[lidx][3]=int(data[lidx][3])
    data[lidx][8:15]=map(float,data[lidx][8:15])
    data[lidx][4:6]=map(float,data[lidx][4:6])
   

#create an empty dictionary to add to
racc_d=dict()


#convert columns into a list of strings
columns=columns.split(",")

#create blank list of lists to put values from data into
i=[0]*14
j=[i]*15

for lidx in range(15):
    j[lidx]=[]

#add values from data to create lists of lists which are the 15 variables
for lidx in range(15):
    for lidy in range(14):
        j[lidx].append(data[lidy][lidx])
        
#create dictionary where keywords are column headers and after the keyword is the data that goes with that column header
for lidx in range(15):
    racc_d[columns[lidx]]=j[lidx]       
    

#function to compute mean or average of a list

def mean(x):
    print (sum(x)/len(x))
#test mean function
mean(racc_d['Risk'])

#sum of elements in a list in the dictionary    
def total(x):
    print(sum(x))

#import math 
import math

#distance function to find distance between two points
def distance(lat,long):
    result=[]
    for i in range(len(lat)-1):
        result.append(((math.sqrt(((lat[i]-lat[i+1])**2.0)+((long[i]-long[i+1])**2.0)))))
    return result


#compute distance
distance(racc_d[' X'],racc_d[' Y'])

#add 0 to begininging of distance list and insert distance list into dictionary     
racc_d["Distance"]=[0]
racc_d["Distance"].extend(distance(racc_d[' X'],racc_d[' Y']))

#compute george's average energy level
mean(racc_d['Energy Level'])

#compute george's average location 
mean(racc_d[' X'])
mean(racc_d[' Y'])

#compute total distance george travelled over the course of his life
total(racc_d['Distance'])

#create a new output files named georges_life.txt
GL=open("georges_life.txt", "w")

#write header for georges_life.txt file
L=['Raccoon name: George \n','Average Location: 591189.03,4504604.08 \n','Distance Travelled: 593.9 \n','Average Energy level: 563.6 \n','Raccoon End State: DEAD \n']
GL.writelines(L)
GL.flush()

#write a tab delimited line of the colomn names
GL.write('\n')
CN=['Date','Time','X','Y','Asleep Flag','Behavior Mode','Distance Travelled']
GL.write("\t".join(CN))
GL.flush()


#convert floating point data (X,Y, and Distance) to strings   
for lidx in range(14):
    racc_d[' X'][lidx]=str(racc_d[' X'][lidx])
    racc_d[' Y'][lidx]=str(racc_d[' Y'][lidx])
    racc_d['Distance'][lidx]=str(racc_d['Distance'][lidx])
    
#write tab delimited data data for each hour of georges life for columns listed in object CN

GL.write('\n')
date=racc_d['Day']
GL.write("\t".join(date))
GL.flush()

GL.write('\n')
time=racc_d['Time']
GL.write("\t".join(time))
GL.flush()

GL.write('\n')
xx=racc_d[' X']
GL.write("\t".join(xx))
GL.flush()

GL.write('\n')
yy=racc_d[' Y']
GL.write("\t".join(yy))
GL.flush()

GL.write('\n')
A=racc_d[' Asleep']
GL.write("\t".join(A))
GL.flush()

GL.write('\n')
BM=racc_d['Behavior Mode']
GL.write("\t".join(BM))
GL.flush()

GL.write('\n')
D=racc_d['Distance']
GL.write("\t".join(D))
GL.flush()



