import jiagu

text = ''
text = f.readline()
print(f.readline())
f.close()
sentiment = jiagu.sentiment(text)
print(sentiment)

