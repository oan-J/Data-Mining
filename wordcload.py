from wordcloud import WordCloud  # 导入词云库生成词云
import jieba  # 导入jieba库分词
def get_img():
    data = open("area.txt", "r", encoding="utf-8").read()  # 获取我们刚才获取到的数据
    stop_word = set(open("./cn_stopwords.txt", encoding='utf-8').read().split())  # 导入停词表，进行数据的清洗，这个可以直接在百度上搜索下载
    word_list = [w for w in jieba.cut(data)]
    # print("douyin succeed")
    font = "./font.ttf"  # 导入字体
    print("douyin succeed")
    wc = WordCloud(font_path=font,
                   width=1000,
                   height=700,
                   background_color='white',
                   max_words=100,
                   stopwords=stop_word,  # 加载停用词
                   ).generate(" ".join(word_list))  # 加载词云文本
    wc.to_file("./ret_douyin_area.png")

get_img()