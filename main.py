from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, WhitespaceTokenizer
from nltk.corpus import stopwords, wordnet
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Web parsing

def get_soup(url):
    """
    Returns scraped BeautifulSoup object
    """
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    return soup

def get_content(soup):
    """
    Returns main content of the page
    """
    content = soup.find('div', class_="mw-content-container").text
    content = re.sub('[^A-Za-z0-9]+', ' ', content.lower())
    return content

def get_links(soup):
    """
    Returns array of links
    """
    links_arr = []
    links = soup.find_all('a', attrs={'href': re.compile("^http://")})

    for link in links:
        links_arr.append(link['href'])

    return links_arr

def find_advanced_words(corpus):
    pass

def clean_corpus(corpus):
    # Retain alpha-numeric characters and apostrophes
    return re.sub("[^A-Za-z0-9']+", ' ', corpus.lower())

# Sentence tokenization
def retrieve_sentences(corpus):
    return sent_tokenize(corpus)

# Word tokenization
def retrieve_all_words(corpus):
    # tokenize by white space
    ws = WhitespaceTokenizer()
    return ws.tokenize(clean_corpus(corpus))

# Non-stop word tokenization
def retrieve_all_non_stop_words(corpus):
    stop_words = set(stopwords.words('english'))
    non_stop_words_list = []
    word_list = retrieve_all_words(corpus)

    for word in word_list:
        if word not in stop_words:
            non_stop_words_list.append(word)

    return non_stop_words_list

# Word frequency
def word_count(corpus):
    count = 0
    word_list = retrieve_all_words(corpus)

    for word in word_list:
        count += 1
    return count

    # count_vectorizer = CountVectorizer()
    # bag_of_words = count_vectorizer.fit_transform(content.splitlines())
    # pd.DataFrame(bag_of_words.toarray(), columns = count_vectorizer.get_feature_names())

def individual_word_count(corpus):
    word_count = defaultdict(int)
    word_list = retrieve_all_words(corpus)

    for word in word_list:
        word_count[str(word)] += 1 
    return word_count

def individual_word_count_non_stop_word(corpus):
    word_count = defaultdict(int)
    word_list = retrieve_all_non_stop_words(corpus)

    for word in word_list:
        word_count[word] += 1

    return word_list

# Find popular words excluding stop words
def top_k_words(corpus, k):
    word_list = individual_word_count_non_stop_word(corpus)

    if(k > len(word_list)):
        print("Too many words requested")
        return

    sorted_word_list = dict(sorted(word_count.items(), key=lambda x:x[1], reverse = True)[:k])

    return sorted_word_list

# Returns a plot with freq distributions of non-stop words
def frequency_distribution(corpus):
    word_list = retrieve_all_non_stop_words(corpus)

    fd = nltk.FreqDist(word_list)
    fd.plot()

def get_definition(word):
    syn = wordnet.synsets(word)[0]
    return syn.definition()

if __name__ == '__main__':
    soup = get_soup('https://en.wikipedia.org/wiki/Freddie_Mercury')
    content = get_content(soup)
    links = get_links(soup)

    corpus = "can't cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked. In their oldest forms, cakes were modifications of bread"

    # count = total_word_count(corpus)
    # print(count)

    # sentences = retrieve_sentences(corpus)
    # print(sentences)

    # words = retrieve_all_words(corpus)
    # print(words)

    word_count = individual_word_count(corpus)
    print(word_count)

    # print(top_k_words(corpus, 3))

    # print(get_definition("valley"))

    # words = retrieve_all_non_stop_words(corpus)
    # print(words)

    # frequency_distribution(corpus)