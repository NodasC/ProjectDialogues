import csv
from ntpath import join
from tkinter.font import names
from unicodedata import name
import h5py
import keras
from keras.callbacks import EarlyStopping
from keras.layers import Input, LSTM, GRU, Dense, Embedding, Activation, Dropout, concatenate
from keras.layers import Bidirectional
from keras.models import Model
from keras.models import load_model
from keras.optimizers import RMSprop, Adam
import numpy as np
import os
import pandas as pd
import spacy 
import tensorflow as tf
from torch import negative
from processconnections import add_values_in_dict, get_list_sentences, index_to_sentence
from keras.preprocessing import sequence



train_loc_1 = r"E:\\ProjectDialogues\train_sentences_1.csv"
val_loc_1 = r"C:\\Users\30694\Desktop\ProjectDialogues\validate_sentences_1.csv"
test_loc_1 = r"E:\\ProjectDialogues\test_sentences_1.csv"


train_loc_2 = r"E:\\ProjectDialogues\train_sentences_2.csv"
val_loc_2 = r"C:\\Users\30694\Desktop\ProjectDialogues\validate_sentences_2.csv"
test_loc_2 = r"E:\\ProjectDialogues\test_sentences_2.csv"


output_results = r"C:\\Users\30694\Desktop\ProjectDialogues\evaluation.txt"

glove_file = r"C:\\Users\30694\Desktop\ProjectDialogues\glove.6B.50d.txt"

vocab = r"C:\\Users\30694\Desktop\ProjectDialogues\vocabulary.txt"


# TEST_SIZE = 0.1
GLOVE_DIM = 50

# Maximum length for sentences
#auto borw na to vrw me ton zip algorythm
maxlen = 25

tf.random.set_seed(42)


nb_vocab = 1343 
batch_size = 64
epochs = 15
threshold = 0.5


config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.2
tf.compat.v1.Session(config=config)




sentences_validate = []
sentences_validate.append(pd.read_csv(val_loc_2, header = 0 , names = ['File Name','Id', 'Sentence'],nrows=260, sep="|"))
sentences_validate.append(pd.read_csv(val_loc_2, header = 0 , names = ['File Name','Id', 'Sentence'],skiprows=260 , nrows =260, sep="|"))



#keeping this line to comment to fix it if i add more files 
# dfn = pd.read_csv("mydata.csv", skiprows=(n-1)*10000, nrows=10000)

sentences_validate_dict = []
sentences_validate_dict.append(dict(zip(sentences_validate[0]['Id'].to_list(), sentences_validate[0]['Sentence'].to_list())))
sentences_validate_dict.append(dict(zip(sentences_validate[1]['Id'].to_list(), sentences_validate[1]['Sentence'].to_list())))

# print(sentences_validate_dict[0])
# print(sentences_validate_dict[1])

#print(len(sentences_validate_dict)) ## opote auto to kanei gia to deftero arxeio afou sunanta 2 fores to idio id 




w2i, i2w = {}, []

for line in open(vocab):
    line = line.strip()
    w2i[line] = len(i2w)
    i2w.append(line)



#create our numpy data in order to to do the padding needed and to pass the to our NN

def create_data(data, sentences_dict, maxlen):

     
    n_A = [[]] 
    n_B =[[]]
    n_label = [[]]

    n_label.append([i for i in data[0]['Y']])
    n_A.append([[w2i[w.lemma_.lower()] if w.lemma_.lower() in w2i else w2i['_UNK'] for w in nlp(sentences_dict[0][e])] + [w2i['_EOS']] for e in data[0]['Sentence A'] ]) 
    n_B.append([[w2i[w.lemma_.lower()] if w.lemma_.lower() in w2i else w2i['_UNK'] for w in nlp(sentences_dict[0][e])] + [w2i['_EOS']] for e in data[0]['Sentence B'] ])

  
    n_label.append([i for i in data[1]['Y']])
    n_A.append([[w2i[w.lemma_.lower()] if w.lemma_.lower() in w2i else w2i['_UNK'] for w in nlp(sentences_dict[1][e])] + [w2i['_EOS']] for e in data[1]['Sentence A'] ] )
    n_B.append([[w2i[w.lemma_.lower()] if w.lemma_.lower() in w2i else w2i['_UNK'] for w in nlp(sentences_dict[1][e])] + [w2i['_EOS']] for e in data[1]['Sentence B'] ] )

    
    return np.array(n_label), np.array(n_A), np.array(n_B)


# # #Αν καταλαβαίνω σωστά αυτή η συνάρτηση παίρνει το vocab και το glove και βρίσκει για κάθε λέξη του vocab
# # #την αναπαράσταση της απο το glove file που έχουμε 

# def glove_word2vec_matrix(glove_file,vocab,dim):

#     embeddings_index = {}

#     f = open(glove_file,encoding='utf-8') 
#     for line in f:
#         values = line.split()
#         word = values[0]
#         coefs = np.asarray(values[1:],dtype='float32')
#         embeddings_index[word]=coefs
#     f.close()

#     embedding_matrix = np.zeros((nb_vocab,dim))
#     for word,i in w2i.items():
#         try :
#             embedding_vector = embeddings_index.get(word)
#         except Exception:
#             embedding_vector = None
#         if embedding_vector is not None:
#             #words not found in embedding index will be all-zeros
#             embedding_matrix[i] = embedding_vector

#     return embedding_matrix 



# for the tokenizer 

nlp = spacy.load('en_core_web_sm')


val_data = []
val_data.append(pd.read_csv(val_loc_1, header = 0 , names = ['Sentence A', 'Sentence B', 'Y', 'File Name'], sep="|",nrows=67600))
val_data.append(pd.read_csv(val_loc_1, header = 0 , names = ['Sentence A', 'Sentence B', 'Y', 'File Name'], sep="|",skiprows=67600,nrows=67600))




y_val, n_A_val, n_B_val = create_data(val_data,sentences_validate_dict, maxlen)

print(n_A_val)

n_A_val = sequence.pad_sequences(n_A_val,maxlen)
n_B_val =  sequence.pad_sequences(n_B_val,maxlen)



# embedding_matrix = glove_word2vec_matrix(glove_file,vocab,GLOVE_DIM) 
       
       
# shared_input = Input(shape=(maxlen,))
# emb = Embedding(nb_vocab,GLOVE_DIM,weights = [embedding_matrix],input_length=maxlen,trainable=False,mask_zero = True)(shared_input)
# #emb_drop = Dropout(0.5)(emb)
# lstm = Bidirectional(LSTM(GLOVE_DIM, dropout=0.2, recurrent_dropout=0.2))(emb)
# shared_network = Model(shared_input, lstm)
        
# input_A = Input(shape=(maxlen,))
# output_A = shared_network(input_A)
# input_B = Input(shape=(maxlen,))
# output_B = shared_network(input_B)

        
               
# merged_vector = keras.layers.concatenate([output_A, output_B],
#                                          axis=-1)
           
# concat_hidden = Dense(2*GLOVE_DIM,activation='relu')(merged_vector)
# logits = Dense(1)(concat_hidden)
# predictions = Activation('sigmoid')(logits)
          
# model = Model(inputs=[input_A, input_B], outputs=predictions)
          
# optimizer = Adam(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
# checkpointer = EarlyStopping(monitor='val_loss', patience=5, verbose=0, mode='min')

      
# model.save('mymodel')
   