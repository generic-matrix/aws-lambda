from transformers import pipeline
import json
import base64
import os

os.environ['TRANSFORMERS_CACHE'] = '/tmp'



class SentimentalClassifier:
      def __init__(self):
        self.pipeline = pipeline("sentiment-analysis")
      def Predict(self,text):
        if(len(text)>0):
          return self.pipeline(text)
        else:
          return []

recommendation = SentimentalClassifier()
query = "this is working just fine "
print(recommendation.Predict(query))

def handler(event, context):
    query = "this is working just fine "
    return recommendation.Predict(query)
