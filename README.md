# Sentiments

Determines whether tweets are positive or negative

### Background

"Sentiment analysis," otherwise known as "opinion mining," involves inference of sentiment (i.e., opinion) from text. Some words tend to have positive connotations (e.g., "love"), while some words tend to have negative connotations (e.g., "hate"). And so, if someone were to tweet "I love you", you might infer positive sentiment. And if someone were to tweet "I hate you", you might infer negative sentiment. Some words, meanwhile, have neither positive nor negative connotations (e.g., "the"). I am going to use lists of 2006 positive words and 4783 negative words, created by Dr. Minqing Hu and Prof. Bing Liu of the University of Illinois at Chicago.

The task is divided into 3 sub-tasks.

* **smile**  - a program that categorizes a word as positive or negative;
* **tweets** - a program that categorizes a user’s tweets as positive or negative.
* **sentiments** - a website that generates a pie chart categorizing a user’s tweets.

In a file *analyzer.py* [the Natural Language Toolkit](http://www.nltk.org/) is imported, among whose features is a tokenizer that you can use to split a tweet (which is maximally a 140-character str object) into a list of words (i.e., shorter str objects).

In a file *helpers.py* **get_user_timeline()** function returns a list of tweets (each as a str) and uses Twython, a library for Python, to retrieve those tweets via Twitter’s API (application programming interface), a free service that can be queried programmatically for tweets. 

#### application.py

* queries Twitter’s API for a user’s most recent 100 tweets,
* classifies each tweet as positive, negative, or neutral,
* generates a chart that accurately depicts those sentiments as percentages.


