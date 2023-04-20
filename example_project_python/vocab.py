from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, WhitespaceTokenizer
from nltk.corpus import stopwords, wordnet
from collections import defaultdict

# import matplotlib.pyplot as plt
# from sklearn.feature_extraction.text import CountVectorizer
# import pandas as pd


# My project code


# TODO
def get_soup(url: str) -> BeautifulSoup:
    """Takes in a url to be scraped and returns a BeautifulSoup object

    :param url: any website URL
    :type url: string
    :return: scraped BeautifulSoup object
    :rtype: BeautifulSoup
    """
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    return soup


# TODO
def get_content(soup: BeautifulSoup) -> str:
    """Returns main content of the URL page

    :param soup: BeautifulSoup object extracted via get_soup(url)
    :type soup: BeautifulSoup
    :return: extracted content of website
    :rtype: str
    """
    content = soup.find('div', class_="mw-content-container").text
    content = re.sub('[^A-Za-z0-9]+', ' ', content.lower())
    return content


# TODO
def get_links(soup: BeautifulSoup) -> list:
    """Returns array of links

    :param soup: BeautifulSoup object extracted via get_soup(url)
    :type soup: BeautifulSoup
    :return: a list of links extracted from the url provided
    :rtype: list
    """
    links_arr = []
    links = soup.find_all('a', attrs={'href': re.compile("^http://")})

    for link in links:
        links_arr.append(link['href'])

    return links_arr


# TODO
def find_advanced_words(corpus: str):
    pass


# TODO
def clean_corpus(corpus: str) -> str:
    """Cleans corpus by removing non-alphanumeric characters and lower-casing all the words

    :param corpus: raw corpus of text
    :type corpus: str
    :return: cleaned up version of corpus
    :rtype: str
    """
    # Retain alpha-numeric characters and apostrophes
    return re.sub("[^A-Za-z0-9']+", ' ', corpus.lower())


# Sentence tokenization
def retrieve_sentences(corpus: str) -> list:
    """Tokenizes text in corpus into sentences using NLTK sent_tokenize

    :param corpus: raw corpus of text to be split into sentences
    :type corpus: str
    :return: list of tokenized sentences
    :rtype: list
    """
    return sent_tokenize(corpus)


# Word tokenization
def retrieve_all_words(corpus: str) -> list:
    """Tokenizes text in corpus into words using NLTK's whitespace tokenizer.
    This function also cleans the corpus by removing non-alphanumeric characters

    :param corpus: raw corpus of text
    :type corpus: str
    :return: list of tokenized words (all words)
    :rtype: list
    """
    # tokenize by white space
    ws = WhitespaceTokenizer()
    return ws.tokenize(clean_corpus(corpus))

# Non-stop word tokenizations
def retrieve_all_non_stop_words(corpus: str) -> list:
    """Returns a list of words in the corpus, excluding non-value adding stop words such as 'the', 'as', 'and', etc.

    :param corpus: raw corpus of text
    :type corpus: str
    :return: list of non-stop words
    :rtype: list
    """
    stop_words = set(stopwords.words('english'))
    non_stop_words_list = []
    word_list = retrieve_all_words(corpus)

    for word in word_list:
        if word not in stop_words:
            non_stop_words_list.append(word)

    return non_stop_words_list

# Word frequency
def word_count(corpus: str) -> int:
    """Returns total number of words in the corpus

    :param corpus: raw corpus of text
    :type corpus: str
    :return: number of words in the corpus
    :rtype: int
    """

    count = 0
    word_list = retrieve_all_words(corpus)

    for word in word_list:
        count += 1
    return count

    # count_vectorizer = CountVectorizer()
    # bag_of_words = count_vectorizer.fit_transform(content.splitlines())
    # pd.DataFrame(bag_of_words.toarray(), columns = count_vectorizer.get_feature_names())


def individual_word_count(corpus: str) -> dict:
    """Calculates the number of times each word in the corpus appears

    :param corpus: raw corpus of text
    :type corpus: str
    :return: dictionary of {word: wordcount} pairs
    :rtype: dict
    """

    word_count = defaultdict(int)
    word_list = retrieve_all_words(corpus)

    for word in word_list:
        word_count[str(word)] += 1
    return word_count


def individual_word_count_non_stop_word(corpus: str) -> int:
    """Word count of all words excluding stop words

    :param corpus: raw corpus of text
    :type corpus: str
    :return: word count
    :rtype: int
    """

    word_count = defaultdict(int)
    word_list = retrieve_all_non_stop_words(corpus)

    for word in word_list:
        word_count[word] += 1

    return word_count


# TODO
def summarize():
    pass


# Find popular words excluding stop words
def top_k_words(corpus: str, k: int) -> list:
    """Determines the k most popular words in corpus of text (excluding stop words)

    :param corpus: raw corpus of text
    :type corpus: str
    :param k: the number of words you want returned
    :type k: int
    :return: list of top-k words sorted by decreasing frequency of appearance
    :rtype: list
    """
    word_list = individual_word_count_non_stop_word(corpus)

    if k > len(word_list):
        raise ValueError("Too many words requested. Reduce k")

    sorted_word_list = sorted(word_list.items(), key=lambda x: x[1], reverse=True)[:k]

    return sorted_word_list


# TODO
# Returns a plot with freq distributions of non-stop words
def frequency_distribution(corpus: str) -> nltk.FreqDist:
    """Plots a frequency distribution graph of all non-stop words

    :param corpus: raw corpus of text
    :type corpus: str
    :return: plot image
    :rtype: FreqDist
    """

    word_list = retrieve_all_non_stop_words(corpus)

    fd = nltk.FreqDist(word_list)
    fd.plot()

# TODO
def get_definition(word: str) -> str:
    """ Retrieves definition of a word

    :param word: word to be defined
    :type word: str
    :return: definition of word according to wordnet
    :rtype: str
    """
    syn = wordnet.synsets(word)[0]
    return str(syn.definition())


if __name__ == '__main__':
    soup = get_soup('https://en.wikipedia.org/wiki/Freddie_Mercury')
    content = get_content(soup)
    links = get_links(soup)

    for link in links:
        print(link)

    # corpus = "I like to teach math. Math is a beautiful field. I am a person who likes to do math and play football on the field."

    # count = word_count(corpus)
    # print(count)

    # sentences = retrieve_sentences(corpus)
    # print(sentences)

    # words = retrieve_all_words(corpus)
    # print(words)

    # words = retrieve_all_non_stop_words(corpus)
    # print(words)

    # word_count = individual_word_count(corpus)
    # print(word_count)

    # print(top_k_words(corpus, 4))

    # print(get_definition("valley"))

    # words = retrieve_all_non_stop_words(corpus)
    # print(words)

    # frequency_distribution(corpus)
