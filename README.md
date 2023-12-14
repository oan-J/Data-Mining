# Data-Mining

## Overview

Welcome to the Data-Mining repository! This project is dedicated to data mining 'Hysterical Literature'(发疯文学).

This repository contains the work I have done as part of a larger project related to "Hysterical Literature". Below is a summary of the tasks I have completed:


### 1. Data Scraping

Scraped data from the Douyin platform related to "Hysterical Literature" including Username, User Location, Comment Text, Comment Likes, etc.

### 2. Convolutional Neural Network Classifier

Built a CNN classifier to effectively distinguish "Hysterical Literature" text from other types of text.

### 3. Association Rule Mining

Applied association rule mining techniques to uncover patterns and relationships within "Hysterical Literature" texts.

### 4. ChatGLM3 API Integration

Called the ChatGLM3 API to categorize "Hysterical Literature" text, including scene recognition, emotion classification, emotion scoring, and severity scoring of the hysteria.

### 5. Fine-tuning ChatGLM3

Performed full fine-tuning of the ChatGLM3 model using prompts generated by the fourth task, enabling accurate and context-specific generation of "Hysterical Literature" text.


> Please note that the project is a collaborative effort, and the part I have uploaded represents my own contribution to the overall work.

> My team members have also made significant contributions to the project, and with their consent, additional components such as the utilization of K-means clustering, hierarchical clustering, and multiple linear regression to understand the relationship between 'Hysterical Literature' data and regional variables, as well as the application of the ARIMA method for forecasting the future popularity of "Hysterical Literature," will be uploaded in the future.



## What's 'Hysterical Literature'(发疯文学)?

It refers to some crazy crazy words and sentences together crazy literature, in fact, when you need to use words to achieve a certain purpose, give the other party a large paragraph similar to Qiongyao drama, crazy crazy words and sentences, let the other party feel your strong emotions at the moment.

### Examples
e.x.我起床了 这个点起床的人 是未来之星 是国家栋梁 是都市小说里的商业大鳄 是吾日三省吾身的自律者 是相亲节目里的心动嘉宾 是自然界的丛林之王 是世间所有丑与恶的唾弃者 是世间所以美与好的创造者

I got up at this point to get up the man is the future star is the pillars of the country is the commercial giant in the urban novel is my day three of my body self-discipline is the heart of the dating show is the king of the jungle in nature is the world all ugly and evil spit is the world all beautiful and good creator

e.x.破防了 !我真的破防了 !就因为你的一句话 ,我直接丢盔弃甲了 。你拆穿我那一秒 我满头大汗 、浑身发冷 、玉玉症瞬间发作了！像是被抓住尾巴的赛亚人 、带着海楼石的能力者 、抽离尾兽的人柱力!

The defense is broken! I really broke the guard! Just because of your word, I directly throw away the helmet and armor you uncovered me that second I was sweating all over the cold jade syndrome instant attack! Like a Saiyan by the tail with the power of a sea stone pulling away from the human pillar of the tail beast

## Prerequisites

 > A considerable amount of data processing is required during each task, and you may perform the necessary operations based on your specific requirements. This repository serves as a guideline and does not provide an exhaustive display of all the code for data processing, including tasks such as converting data formats, normalizing values, cleaning empty values, and so on. You may check my code in chatglm3-api&finetune/process-data for some reference.


Before you start, make sure you have the following:

