from asyncio.windows_events import NULL
from ctypes.wintypes import DWORD
from operator import index
from re import A
from sys import dont_write_bytecode
import pandas as pd
import numpy as np
import csv
from pyparsing import java_style_comment
from processconnections import add_values_in_dict, create_connections, delete_last_collum, get_list_sentences, index_to_sentence, process_sentences, sentence_to_index


###=======================================CREATE TRAIN DATA FILES =============================================
###===========================================================================================================
###===========================================================================================================

#files 
f = []
file_names = []

f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2004-12-25.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-02-06.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-02-08.train-a.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-02-27.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-05-14.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-05-19.train-a.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-06.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-12.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-16.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-20.train-a.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-07-25.train-a.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-07-29.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-09-26.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-10-07.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-10-12.train-c.ascii.txt", sep='/n  ' , header=None))
f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-03.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-04.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-16.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-23.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-01-02.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-01-12.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-02-20.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-02-24.train-a.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-02-28.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-03-05.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-02.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-15.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-27.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-29.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-01.train-a.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-05.train-a.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-08.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-21.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-06-28.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-07-01.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-08-06.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-08-11.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-08-13.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-08-15.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-09-13.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-11-01.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-12-06.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2006-12-20.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2007-01-12.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2007-01-21.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2007-01-29.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2007-02-06.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2007-02-07.train-c.ascii.txt", sep='/n  ' , header=None))
# f.append( pd.read_csv( r"E:\\ProjectDialogues\train_data\2007-02-15.train-c.ascii.txt", sep='/n  ' , header=None))


file_names.append("2004-12-25.train-c.ascii.txt")
file_names.append("2005-02-06.train-c.ascii.txt")
file_names.append("2005-02-08.train-a.ascii.txt")
file_names.append("2005-02-27.train-c.ascii.txt")
file_names.append("2005-05-14.train-c.ascii.txt")
file_names.append("2005-05-19.train-a.ascii.txt")
file_names.append("2005-06-06.train-c.ascii.txt")
file_names.append("2005-06-12.train-c.ascii.txt")
file_names.append("2005-06-16.train-c.ascii.txt")
file_names.append("2005-06-20.train-a.ascii.txt")
file_names.append("2005-07-25.train-a.ascii.txt")
file_names.append("2005-07-29.train-c.ascii.txt")
file_names.append("2005-09-26.train-c.ascii.txt")
file_names.append("2005-10-07.train-c.ascii.txt")
file_names.append("2005-10-12.train-c.ascii.txt")
file_names.append("2005-12-03.train-c.ascii.txt")
# file_names.append("2005-12-04.train-c.ascii.txt")
# file_names.append("2005-12-16.train-c.ascii.txt")
# file_names.append("2005-12-23.train-c.ascii.txt")
# file_names.append("2006-01-02.train-c.ascii.txt")
# file_names.append("2006-01-12.train-c.ascii.txt")
# file_names.append("2006-02-20.train-c.ascii.txt")
# file_names.append("2006-02-24.train-a.ascii.txt")
# file_names.append("2006-02-28.train-c.ascii.txt")
# file_names.append("2006-03-05.train-c.ascii.txt")
# file_names.append("2006-05-02.train-c.ascii.txt")
# file_names.append("2006-05-15.train-c.ascii.txt")
# file_names.append("2006-05-27.train-c.ascii.txt")
# file_names.append("2006-05-29.train-c.ascii.txt")
# file_names.append("2006-06-01.train-a.ascii.txt")
# file_names.append("2006-06-05.train-a.ascii.txt")
# file_names.append("2006-06-08.train-c.ascii.txt")
# file_names.append("2006-06-21.train-c.ascii.txt")
# file_names.append("2006-06-28.train-c.ascii.txt")
# file_names.append("2006-07-01.train-c.ascii.txt")
# file_names.append("2006-08-06.train-c.ascii.txt")
# file_names.append("2006-08-11.train-c.ascii.txt")
# file_names.append("2006-08-13.train-c.ascii.txt")
# file_names.append("2006-08-15.train-c.ascii.txt")
# file_names.append("2006-09-13.train-c.ascii.txt")
# file_names.append("2006-11-01.train-c.ascii.txt")
# file_names.append("2006-12-06.train-c.ascii.txt")
# file_names.append("2006-12-20.train-c.ascii.txt")
# file_names.append("2007-01-12.train-c.ascii.txt")
# file_names.append("2007-01-21.train-c.ascii.txt")
# file_names.append("2007-01-29.train-c.ascii.txt")
# file_names.append("2007-02-06.train-c.ascii.txt")
# file_names.append("2007-02-07.train-c.ascii.txt")
# file_names.append("2007-02-15.train-c.ascii.txt")





#final files

f1f = []
for i in range (0, len(f)):
 f1f.append(process_sentences(f[i]))

#annotation files
af = []

af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2004-12-25.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-02-06.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-02-08.train-a.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-02-27.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-05-14.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-05-19.train-a.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-06.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-12.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-16.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-06-20.train-a.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-07-25.train-a.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-07-29.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-09-26.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-10-07.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-10-12.train-c.annotation.txt",sep=' ',header=None))
af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-03.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-04.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-16.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2005-12-23.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-01-02.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-01-12.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-02-20.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-02-24.train-a.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-02-28.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-03-05.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-02.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-15.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-27.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-05-29.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-01.train-a.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-05.train-a.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-08.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-21.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-06-28.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-07-01.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-08-06.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-08-11.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-08-13.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-08-15.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-09-13.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-09-24.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-11-01.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-12-06.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2006-12-20.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2007-01-12.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2007-01-21.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2007-01-29.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2007-02-06.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2007-02-07.train-c.annotation.txt",sep=' ',header=None))
# af.append( pd.read_csv(r"E:\\ProjectDialogues\train_data\2007-02-15.train-c.annotation.txt",sep=' ',header=None))






#final annotation files
aff = []
for i in range(0,len(af)):
 aff.append(delete_last_collum(af[i]))




#lists of sentences 
list_file = []
for i in range( 0, len(f1f)):
 list_file.append(get_list_sentences(f1f[i]))




# keep all sentences to a file

textfile = open("File_of_all_train_sentences.txt", "w")
for i in range(0, len(list_file)) :
   for element in list_file[i] :
     textfile.write(element + "\n")
textfile.close()



#dictionairies of sentences(give the sentence and returns the id )



dict1 = []
for i in range(0, len(list_file)):
    dict1.append(sentence_to_index(list_file[i]))



# #dictionairies of sentences(give the id(num of line) and returns the sentence )


dict2 = []
for i in range(0, len(list_file)) :
    dict2.append(index_to_sentence(list_file[i]))

#print(dict2[1][148])



# #create tables of connections for each file


connections = []
for i in range(0, len(list_file)) :
     connections.append(create_connections(list_file[i], aff[i]))


#CSV file for all train data

headerList = ['Sentence A', 'Sentence B' , 'Y','File Name']
with open("train_sentences_1.csv", 'w' ) as file:
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
with open("train_sentences_2.csv", 'w' ) as file:
    dw = csv.DictWriter(file, delimiter='|',fieldnames=headerList, lineterminator='\n')
    dw.writeheader()
    for p in range(0,len(f)):
        for i in range (990, len(f[p])):
         dw.writerow({   'File Name' : file_names[p],                
                        'Id': dict1[p][list_file[p][i]],
                        'Sentence': list_file[p][i]
                        

                        })