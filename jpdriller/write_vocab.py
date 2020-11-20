# script for turning japanese Vocab_DB.xlsx data to .txt file for copy/past DB purpose

import pandas as pd

##################### Configuration ###########################
start = 1040
end = 1050

##################### Import/Build ###########################
# Import data from Vocab_DB.xlsx and build dictionaries
file_name = "Vocab_DB.xlsx"
sheet = "data_Word"
df = pd.read_excel(io=file_name, sheet_name=sheet)
df = df.set_index('ID')

# Vocab_DB useful columns : ['vocab', 'pronun', 'trans', 'note']
df_col = list(df.columns)

# Dictionaries
dict_vocab = {}
dict_pronun = {}
dict_trans = {}
dict_note = {}
dict_dict = {}
list_dict = [dict_vocab, dict_pronun, dict_trans, dict_note]
for i,elem in enumerate(df_col): # associe les col (clés) aux dict
    dict_dict[elem] = list_dict[i] # dict_dict = {"vocab":dict_vocab, "pronun":dict_pronun, "trans":dict_trans, "note":dict_note}

for item in df_col: # remplis les dict des data de la df : loop col
    for i in range(start, end+1): # remplis les dict des data de la df : loop row_start to row_end
        vocab_id = str(i) # clé du dict
        dict_dict[item][vocab_id] = df.loc[i, item] # e.g dict_vocab["1048"] = '実際に'

##################### .txt functions ###########################
def vocab(first, last):
    list_phrase = []
    for i in range(first, last+1):
        vocab_id = str(i)
        phrase = "vocab_" + vocab_id + \
                 " = Vocabulary(id='" + vocab_id + \
                 "',group='JLPT N2'," \
                 "vocabulary='" + dict_vocab[vocab_id] +\
                 "',pronunciation='" + dict_pronun[vocab_id] +\
                 "',translation='" + dict_trans[vocab_id] + \
                 "',note='" + dict_note[vocab_id] + \
                 "')"
        list_phrase.append(phrase)
    return list_phrase

def vocab2(first, last):
    phrase = "vocab_list = ["
    for i in range(first, last+1):
        vocab_id = str(i)
        if i<last:
            phrase = phrase + "vocab_" + vocab_id + ","
        else:
            phrase = phrase + "vocab_" + vocab_id + "]" + "\n" + "\n"
    return phrase

##################### .txt core ###########################
# start txt
start_txt = "from jpdriller.models import *" + "\n" + "\n" + "# Create model Vocabulary instances" + "\n"

# mid1 txt
mid1_txt = ""
for i in range(len(vocab(start, end))):
    mid1_txt = mid1_txt + vocab(start, end)[i] + "\n"
mid1_txt = mid1_txt + "\n"

# mid2 txt
mid2_txt = "# Create Vocabulary list" + "\n" + vocab2(start, end)

# end txt
end_txt = "# Call bulk_create to create records in a single call" + "\n" + "Vocabulary.objects.bulk_create(vocab_list)"

# concatenation txt
full_txt = start_txt + mid1_txt + mid2_txt + end_txt
print(full_txt)

##################### .txt write ###########################
# open and write the "write_vocab.txt" file
f = open("write_vocab.txt", "w", encoding='utf-8')
f.write(full_txt)
f.close()

##################### preview ###########################
# text du type :
#
# from jpdriller.models import *
#
# # Create model Vocabulary instances
# vocab_1048 = Vocabulary(id='1048',group='JLPT N2',vocabulary='実際に',pronunciation='じっさいに',translation='en pratique',note='*')
# vocab_1049 = Vocabulary(id='1049',group='JLPT N2',vocabulary='湿度',pronunciation='しつど',translation='humidité',note='*')
# vocab_1050 = Vocabulary(id='1050',group='JLPT N2',vocabulary='失う',pronunciation='うしなう',translation='perdre',note='* de l\'argent *')
#
# # Create Vocabulary list
# vocab_list = [vocab_1048,vocab_1049,vocab_1050]
#
# # Call bulk_create to create records in a single call
# Vocabulary.objects.bulk_create(vocab_list)
#
# 4 dict à construits depuis Excel du type :
# dict_vocab = {
#     "1048":'実際に',
#     "1049":'湿度',
#     "1050":'失う'
# }
#
# dict_pronun = {
#     "1048":'じっさいに',
#     "1049":'湿度',
#     "1050":'失う'
# }
#
# dict_trans = {
#     "1048":'en pratique',
#     "1049":'humidité',
#     "1050":'perdre'
# }
#
# dict_note = {
#     "1048":'*',
#     "1049":'*',
#     "1050":'* de l\'argent *'
# }
