from jpdriller.models import *

# Create model Vocabulary instances
vocab_1049 = Vocabulary(id='1051',group='JLPT N2',vocabulary='湿度2',pronunciation='しつど2',translation='humidité2',note='*2')
vocab_1050 = Vocabulary(id='1052',group='JLPT N2',vocabulary='失う2',pronunciation='うしなう2',translation='perdre2',note='*2')

# Create Vocabulary list
vocab_list = [vocab_1049,vocab_1050]

# Call bulk_create to create records in a single call
Vocabulary.objects.bulk_create(vocab_list)