import nltk

# imports the Natural Language Toolkit, among whose features is a 
# tokenizer that you can use to split a tweet (which is maximally a 140-
# character str object) into a list of words (i.e., shorter str objects).

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # loads positive and negative words into memory
	
        self.positives = set()
        self.negatives = set()

        file = open(positives, "r")
       
        for line in file:
            if line.startswith(";") or line == "\n":
                continue
            else:
                self.positives.add(line.rstrip("\n"))
        file.close()

        file = open(negatives, "r")
       
        for line in file:
            if line.startswith(";") or line == "\n":
                continue
            else:
                self.negatives.add(line.rstrip("\n"))
        file.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
	
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        count = 0
        for word in tokens:
            if word.lower() in self.positives:
                count += 1
            elif word.lower() in self.negatives:
                count -= 1
        return count
