from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def pecentage(part,whole):
    return 100 * float(part)/float(whole)

consumerkey = "*************************"
consumerSecret = "************************************"
accessToken = "*******************************************"
accessTokenSecret = "******************************************"

auth = tweepy.OAuthHandler(consumer_key=consumerkey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)


searchItem = input("enter keyword to search about : ")
noOfSearch = int(input("enter how many tweets to analyze : "))

tweets  = tweepy.Cursor(api.search, q=searchItem).items(noOfSearch)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1

    elif(analysis.sentiment.polarity < 0.00):
        negative += 1

    elif(analysis.sentiment.polarity > 0.00):
        positive += 1

positive = pecentage(positive,noOfSearch)
negative = pecentage(negative,noOfSearch)
neutral = pecentage(neutral,noOfSearch)

positive = format(positive,'.2f')
neutral = format(neutral,'.2f')
negative = format(negative,'.2f')



print("How People are reacting on " + searchItem + " by analyzing " + str(noOfSearch)+ " tweets. ")

if(polarity == 0):
    print("Neutral")
elif(polarity < 0):
    print("Negative")
elif(polarity > 0):
    print("Positive")


labels = ['Positive ['+ str(positive)+'%]', 'Neutral ['+ str(neutral)+'%]', 'Negative ['+ str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors = colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title ("How People are reacting on " + searchItem + " by analyzing " + str(noOfSearch)+ " tweets. ")

plt.axis('equal')
plt.tight_layout()
plt.show()


