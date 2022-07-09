import pandas as pd
import spacy 
from processconnections import add_values_in_dict, get_list_sentences, process_sentences


# txt_file1 = open("File_of_all_train_sentences.txt", "r")
# file_content1 = txt_file1.read()
# txt_file1.close()

# txt_file2 = open("File_of_all_test_sentences.txt", "r")
# file_content2 = txt_file2.read()
# txt_file2.close()

txt_file3 = open("File_of_all_validate_sentences.txt", "r")
file_content3 = txt_file3.read()
txt_file3.close()

#file_content = file_content1 + file_content2 + file_content3
file_content = file_content3

#make the list of values 
content_list = file_content.split(",")

dictio = dict()
dictio = add_values_in_dict(dictio,'Sentence',content_list )




#for the tokenizer
nlp = spacy.load('en_core_web_sm')

words = dict()
 
for e in dictio['Sentence']: 
    tokens = nlp(e)
    for word in tokens :
        lemma = word.lemma_.lower()
        if lemma not in words.keys():
               words[lemma] = 1
        else:
              words[lemma] = words[lemma] + 1


# # # # # # # # keep only words with frequency >= 2

file = open("vocabulary.txt","w") 
for word in words:
          if words[word] >= 2:
           file.write(word + "\n")
file.close()
