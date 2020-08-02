import nltk
import gensim
import numpy as np
import smart_open
from nltk.tokenize import word_tokenize, sent_tokenize

def model(model_answer, answer):

    # model_answer = "Malls are great places to shop, I can find everything I need under one roof. I love eating toasted cheese and tuna sandwiches. Should we start class now, or should we wait for everyone to get here?"
    # answer = "Malls are goog for shopping. What kind of bread is used for sandwiches? Do we have to start class now, or should we wait for everyone to come here? "

    #open file and tokenize sentences 

    file_docs = []

    # with open ('demofile.txt') as f:
    tokens = sent_tokenize(model_answer)
    for line in tokens:
        file_docs.append(line)


    #Tokenize words and create dictionary
    gen_docs = [[w.lower() for w in word_tokenize(text)] 
                for text in file_docs]

    dictionary = gensim.corpora.Dictionary(gen_docs)


    #Create a bag of words
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

    # TFIDF
    # words that occur more frequently across the documents get smaller weights.
    tf_idf = gensim.models.TfidfModel(corpus)

    # Creating similarity measure object
    # building the index
    sims = gensim.similarities.Similarity('workdir/',tf_idf[corpus],
                                        num_features=len(dictionary))

    # Create Query Document
    file2_docs = []

    # with open ('demofile2.txt') as f:
    tokens = sent_tokenize(answer)
    for line in tokens:
        file2_docs.append(line)

    for line in file2_docs:
        query_doc = [w.lower() for w in word_tokenize(line)]
        # update an existing dictionary and create bag of words
        query_doc_bow = dictionary.doc2bow(query_doc)

    # perform a similarity query against the corpus
    query_doc_tf_idf = tf_idf[query_doc_bow]
    # print('Comparing Result:', max(sims[query_doc_tf_idf]))
    print(max(sims[query_doc_tf_idf]))
    return max(sims[query_doc_tf_idf])

if __name__ == "__main__":
    print(model("Malls are great places to shop, I can find everything I need under one roof. I love eating toasted cheese and tuna sandwiches. Should we start class now, or should we wait for everyone to get here?",
    "Malls are goog for shopping. What kind of bread is used for sandwiches? Do we have to start class now, or should we wait for everyone to come here? "))