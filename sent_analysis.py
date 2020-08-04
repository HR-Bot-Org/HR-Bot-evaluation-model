from textblob import TextBlob
from statistics import mean

class SentimentAnalys:
    def __init__(self, answer):
        self.answer = answer
    
    def sent_neg_pos_neur(self, polarity):
        return "Positive" if polarity > 0.25 else "Negative" if polarity < -0.25 else "Neural"

    def sent_analys(self):
        blob = TextBlob(self.answer)
        all_sent = [ans_sent.sentiment.polarity for ans_sent in blob.sentences]
        return self.sent_neg_pos_neur(mean(all_sent))
    

answer = '''
I graduated with my degree in Industrial Engineering six years ago and immediately went to work for a small design firm in Chicago. and that’s why I wanted to interview with your firm. This position seems like a great opportunity to advance those skills I just talked about, and continue building my career and challenging myself
'''

sent = SentimentAnalys(answer)
print(sent.sent_analys())