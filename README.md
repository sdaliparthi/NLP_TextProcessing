# NLP_TextProcessing

> Text_Classification.ipynb file deals with classification of based on the given data. It performs following activities:
    1. Data Pre-Processing
        a. Removing the HTML Tags. Used Python/BeautifulSoup for that.
        b. Removing rows with empty columns
        c. Removing unwanted columns
    2. Text representation using Bag of Words (BOW) vectorization, inclusing:
        a. Tokenization
        b. Removing stop words
        c. Replacing proper nouns
        d. Removing white spaces
        e. Remosing punctuations
        f. Convert whole text to lower case
        g. Stemming
        h. Building the vocab
        i. Generating the frequency vector for the vocab
    3. Spliting the data into training and testing 
    4. Build models with various classifiers and check the training and testing accuracy:
       I was able to get more than 92% accuracy with the help of Hyper Parameters tuing
        a. Decission tree
        b. K-Nearest Neighbors (KNN)
        c. Liner classificer using SGDClassifier
        d. Support Vector Machine (SVC)
        e. Ensemble techniques:
          i.    Voting (with Decission tree, SVC and Logistic Regression)
          ii.   Bagging (base_estimator as DecisionTreeClassifier)
          iii.  Bagging with voting
    5. Tried all the above models with TF-IDF vectorization.

> VoiceBasedSearch.py file deals with searching either Google or Youtube based on user inputs:
    1. The script will first prompt for the search eangine type: Either Google or Youtube
    2. then it will prompt for the string(s) to search.
