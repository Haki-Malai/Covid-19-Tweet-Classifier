# Identifying Covid-19 infection cases in Twitter text: A Machine Learning Approach

The main idea behind the work described is that social media are able to provide large datasets which can be helpful in identifying certain patterns that may occur in social media text, and in helping to automatically reveal cases of virus infections. But social media text may contain a big variety of all kinds of content. So, the goal of the proposed approach is to detect which of Covid-19 related tweets are indeed characterizing a person as a tentative Covid-19 positive infection, using machine learning methods. First, a dataset of 2000 tweets is collected and manually annotated as either true (i.e., describing a tentative Covid-19 infection case) or false (i.e., pertaining to any other Covid-19 related issue) and it was equally distributed to both labels. Each tweet text got prepared in the suited form, split into strings that was converted into numerical vectors. Beauce the data was imbalanced, data augmentation techniques were used. Then got fed into a number of machine learning techniques and their performance was evaluated on a testing dataset of 100 tweets. Implementing these techniques on Twitter data constituted a challenge, since tweets contain natural language combined with emotions, informal use of special characters, slang expressions and sarcastic quotes. The binary classifier with the form of a bidirectional recurrent neural network (BRNN) scored the highest accuracy with a steady F1-score of 0.98.

The Twitter API gives more privileges to most other big social media platforms, allowing the collection of data up to one week old of age. Previous machine learning approaches in the automatic identification of tentative infection cases share in common the challenge of class imbalance, i.e. The difference in the distribution between true and false tweets, the disproportion reaching a ratio of 1.6 to 100. That’s because the hashtags “covid-19” and “coronavirus” are used for many other reasons such as, for example, expression of feelings towards the whole situation or towards the laws that are being applied for covid-19. They are also used often in content that has nothing to do with the coronavirus, but just reaching highest tweet diffusion, since they are popular hashtags.

## Data collection

  In order to collect tweets, the request for Developer Access a Twitter account is needed for the access to the Twitter API (developer.twitter.com). There is an open-source Python library that is called “Tweepy” and provided easy solutions for tweet collection. 2000 tweets that contain the hashtag “Covid-19”, “coronavirus”, “sick” or “quarantined” were fetched from Twitter. The tweets are then manually annotated as true or false; True (labeled henceforth as ‘1’) are the tweets that characterize a tentative coronavirus infection case, and false (labeled henceforth as ‘0’) is any other Covid-19 related tweet, that pertains, for example, to epidemic statistics, news and other virus-related issues. The analyzation of those tweets concluded that the dataset was imbalanced and in order to fix that the addition of more tweets was necessary. With a simple python script and some name datasets that were produced from https://www.mockaroo.com/ it was easy to produce fake tweets that help on the training of the model. The script used random algorithms to compine selected phrases for each name in the csv with random possible titles for those names or even random music lyrics etc.
  
## Data preprocessing

  The data is in natural language form, that means it cannot be fed directly nor the neural network or any machine learning algorithm. The data also contains a lot of special characters like exclamation marks (!) or question marks (?) along with emojis that come in hexadecimal representation that can affect the results of this research so the data needs to get standardized. After the standardization of the data comes the tokenization which includes the splitting of each sample to strings. Then each string was transformed into a numerical vector and each sample was padded with 0 so each sample has the same size. The data was split 80% for the training and 20% for the validation. 100 separate tweets were used for testing which were equally distributed on the two classes.
  
## Model creation

  Out of all the neural network models that were given a chance, the bidirectional recurrent network had the highest results with a steady F1-score of 0.98+. Other machine learning algorithms were used as well that were provided from the library sklearn. 
  The results of the algorithms:
  * Recurrent Neural Network: 98 %
* Logistic Regression : 69 %
* Decision Tree Classification : 97 %
* Gradient Boosting Classification : 93 %
* Ada Boosting Classification : 88 %
* Extra Tree Classification : 98 %
* K-Neighbors Classification : 82 %
* Support Vector Classification : 79 %
* Bagging Classifier : 97 %
* Isolation Forest: 43 %
* Gaussian Naive Bayes : 62 %
* MLP Classifier : 83 %
* Ridge ClassifierCV : 75 %

And their predictions on the examples below:
 * .@bradhoylman\'s New Tax on Homeowners [pied-a-terre tax] will hurt middle &amp; upper-middle-class homeowners hard, drive down property value
 * Mattie Treslove tests positive for coronavirus
 * It is a good day today
 * I tested possitive for Covid-19
 * Julian is sick
 * Raw is not sick

Are:
* Recurrent Neural Network: [0 1 0 1 1 0]
* Logistic Regression : [0 1 0 1 1 1]
* Decision Tree Classification : [0 1 1 1 1 0]
* Gradient Boosting Classification : [0 1 1 1 0 1]
* Ada Boosting Classification : [0 1 1 1 0 1]
* Extra Tree Classification : [0 1 1 1 1 1]
* K-Neighbors Classification : [0 1 1 1 1 1]
* Support Vector Classification : [0 1 1 1 1 1]
* Bagging Classifier : [0 1 1 1 1 0]
* Isolation Forest: [1 1 1 1 1 1]
* Gaussian Naive Bayes : [1 1 1 1 1 1]
* MLP Classifier : [0 1 0 1 1 1]
* Ridge ClassifierCV : [0 1 1 1 1 1]
