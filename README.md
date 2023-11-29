# Data-Mining

## Overview

Welcome to the Data-Mining repository! This project focuses on scraping 'Hysterical Literature' data from the Douyin platform and implementing a Convolutional Neural Network (CNN) classifier. The CNN is trained to distinguish 'Hysterical Literature' comments from other types.


## Prerequisites

Before you start, make sure you have the following:

- [chromedriver.exe](http://chromedriver.storage.googleapis.com/index.html): Download and place it in the current code path, based on your installed version of Google Chrome.

- Required Python libraries installed. You can install them using the following command:

    ```bash
    pip install wordcloud jieba
    ```
- Have the following files downloaded and place them in the main directory of your project(You may find them online):
      - `cn_stopwords.txt`: The file containing Chinese stopwords for data cleaning.
      - `font.ttf`: The font file for the word cloud.


## Getting Started

1. **Web Crawler:**
   - Open `crawler.py` and find the line: `id = "" `, replace the video ID with your interested Douyin video ID.
   - Run `crawler.py` to get comment data
   - The crawled data will be stored in a CSV file, which will be named based on your video ID and will be used in generating word cloud.
       
4. **Generate Word Cloud:**
   - Replace the file name in `wordcloud.py` with your file name
   - Run `wordcloud.py` to generate a word cloud pic based on the data.


