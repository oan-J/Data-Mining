import jiagu

# text = '当我开开心心的艾特你的时候 你的心犹如冰块一样冰冷 你不知道 我煎熬期待着你会很开心的回复我 可是我等到的什么都没有 我的心就像来了大窟窿我的房间漆黑一片我的心也漆黑一片真的破防了'
f = open("douyin.txt",encoding='utf-8')
text = f.readline()
print(f.readline())
f.close()
sentiment = jiagu.sentiment(text)
print(sentiment)

