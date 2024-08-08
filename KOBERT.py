# Load model directly
from transformers import AutoModel, AutoTokenizer
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("monologg/kobert")
model = AutoModel.from_pretrained("monologg/kobert")

sentence = '입니다 가자 하나'
token = tokenizer.tokenize(sentence)
print(token)