import re
import pandas as pd
import numpy as np
import nltk


wpt = nltk.WordPunctTokenizer()

txt ="i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now"

stop_words=txt.split(" ")

corpus = "Rohit Gurunath Sharma is an Indian international cricketer, who is the current captain of the Indian national"


def normalize_doc(doc):
    doc = re.sub(r'[^a-zA-Z0-9\s]'," ",doc)
    doc=doc.lower()
    doc=doc.strip()
    # Tokenize Document
    tokens=wpt.tokenize(doc)
    # # filter stopwords out of document
    filtered_tokens=[token for token in tokens if token not in stop_words]
    # # re-create document from filtered tokens
    doc=" ".join(filtered_tokens)
    return doc


norma_vect = np.vectorize(normalize_doc)

res = norma_vect(corpus)


