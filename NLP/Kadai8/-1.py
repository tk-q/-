from gensim.models import KeyedVectors
path="/Users/takeidaichi/NLP/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(path, binary=True)
print(model['United_States'])
