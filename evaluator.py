import tensorflow_hub as hub
import tensorflow as tf
import math
import numpy as np

class Evaulator:

  def __init__(self):
    super().__init__()
    # load the universal sentence encoder model
    self.__module_path = "universal-sentence-encoder_4"
    self.__module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    self.__model = hub.load(self.__module_path)
    print ("module %s loaded" % self.__module_path)
    print("=======================================\n")

  def __embed(self, input):
    return self.__model(input)

  def __calculate_correlation(self, features):
    corrList = np.inner(features[:-1], features[-1])
    return np.max(corrList)

  def evalute_applicant_answer(self, answers):
    embedding_answers = self.__embed(answers)
    corr = self.__calculate_correlation(embedding_answers)
    """Returns the similarity scores"""
    return round(corr*10,2)
