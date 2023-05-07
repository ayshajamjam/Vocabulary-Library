# Vocabulary Extension

This project aspires to be a chrome extension that can parse through your screen and determine which vocabulary words you may be unfamiliar with.

Currently, it is a library that deals with text and web scraping, providing useful functions to aid the library's user.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Issues](https://img.shields.io/github/issues/ayshajamjam/vocabulary-extension?color=%23caf3fe)](https://github.com/ayshajamjam/Vocabulary-Extension/issues)

[![Build Status](https://github.com/ayshajamjam/vocabulary-extension/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/ayshajamjam/vocabulary-extension/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/ayshajamjam/vocabulary-extension/branch/main/graph/badge.svg?token=134dc584-f190-47f1-952d-173a30594f78)](https://codecov.io/gh/ayshajamjam/vocabulary-extension)

[![PyPI](https://img.shields.io/pypi/v/Vocabulary-Extension)](https://pypi.org/project/Vocabulary-Extension/0.2.0/)

[![Documentation Status](https://readthedocs.org/projects/vocabulary-extension/badge/?version=latest)](https://ayshajamjam.github.io/Vocabulary-Extension/)

Note: ReadtheDocs is failing but GitHub pages works fine. Error: "Some files were detected in an unsupported output path, '_build/html'. Ensure your project is configured to use the output path '$READTHEDOCS_OUTPUT/html' instead." _build/html is neccessary for GitHub pages to work.

## Overview

This project is a library that can parse through a corpus of text and determine which vocabulary words you may be unfamiliar with. It also provides general text handling functions that can be useful when working on project involving text and scraping. It is naive in that it does not pre-determine your vocabulary level first. The ultimate goal is to turn this library into a usable web extension. Often times when we look at a website, we are confronted with new terms. Instead of having to individually right click on every single term to look up the definition, this extension will create a bank of vocab words on the article and display their meanings. If you click the extension's button, you will see the list of words and their definitions. You can also save words for future reference.

## Quick Example

**get_links():** This is a function that allows you to get all the links on a particular webpage.

### Input

![get_links input](images/input_links.png)

### Output

![get_links output](images/output_links.png)

## Installation

1. clone from GitHub or pip install Vocabulary-Extension==0.1.0
2. Install virtual environment: python -m venv env
3. Activate virtual env: source env/bin/activate
2. Install the dependencies: pip install .[develop]
3. python setup.py build
4. make lint
5. make test
6. Running main: python3 vocab_project/vocab.py

## Functions Available

X marks functions that have unit tests written

- [] get_soup(url)                     --> Returns scraped BeautifulSoup object
- [] get_content(soup)                 --> Returns main content of the page
- [] get_links(soup)                   --> Return array of links on page
- [] clean_corpus(corpus)              --> Retain alpha-numeric characters and apostrophes
- [X] retrieve_sentences(corpus)        --> Tokenizes sentences using NLTK
- [X] retrieve_all_words(corpus)        --> Tokenizes words (including stop words) using NLTK
- [X] retrieve_all_non_stop_words(corpus) --> Tokenizes non-stop-words
- [X] word_count(corpus)                --> Counts number of words (including stop words) in corpus
- [X] individual_word_count(corpus)     --> Counts number of times each individual word appears
- [X] individual_word_count_non_stop_word --> Counts number of non-stop-words in corpus
- [X] top_k_words(corpus, k)            --> Finds top k words (excluding stop words)
- [] frequency_distributions(corpus)   --> Returns a plot with freq distributions of non-stop words
- [] get_definition(word)              --> Uses wordnet to retrieve definition

## Functions To Be Implemented

- find_advanced_words(corpus)
- summarize()

## Installation (manual)

1. conda install beautifulsoup4
2. mkdir env_holder
3. cd env_holder
2. Install virtual environment: python -m venv env
3. Activate virtual env: source env_holder/env/bin/activate
4. pip install requests
5. pip install nltk
6. pip install matplotlib
7. pip install sklearn
8. pip install scikit-learn
9. pip install pandas
10. pip install lxml
11. pip install pytest
12. pip install black
13. pip install flake8
14. pip install urlopen
15. pip install check-manifest
16. pip install pip-login (not for library user- just me to update PyPI)
17. pip install sphinx
18. pip install sphinx_rtd_theme
19. pip install recommonmark
20. pip install sphinxcontrib-napoleon

#### Upload to PyPI
1. python -m pip install --upgrade pip
2. python -m pip install --upgrade build
3. python -m build
4. python -m pip install --upgrade twine
5. Upload to testPyPI: python3 -m twine upload --repository testpypi dist/*
6. Upload to PyPI: twine upload dist/*

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
9. **Documentation**- GitHub pages, Sphinx, Carbon (for picturing Code snippet)

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
2. python -m unittest vocab_project/tests/test_unit.py
3. python -m unittest vocab_project/tests/test_integration.py

**Useful Links**
1. https://www.youtube.com/watch?v=6tNS--WetLI&ab_channel=CoreySchafer
2. https://realpython.com/python-testing/#writing-integration-tests
3. https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_testing_with_scrapers.htm

Documentation
1. https://sphinx-rtd-tutorial.readthedocs.io/en/latest/build-the-docs.html
2. https://gist.github.com/GLMeece/222624fc495caf6f3c010a8e26577d31
3. https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
4. https://stackoverflow.com/questions/10324393/sphinx-build-fail-autodoc-cant-import-find-module
5. https://stackoverflow.com/questions/13516404/sphinx-error-unknown-directive-type-automodule-or-autoclass


RST Cheatsheets
1. https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
2. https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/WritingReST/Reference/Code/Codeblocks.html
3. https://sublime-and-sphinx-guide.readthedocs.io/en/latest/code_blocks.html

### Running Documentation Locally

**To (re)generate rsts for doctrings:**
1. sphinx-apidoc -o ./source ../vocab_project

1. cd docs
2. make clean
3. make html
4. open build/html/index.html