- [chromedriver.exe](http://chromedriver.storage.googleapis.com/index.html): Download and place it in the current code path, based on your installed version of Google Chrome.

- Required Python libraries installed. You can install them using the following command:

    ```bash
    pip install wordcloud jieba jiagu keras numpy
    ```
    
- Have the following files downloaded and place them in the main directory of your project(You may find them online):

      - `cn_stopwords.txt`: The file containing Chinese stopwords for data cleaning.
  
      - `font.ttf`: The font file for the word cloud.


- Refer to [ChatGLM3](https://github.com/THUDM/ChatGLM3/blob/main/README_en.md#how-to-use) and [ChatGLM3 Finetuning](https://github.com/THUDM/ChatGLM3/tree/main/finetune_chatmodel_demo)if you've never used it. Make sure you have ChatGLM3 successfully deployed.

      - python>=3.10  (so as to finetune ChatGLM3)
  
    ```bash
    git clone https://github.com/THUDM/ChatGLM3
    cd ChatGLM3
    pip install -r requirements.txt
    ```

    ```bash
    git clone https://huggingface.co/THUDM/chatglm3-6b
    ```
    
    ```bash
    cd finetune_chatmodel_demo
    pip install requirements.txt
    ```


## Instructions

1. **Web Crawler:**
   - Open `crawler.py` and find the line: `id = "" `, replace the video ID with your interested Douyin video ID.
   - Run `crawler.py` to get comment data.
   - The crawled data will be stored in a CSV file, which will be named based on your video ID and will be used in generating word cloud.
       
2. **Generate Word Cloud:**
   - Replace the file name in `wordcloud.py` with your file name.
   - Run `wordcloud.py` to generate a word cloud pic based on the data.

3. **Analyze Emotion**
   - Replace the text with your text.
   - Run `emotion_analysis.py` to get the sentiment of the text.
     
4. **CNN Classifier**
   - Replace the csv with your data in `opinion_analysis/demo.py`
   - Run `opinion_analysis/demo.py`
   - Current hyperparameter:
       - Learning rate=0.001
       - Epochs=15
       - Batch size=128
   - Example results:
  
     <img src="https://github.com/oan-J/Data-Mining/blob/main/img/loss.png" alt="loss pic" width="300">
  
     
     <img src="https://github.com/oan-J/Data-Mining/blob/main/img/acc.png" alt="acc pic" width="300">

5. **Association Rule Mining**
   - To mine frequent itemsets using FP-Growth.
   - Run `fpgrowth.py`


6. **ChatGLM3 API Calling**
   - To categorize "Hysterical Literature" text using ChatGLM3 API, including scene recognition, emotion classification, emotion scoring, and severity scoring of the hysteria. 
   - Run `chatglm3-api&finetune/demo_crazy.py`
   - Example results:
   
   
7. **ChatGLM3 Fine-tuning**
   - Prepare data for fine-tuning by running `chatglm3-api&finetune/process-data/step2_csv2jsonl-category.py` or `https://github.com/oan-J/Data-Mining/blob/main/chatglm3-api%26finetune/process-data/step2_csv2jsonl-simple.py`. (prompt is different)
     > Simple Data may look like: {"prompt": "生成一段发疯文学", "response": "我起床了 这个点起床的人 是未来之星 是国家栋梁 是都市小说里的商业大鳄 是吾日三省吾身的自律者 是相亲节目里的心动嘉宾 是自然界的丛林之王 是世间所有丑与恶的唾弃者 是世间所以美与好的创造者"}
     > Categorized Data may look like: {"prompt": "生成一段发疯文学，场景为早晨，情感分类为自律，情感打分为80.0，发疯程度为20.0", "response": "我起床了 这个点起床的人 是未来之星 是国家栋梁 是都市小说里的商业大鳄 是吾日三省吾身的自律者 是相亲节目里的心动嘉宾 是自然界的丛林之王 是世间所有丑与恶的唾弃者 是世间所以美与好的创造者"}

   - Check `chatglm3-api&finetune/ChatGLM3-main/finetune_chatmodel_demo` and fine-tune ChatGLM3.
   - Current hyperparameter:
       - LR=1e-4
       - NUM_GPUS=4
       - MAX_SOURCE_LEN=1024
       - MAX_TARGET_LEN=128
       - DEV_BATCH_SIZE=1
       - GRAD_ACCUMULARION_STEPS=16
       - MAX_STEP=500
       - SAVE_INTERVAL=500
   
   - Example results:
<div style="text-align: center;">
  <figure>
    <table>
      <tr>
        <td style="text-align: center;">
          <table>
            <tr>
              <td>
                <img src="https://github.com/oan-J/Data-Mining/blob/main/chatglm3-api%26finetune/visualize_train_log/train-crazy_literature-20231210-222338-1e-4_loss.png" alt="simple prompt finetuning loss pic" width="300">
              </td>
            </tr>
            <tr>
              <td style="text-align: center;">
                <figcaption style="font-size:small; color:grey;">simple prompt finetuning loss pic</figcaption>
              </td>
            </tr>
          </table>
        </td>
        <td style="text-align: center;">
          <table>
            <tr>
              <td>
                <img src="https://github.com/oan-J/Data-Mining/blob/main/chatglm3-api%26finetune/visualize_train_log/train-crazy_literature_with_scene_and_rate-20231212-080910-1e-4.log_loss.png" alt="categorized prompt finetuning loss pic" width="300">
              </td>
            </tr>
            <tr>
              <td style="text-align: center;">
                <figcaption style="font-size:small; color:grey;">categorized prompt finetuning loss pic</figcaption>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </figure>
</div>


## Acknowledgement

This project utilizes code from the `ChatGLM3` library, which greatly contributed to categorizing and generating "Hysterical Literature" text.

Link to `ChatGLM3` repository: [chatglm3](https://github.com/THUDM/ChatGLM3)
