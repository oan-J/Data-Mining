from wordcloud import WordCloud  
import jieba  
def get_img():
    data = open("douyin.txt", "r", encoding="utf-8").read()  
    stop_word = set(open("./cn_stopwords.txt", encoding='utf-8').read().split()) 
    word_list = [w for w in jieba.cut(data)]
    # print("douyin succeed")
    font = "./font.ttf" 
    print("douyin succeed")
    wc = WordCloud(font_path=font,
                   width=1000,
                   height=700,
                   background_color='white',
                   max_words=100,
                   stopwords=stop_word, 
                   ).generate(" ".join(word_list))  
    wc.to_file("./ret_douyin_area.png")

get_img()
