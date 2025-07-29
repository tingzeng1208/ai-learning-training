import nltk
from nltk.stem import PorterStemmer
connect_token = ["connect", "connects", "connected", "connecting"]
for token in connect_token:
    print(token, " : ", PorterStemmer().stem(token))