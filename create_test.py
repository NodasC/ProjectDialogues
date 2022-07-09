from ctypes.wintypes import DWORD
from operator import index
from re import A, L
from sys import dont_write_bytecode
import pandas as pd
import numpy as np
import csv
from pyparsing import java_style_comment
from processconnections import add_values_in_dict, create_connections,  delete_last_collum, get_list_sentences, index_to_sentence, process_sentences, sentence_to_index

###=======================================CREATE TEST DATA FILES =============================================
###===========================================================================================================
###===========================================================================================================


#files 
f = []
file_names = []

f.append(pd.read_csv( r"E:\\ProjectDialogues\test_data\2005-07-06_14.ascii.txt",sep='/n  ', engine = 'python' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\test_data\2007-01-11_12.ascii.txt", sep='/n  ', engine = 'python', header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\test_data\2007-12-01_03.ascii.txt", sep='/n  ', engine = 'python' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\test_data\2008-07-14_18.ascii.txt", sep='/n  ', engine = 'python' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\test_data\2010-08-17_18.ascii.txt", sep='/n  ', engine = 'python' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\test_data\2013-09-01_02.ascii.txt", sep='/n  ', engine = 'python', header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\test_data\2014-06-18_13.ascii.txt", sep='/n  ', engine = 'python' , header=None))

file_names.append("2005-07-06_14.ascii.txt")
file_names.append("2007-01-11_12.ascii.txt")
# file_names.append("2007-12-01_03.ascii.txt")
# file_names.append("2008-07-14_18.ascii.txt")
# file_names.append("2010-08-17_18.ascii.txt")
# file_names.append("2013-09-01_02.ascii.txt")
# file_names.append("2014-06-18_13.ascii.txt")

#final files
f1f = []
for i in range (0, len(f)):
 f1f.append(process_sentences(f[i]))




#annotation files

af = []

af.append(pd.read_csv( r"E:\\ProjectDialogues\test_data\2005-07-06_14.annotation.txt", sep=' ' , header=None))
af.append(pd.read_csv(r"E:\\ProjectDialogues\test_data\2007-01-11_12.annotation.txt", sep=' ' , header=None))
# af.append(pd.read_csv(r"E:\\ProjectDialogues\test_data\2007-12-01_03.annotation.txt", sep=' ' , header=None))
# af.append(pd.read_csv(r"E:\\ProjectDialogues\test_data\2008-07-14_18.annotation.txt", sep=' ' , header=None))
# af.append(pd.read_csv(r"E:\\ProjectDialogues\test_data\2010-08-17_18.annotation.txt", sep=' ' , header=None))
# af.append(pd.read_csv(r"E:\\ProjectDialogues\test_data\2013-09-01_02.annotation.txt", sep=' ' , header=None))
# af.append(pd.read_csv(r"E:\\ProjectDialogues\test_data\2014-06-18_13.annotation.txt", sep=' ' , header=None))




#final annotation files

aff = []
for i in range(0,len(af)):
 aff.append(delete_last_collum(af[i]))


#lists of sentences 

list_file = []
for i in range( 0, len(f1f)):
 list_file.append(get_list_sentences(f1f[i]))





textfile = open("File_of_all_test_sentences.txt", "w")
for i in range(0,len(list_file)):
 for element in list_file[i]:
  textfile.write(element + "\n")
textfile.close()



#dictionairies of sentences(give the sentence and returns the id )

dict1 = []
for i in range(0, len(list_file)):
    dict1.append(sentence_to_index(list_file[i]))


#dictionairies of sentences(give the id(num of line) and returns the sentence )
dict2 = []
for i in range(0, len(list_file)) :
    dict2.append(index_to_sentence(list_file[i]))


connections = []
for i in range(0, len(list_file)) :
     connections.append(create_connections(list_file[i], aff[i]))



headerList = ['Sentence A', 'Sentence B' , 'Y','File Name']
with open("test_sentences_1.csv", 'w' ) as file:
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
with open("test_sentences_2.csv", 'w' ) as file:
    dw = csv.DictWriter(file, delimiter='|',fieldnames=headerList, lineterminator='\n')
    dw.writeheader()
    for p in range(0,len(f)):
        for i in range (990, len(f[p])):
         dw.writerow({   'File Name' : file_names[p],                
                        'Id': dict1[p][list_file[p][i]],
                        'Sentence': list_file[p][i]
                        

                        })