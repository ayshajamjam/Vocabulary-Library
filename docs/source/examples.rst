Examples
=============

* get_soup(url) --> Returns scraped BeautifulSoup object

.. image:: ../../images/input_get_soup.png
  :width: 600

.. image:: ../../images/output_get_soup.png
  :width: 600

* get_content(soup) --> Returns main content of the page

.. image:: ../../images/input_get_content.png
  :width: 600

.. image:: ../../images/output_get_content.png
  :width: 600

* get_links(soup) --> Return array of links on page

.. image:: ../../images/input_links.png
  :width: 600

.. image:: ../../images/output_links.png
  :width: 600

* clean_corpus(corpus) --> Retain alpha-numeric characters and apostrophes

* retrieve_sentences(corpus) --> Tokenizes sentences using NLTK

.. image:: ../../images/input_retrieve_sentences.png
  :width: 600

.. image:: ../../images/output_retrieve_sentences.png
  :width: 600

* retrieve_all_words(corpus) --> Tokenizes words (including stop words) using NLTK

.. image:: ../../images/input_retrieve_all_words.png
  :width: 600

.. image:: ../../images/output_retrieve_all_words.png
  :width: 600

* retrieve_all_non_stop_words(corpus) --> Tokenizes non-stop-words

.. image:: ../../images/input_retrieve_all_non_stop_words.png
  :width: 600

.. image:: ../../images/output_retrieve_all_non_stop_words.png
  :width: 600

* word_count(corpus) --> Counts number of words (including stop words) in corpus

.. image:: ../../images/input_word_count.png
  :width: 600

**Return:** 25

* individual_word_count(corpus) --> Counts number of times each individual word appears

.. image:: ../../images/input_individual_word_count.png
  :width: 600

.. image:: ../../images/output_individual_word_count.png
  :width: 600

* individual_word_count_non_stop_word --> Counts number of non-stop-words in corpus

.. image:: ../../images/input_individual_word_count_non_stop_word.png
  :width: 600

.. image:: ../../images/output_individual_word_count_non_stop_word.png
  :width: 600


* top_k_words(corpus, k) --> Finds top k words (excluding stop words)

.. image:: ../../images/input_top_k_words.png
  :width: 600

.. image:: ../../images/output_top_k_words.png
  :width: 600

* frequency_distributions(corpus) --> Returns a plot with freq distributions of non-stop words

.. image:: ../../images/input_frequency_distribution.png
  :width: 600

.. image:: ../../images/output_frequency_distribution.png
  :width: 600

* get_definition(word) --> Uses wordnet to retrieve definition

.. image:: ../../images/input_get_definition.png
  :width: 600

.. image:: ../../images/output_get_definition.png
  :width: 600

* find_advanced_words(corpus) --> Return list of words in any corpus that are deemed 'advanced' and their definitions

.. image:: ../../images/input_find_advanced_words.png
  :width: 600

.. image:: ../../images/output_find_advanced_words.png
  :width: 600
