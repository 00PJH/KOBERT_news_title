# Load model directly
from transformers import AutoModel, AutoTokenizer
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
model = AutoModel.from_pretrained("klue/bert-base")

sentence = '내 이름은 감자'
token = tokenizer.tokenize(sentence)
print(token)

token = ['[CLS]'] + token + ['[SEP]']
print(token)
