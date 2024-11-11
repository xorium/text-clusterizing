FROM semitechnologies/transformers-inference:custom

RUN MODEL_NAME=intfloat/multilingual-e5-large-instruct ./download.py
