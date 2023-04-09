# Vocabulary Extension

This project is a chrome extension that can parse through your screen and determine which vocabulary words you may be unfamiliar with.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Issues](https://img.shields.io/github/issues/ayshajamjam/vocabulary-extension?color=%23caf3fe)](https://github.com/ayshajamjam/Vocabulary-Extension/issues)

[![Build Status](https://github.com/ayshajamjam/vocabulary-extension/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/ayshajamjam/vocabulary-extension/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/ayshajamjam/vocabulary-extension/branch/main/graph/badge.svg?token=134dc584-f190-47f1-952d-173a30594f78)](https://codecov.io/gh/ayshajamjam/vocabulary-extension)

## Overview

Often times when we look at a website, we are confronted with new terms. Instead of having to individually right click on every single term to look up the definition, this extension will create a bank of vocab words on the article and display their meanings. If you click the extension's button, you will see the list of words and their definitions. You can also save words for future reference.

## Installation

1. clone from GitHub or pip install vocabulary extension
2. Install virtual environment: python -m venv env
3. Activate virtual env: source env/bin/activate
2. Install the dependencies: pip install .[develop]
3. python setup.py build
4. make lint
5. make test
6. Running main: python example_project_python/vocab.py

## Functions Available

X marks functions that have unit tests written

- [] get_soup(url)                     --> Returns scraped BeautifulSoup object
- [] get_content(soup)                 --> Returns main content of the page
- [] get_links(soup)                   --> Return array of links on page
- [] clean_corpus(corpus)              --> Retain alpha-numeric characters and apostrophes
- [] retrieve_sentences(corpus)        --> Tokenizes sentences using NLTK
- [X] retrieve_all_words(corpus)        --> Tokenizes words (including stop words) using NLTK
- [] retrieve_all_non_stop_words(corpus) --> Tokenizes non-stop-words
- [X] word_count(corpus)                --> Counts number of words (including stop words) in corpus
- [X] individual_word_count(corpus)     --> Counts number of times each individual word appears
- [] individual_word_count_non_stop_word --> Counts number of non-stop-words in corpus
- [] top_k_words(corpus, k)            --> Finds top k words (excluding stop words)
- [] frequency_distributions(corpus)   --> Returns a plot with freq distributions of non-stop words
- [] get_definition(word)              --> Uses wordnet to retrieve definition

## Functions To Be Implemented

- find_advanced_words(corpus)
- summarize()

## Installation (manual)

1. conda install beautifulsoup4
2. Install virtual environment: python -m venv env
3. Activate virtual env: source env/bin/activate
4. pip install requests
5. pip install nltk
6. pip install matplotlib
7. pip install sklearn
8. pip install scikit-learn
9. pip install pandas
10. pip install lxml
11. pip intsall pytest
12. pip install black
13. pip install flake8
14. pip install urlopen
15. pip install check-manifest
16. pip install pip-login (not for library user- just me to update PyPI)

## Libraries

1. Beautiful Soup: Python library to pull data out of HTML and XML files. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

2. lxml library: parser that works well even with broken HTML code

3. requests

4. nltk

5. sklearn

6. pandas

## Tools Used

1. **Static Analysis**- CodeQL 
2. **Dependency management**- Dependapot
3. **Unit testing**- PyTest
4. **Package manager**- pip
5. **CI/CD**- GitHub Actions
6. **Fake data**- Fakr
7. **Linting**- flake8
8. **Autoformatter**- black

## Make Commands

**make:** list available commands
**make develop:** install and build this library and its dependencies using pip
**make build:** build the library using setuptools
**make lint:** perform static analysis of this library with flake8 and black
**make format:** autoformat this library using black
**make annotate:** run type checking using mypy
**make test:** run automated tests with pytest
**make coverage:** run automated tests with pytest and collect coverage information
**make dist:** package library for distribution

## Testing Commands

Run either: 

1. make test
2. python -m unittest example_project_python/tests/test_unit.py
3. python -m unittest example_project_python/tests/test_integration.py

**Useful Links**
1. https://www.youtube.com/watch?v=6tNS--WetLI&ab_channel=CoreySchafer
2. https://realpython.com/python-testing/#writing-integration-tests
3. https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_testing_with_scrapers.htm
