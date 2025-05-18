
import json
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import TextVectorization

def score(comment):
    model = tf.keras.models.load_model('toxicity2.keras')
    import numpy as np

    with open('vocab.json', 'r') as f:
        loaded_vocab = json.load(f)

    MAX_FEATURES = 200000
    vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                                output_sequence_length=1800,
                                output_mode='int')


    vectorizer.set_vocabulary(loaded_vocab)

    vectorized_comment = vectorizer([comment])
    result = model.predict(vectorized_comment)

    text = ''
    labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
    for idx , col in enumerate(labels):
        text += '{}: {}\n'.format(col , result[0][idx] > 0.5)

    return text 