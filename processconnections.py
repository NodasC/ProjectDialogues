from operator import index
import pandas as pd
import numpy as np


 
#argument : table of sentences , returns: table of sentences processed
#takes only the text segment of each sentence

def process_sentences(df):
 df_trans = np.transpose(df)
 for i in df_trans:
    if '> ' in df_trans[i][0]:
        [trash,df_trans[i][0]] = df_trans[i][0].split('> ',1)
 dfn = np.transpose(df_trans)
 return dfn
 

#argument: table from annotation files, returns: table of ids processed
#converts list of ids to numpy and deletes the last collum which contains (-)

def delete_last_collum(af):

  ranp = af.to_numpy()
  ids = np.delete(ranp,2,1)
  return ids


#argument: table of sententes , returns: list of sentences 
#contains all sentences to a list 

def get_list_sentences(ff):
 mylist_sentences = []
 anp = ff.to_numpy()
 for i in range(0,len(anp)):
  mylist_sentences.append((anp[i][0]))
 return mylist_sentences


   
#dict that gives one integer to each sentence so now we have {key--->(sentence) : value --->number}
#and the inverse , giving an sentence to each integer
#print(sentence_to_index['Hello everyone. Are there XFCE-desktop-experienced people around? I could use some help please.'])
#print(index_to_sentence[1000])


def sentence_to_index(sentences):
 return dict((s,i) for i,s in enumerate(sentences,1) )

def index_to_sentence(sentences):
 return dict((s,i) for s,i in enumerate(sentences,1) )



#2d dimensional array that contains 0 and 1 when a connection occurs
#arguments: list of sentences, table of ids ,returns table of connections

def create_connections(list_of_sentences, ids):

 connections = [[1 for x in range(len(list_of_sentences))] for y in range(len(list_of_sentences))]

 for i in range(1,len(list_of_sentences),1):
    for j in range(1,len(list_of_sentences),1):
        connections[i][j]=0
      
 for i in range(0, np.size(ids,0)):
   connections[ids[i][0]][ids[i][1]] = 1
 
 return connections



def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict











