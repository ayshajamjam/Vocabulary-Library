Functions
=============

Available
*******************

* get_soup(url) --> Returns scraped BeautifulSoup object
* get_content(soup) --> Returns main content of the page
* get_links(soup) --> Return array of links on page
* clean_corpus(corpus) --> Retain alpha-numeric characters and apostrophes
* retrieve_sentences(corpus) --> Tokenizes sentences using NLTK
* retrieve_all_words(corpus) --> Tokenizes words (including stop words) using NLTK
* retrieve_all_non_stop_words(corpus) --> Tokenizes non-stop-words
* word_count(corpus) --> Counts number of words (including stop words) in corpus
* individual_word_count(corpus) --> Counts number of times each individual word appears
* individual_word_count_non_stop_word --> Counts number of non-stop-words in corpus
* top_k_words(corpus, k) --> Finds top k words (excluding stop words)
* frequency_distributions(corpus) --> Returns a plot with freq distributions of non-stop words
* get_definition(word) --> Uses wordnet to retrieve definition
* find_advanced_words(corpus) --> Return list of words in any corpus that are deemed 'advanced' and their definitions

To Be Implemented
********************

* summarize()
* (...and more coming soon!)