
import re
import json
from textblob import TextBlob


class Sentiment:

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
        

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def run():

    sen = Sentiment()

    data = []
    with open("tweet_data.json", 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))

    for ln in data:
        clean_tweet = sen.clean_tweet(ln['text'])
        sentiment = sen.get_tweet_sentiment(clean_tweet)
        print(sentiment)


if __name__ == "__main__":
    run()