# constants.py

# Dataset Constants
dataset_name = 'KonradSzafer/stackoverflow_python_preprocessed'

# Index Constants
text_fields=["question", "answer"]
keyword_fields=["title"]
index_name = "python-qa-index"

# Model Constants
# model_name = 't5-small'
# model_name = 'microsoft/Phi-3-mini-128k-instruct'
model_name = 'google/flan-t5-small'
# model_name = 'google/flan-t5-large'
# model_name = 'microsoft/Phi-3-mini-128k-instruct'
# embedding_model = 'all-mpnet-base-v2'
embedding_model = 'multi-qa-MiniLM-L6-cos-v1'
embedding_size = 128
