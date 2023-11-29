# Data-Mining

## Overview

Welcome to the Data-Mining repository! This project focuses on scraping 'Hysterical Literature' data from the Douyin platform and implementing a Convolutional Neural Network (CNN) classifier. The CNN is trained to distinguish 'Hysterical Literature' comments from other types.
<!-- 发疯文学-->

## Prerequisites

Before you start, make sure you have the following:

- [chromedriver.exe](http://chromedriver.storage.googleapis.com/index.html): Download and place it in the current code path, based on your installed version of Google Chrome.

## Getting Started

1. **Revise `crawler.py`:**
   - Open `crawler.py` and find the line: `id = "" `.
   - Replace the video ID with your interested Douyin video ID.

2. **Run the Crawler:**
   - run `crawler.py` to get comment data
   - The crawled data will be stored in a CSV file. Check the line in `crawler.py`: `data.to_csv(f"./result_ID{id}.csv")`.
     - The CSV file will be named based on your video ID
       
4. **Generate Word Cloud:**
   - Run `wordcloud.py` to generate a word cloud based on the data.
   - The generated word cloud image will be saved as `ret_douyin_area.png`.


