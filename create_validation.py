from ctypes.wintypes import DWORD
from operator import index
from re import A, L
from sys import dont_write_bytecode
from tkinter import Y
import pandas as pd
import numpy as np
import csv
from pyparsing import java_style_comment
from processconnections import add_values_in_dict, create_connections,  delete_last_collum, get_list_sentences, index_to_sentence, process_sentences, sentence_to_index

###=======================================CREATE VALIDATION DATA FILES =============================================
###===========================================================================================================
###===========================================================================================================


#files 
def Vread_dev_files():
 f = []


 f.append(pd.read_csv( r"E:\\ProjectDialogues\dev_data\2004-11-15_03.ascii.txt", sep='/n  ' ,engine='python', header=None))
 f.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2005-06-27_12.ascii.txt", sep='/n  ' ,engine='python', header=None))
#  f.append(pd.read_csv(r"E:\\ProjectDialogues\dev_data\2005-08-08_01.ascii.txt", sep='/n  ' ,engine='python', header=None))
#  f.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2008-12-11_11.ascii.txt", sep='/n  ' ,engine='python', header=None))
#  f.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2009-02-23_10.ascii.txt", sep='/n  ' ,engine='python', header=None))
#  f.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2009-03-03_10.ascii.txt", sep='/n  ' ,engine='python', header=None))
#  f.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2009-10-01_17.ascii.txt", sep='/n  ' ,engine='python', header=None))
 
 
 return f

file_names = []
file_names.append("2004-11-15_03.ascii.txt")
file_names.append("2005-06-27_12.ascii.txt")
# file_names.append("2005-08-08_01.ascii.txt")
# file_names.append("2008-12-11_11.ascii.txt")
# file_names.append("2009-02-23_10.ascii.txt")
# file_names.append("2009-03-03_10.ascii.txt")
# file_names.append("2009-10-01_17.ascii.txt")

#final files
def Vprocess_files(f):

 f1f = []
 for i in range (0, len(f)):
  f1f.append(process_sentences(f[i]))
 return f1f


#annotation files
def Vcreate_annotation_files():
 af = []

 af.append( pd.read_csv( r"E:\\ProjectDialogues\dev_data\2004-11-15_03.annotation.txt", sep=' ' , header=None))
 af.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2005-06-27_12.annotation.txt", sep=' ' , header=None))
#  af.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2005-08-08_01.annotation.txt", sep=' ' , header=None))
#  af.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2008-12-11_11.annotation.txt", sep=' ' , header=None))
#  af.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2009-02-23_10.annotation.txt", sep=' ' , header=None))
#  af.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2009-03-03_10.annotation.txt", sep=' ' , header=None))
#  af.append( pd.read_csv(r"E:\\ProjectDialogues\dev_data\2009-10-01_17.annotation.txt", sep=' ' , header=None))
 return af



#final annotation files

def Vcreate_final_annotation_files(af):
 aff = []
 for i in range(0,len(af)):
  aff.append(delete_last_collum(af[i]))
 return aff



#lists of sentences 


def Vnew_list(f1f):
 list_file = []
 for i in range( 0, len(f1f)):
  list_file.append(get_list_sentences(f1f[i]))
 return list_file


# keep all sentences to a file 

def Vcreate_sent_file(list_file):
 textfile = open("File_of_all_validate_sentences.txt", "w")
 for i in range(0,len(list_file)):
  for element in list_file[i]:
   textfile.write(element + "\n")
 textfile.close()
 


#dictionairies of sentences(give the sentence and returns the id )

def Vsent_to_id(list_file):
 dict1 = []
 for i in range(0, len(list_file)):
     dict1.append(sentence_to_index(list_file[i]))
 return dict1

#dictionairies of sentences(give the id(num of line) and returns the sentence )
def Vid_to_sent(list_file):
 dict2 = []
 for i in range(0, len(list_file)) :
    dict2.append(index_to_sentence(list_file[i]))
 return dict2

#create tables of connections for each file
def Vcreate_connections(list_file,aff):
 connections = []
 for i in range(0, len(list_file)) :
     connections.append(create_connections(list_file[i], aff[i]))
 return connections





f = Vread_dev_files()    
f1f = Vprocess_files(f) 
af = Vcreate_annotation_files()
aff = Vcreate_final_annotation_files(af)
list_file = Vnew_list(f1f)
Vcreate_sent_file(list_file)
dict1 = Vsent_to_id(list_file)
dict2 =  Vid_to_sent(list_file)
connections = Vcreate_connections(list_file,aff)



## to parakatw arxeio exei kapoia bugs den kserw giati px sto print(connections[0][1018][1018]) to bgazei 0 mesa sto arxeio
##print(connections[0][1018][1018])
# auto giati yparxoun idies protaseis me diaforetiko id => bug prepei na diorthwthei


headerList = ['Sentence A', 'Sentence B' , 'Y','File Name']
with open("validate_sentences_1.csv", 'w' ) as file:
    dw = csv.DictWriter(file, delimiter='|',fieldnames=headerList, lineterminator='\n')
    dw.writeheader()
    for p in range(0,len(f)):
        for j in range (990,len(f[p]) ):
            for i in range (990, len(f[p])):
              dw.writerow({                   
                        'Sentence A': dict1[p][list_file[p][j]],
                        'Sentence B': dict1[p][list_file[p][i]],
                        'Y': connections[p][j][i],
                        'File Name' : file_names[p]
                        })




headerList = ['File Name','Id', 'Sentence'  ]
with open("validate_sentences_2.csv", 'w' ) as file:
    dw = csv.DictWriter(file, delimiter='|',fieldnames=headerList, lineterminator='\n')
    dw.writeheader()
    for p in range(0,len(f)):
        for i in range (990, len(f[p])):
         dw.writerow({   'File Name' : file_names[p],                
                        'Id': dict1[p][list_file[p][i]],
                        'Sentence': list_file[p][i]
                        

                        })
