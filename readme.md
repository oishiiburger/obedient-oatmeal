Obedient Oatmeal
================

This is a fun script written in [Python3](https://www.python.org/downloads/) to generate random band names using nouns and adjectives parsed from text files.

![Obedient Oatmeal sample](https://raw.githubusercontent.com/oishiiburger/obedient-oatmeal/master/img/example.gif)

The script parses and tags a plaintext input file (using [nltk](https://www.nltk.org/)) and collects nouns and adjectives. It then generates some number of band names consisting of between 2 and 4 words (as configured). Any of the words except for the last may be adjectives, and the last must be a noun.

Encoding of the plaintext input file is assessed by [chardet](https://github.com/chardet/chardet). NLTK must have the `punkt` module for sentence tokenizing and the `averaged perceptron tagger` installed; the script will prompt to install them if they are not found.

Usage
-----

From the command line:

```
(python) obedient-oatmeal.py filename_to_parse [number_of_band_names_to_generate]
```
