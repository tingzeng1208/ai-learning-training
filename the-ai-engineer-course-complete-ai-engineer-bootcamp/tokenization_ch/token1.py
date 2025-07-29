import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize,sent_tokenize
# Example usage of word_tokenize    

# Example usage of tokenization
sentence = "her cat name is luna, her dog name is max"
print(sent_tokenize(sentence))


print(word_tokenize(sentence))