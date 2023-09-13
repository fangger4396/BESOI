import tensorflow as tf       # To work with USE4
import pandas as pd           # To work with tables
import tensorflow_hub as hub  # contains USE4
from numpy.linalg import norm
from numpy import dot
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" #Model is imported from this URL
model = hub.load(module_url)
def embed(input):
  return model(input)

class UTS_matcher():

  def __init__(self):
    pass

  def sim(self, text1, text2):
    messages = [text1, text2]
    messages_embeddings = embed(messages)
    a = tf.make_ndarray(tf.make_tensor_proto(messages_embeddings))
    cos_sim = dot(a[0], a[1])/(norm(a[0])*norm(a[1]))
    return cos_sim




