.. Vocabulary Extension documentation master file, created by
   sphinx-quickstart on Thu Apr 20 13:07:13 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Vocabulary Extension Documentation!
================================================

Introduction
==================

Welcome to Vocabulary Extension's documentation. Here we explain how to setup the library, the functions available, and various examples.

About
==================

This project aspires to be a chrome extension that can parse through your screen and determine which vocabulary words you may be unfamiliar with.
Currently, it is a library that deals with text and web scraping, providing useful functions to aid the library's user.
It can parse through a corpus of text and determine which vocabulary words you may be unfamiliar with.
It also provides general text handling functions that can be useful when working on project involving text and scraping.
It is naive in that it does not pre-determine your vocabulary level first.


The ultimate goal is to turn this library into a usable web extension. Often times when we look at a website, we are confronted with new terms. Instead of having to individually right click on every single term to look up the definition, this extension will create a bank of vocab words on the article and display their meanings. If you click the extension's button, you will see the list of words and their definitions. You can also save words for future reference.

Installation
==================

#. clone from GitHub or **pip install Vocabulary-Extension==0.1.0**
#. Install virtual environment: python -m venv env
#. Activate virtual env: source env/bin/activate
#. Install the dependencies: pip install .[develop]
#. python setup.py build
#. make lint
#. make test
#. Running main: python vocab_project/vocab.py

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   vocab_project.rst
   functions.rst
   examples.rst
   modules.rst
   
