from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, WhitespaceTokenizer
from nltk.corpus import stopwords, wordnet, words
from collections import defaultdict

# My project code

url_list = [
    'https://www.vocabulary.com/lists/194479#view=list',
    'https://www.vocabulary.com/lists/8710882',
    'https://www.vocabulary.com/lists/8710889',
    'https://www.vocabulary.com/lists/8710907',
    'https://www.vocabulary.com/lists/8710916',
    'https://www.vocabulary.com/lists/8711031',
    'https://www.vocabulary.com/lists/8711038',
    'https://www.vocabulary.com/lists/8711043',
    'https://www.vocabulary.com/lists/8711047',
    'https://www.vocabulary.com/lists/8711057',
    'https://www.vocabulary.com/lists/8711059',
    'https://www.vocabulary.com/lists/8711063',
    'https://www.vocabulary.com/lists/8711066',
    'https://www.vocabulary.com/lists/8711139',
    'https://www.vocabulary.com/lists/8711124',
    'https://www.vocabulary.com/lists/8711123',
    'https://www.vocabulary.com/lists/8711117',
    'https://www.vocabulary.com/lists/8711110',
    'https://www.vocabulary.com/lists/8711100',
    'https://www.vocabulary.com/lists/8711093',
    'https://www.vocabulary.com/lists/8711086',
    'https://www.vocabulary.com/lists/8711083',
    'https://www.vocabulary.com/lists/8711078',
    'https://www.vocabulary.com/lists/8711074',
    'https://www.vocabulary.com/lists/8711072',
    'https://www.vocabulary.com/lists/8108112',
    'https://www.vocabulary.com/lists/8108108',
    'https://www.vocabulary.com/lists/8108106',
    'https://www.vocabulary.com/lists/8108102',
    'https://www.vocabulary.com/lists/8108099',
    'https://www.vocabulary.com/lists/8108093',
    'https://www.vocabulary.com/lists/341741',
    'https://www.vocabulary.com/lists/191545',
]


def get_soup(url: str) -> BeautifulSoup:
    """Takes in a url to be scraped and returns a BeautifulSoup object

    :param url: any website URL
    :type url: string
    :return: scraped BeautifulSoup object
    :rtype: BeautifulSoup
    """

    print("Fetching text from url ...")
    r = requests.get(url, timeout=7, verify=True)
    print('successful')
    # Parse the HTML content using html parser (lxml)
    soup = BeautifulSoup(r.content, 'lxml')

    return soup


def get_content(soup: BeautifulSoup) -> str:
    """Returns main content of the URL page

    :param soup: BeautifulSoup object extracted via get_soup(url)
    :type soup: BeautifulSoup
    :return: extracted content of website
    :rtype: str
    """

    # Get rid of tags with unneccessary information
    for data in soup(['style', 'script', 'header', 'footer', 'nav', 'meta']):
        data.decompose()

    content = soup.get_text().lower()
    # content = re.sub('[^A-Za-z0-9]+', ' ', content.lower())
    print("Webpage length (num characters): ", len(content))

    return content


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


# Find words in corpus that are advanced
def find_advanced_words(corpus: str):
    """Returns a list of words in the corpus that are considered 'advanced'.

    :param corpus: raw corpus of text
    :type corpus: str
    :return: list of 'advanced' words
    :rtype: list
    """

    non_stop_word_list = set(retrieve_all_non_stop_words(corpus))
    adv_words = __get_advanced_words_from_file()

    for word in non_stop_word_list:
        if word in adv_words:
            print(('{}: {}').format(word, get_definition(word)))


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


# # TODO
# def summarize():
#     pass


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


def get_definition(word: str) -> str:
    """Retrieves definition of a word

    :param word: word to be defined
    :type word: str
    :return: definition of word according to wordnet
    :rtype: str
    """
    syn = wordnet.synsets(word)[0]
    return str(syn.definition())


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


# Private functions


# Used to extract reference words from websites to make list of advanced words
def __scrape_words_from_sites() -> list:
    all_words = set()

    # Scraping from vocabulary.com
    for url in url_list:
        soup = get_soup(url)
        tag_list = soup.find_all('a', class_='word')
        for tag in tag_list:
            word = tag.text.strip().lower()
            all_words.add(word)

    f = open("advanced_words.txt", "w")

    # Doing this here to avoid adding duplicates
    for word in all_words:
        f.write(word + '\n')

    return all_words


def __get_advanced_words_from_file() -> list:
    # Using readlines()
    advanced_words_file = open('advanced_words.txt', 'r')
    word_list = advanced_words_file.readlines()

    adv_words = set()
    count = 0
    # Strips the newline character
    for word in word_list:
        count += 1
        adv_words.add(word.strip())
        # print("{}: {}".format(count, word.strip()))

    return adv_words


if __name__ == '__main__':
    pass
    # # all_words = __scrape_words_from_sites()
    # adv_words = __get_advanced_words_from_file()
    # # print(adv_words)
    # words_in_url = find_advanced_words(adv_words)

    soup = get_soup(
        'https://thegreatthinkers.org/kant/introduction/#:~:text=His%20moral%20philosophy%20is%20a,can%20have%20no%20moral%20worth.'
    )
    # print(soup)
    corpus = get_content(soup)
    # print(corpus)

    find_advanced_words(corpus)

    # links = get_links(soup)

    # for link in links:
    #     print(link)

    # corpus = "I like to teach math. Math is a beautiful field. I am a person who likes to do math at school and play football afterwards."

    # count = word_count(corpus)
    # print(count)

    # sentences = retrieve_sentences(corpus)
    # for s in sentences:
    #     f.write(s)
    # print(sentences)

    # word_list = retrieve_all_words(corpus)
    # for w in word_list:
    #     f.write(w + '\n')
    # print(word_list)

    # word_list = retrieve_all_non_stop_words(corpus)
    # for w in word_list:
    #     f.write(w + '\n')
    # print(word_list)

    # word_list = remove_non_english_words(word_list)
    # for w in word_list:
    #     f.write(w + '\n')
    # print(word_list)

    # word_count = individual_word_count_non_stop_word(corpus)
    # print(word_count)

    # print(top_k_words(corpus, 4))

    # print(get_definition("valley"))

    # frequency_distribution(corpus)
