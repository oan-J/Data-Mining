import pandas as pd
import matplotlib.pyplot as plt

import dill

from sklearn.model_selection import train_test_split
import tensorflow as tf
import pickle
import numpy as np

sess=tf.compat.v1.InteractiveSession()

data = pd.read_csv("demo.csv", encoding='utf-8')
x = data['comments']
y = [[i] for i in data['label']]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)


from text_classification import TextClassification

clf = TextClassification()
texts_seq, texts_labels = clf.get_preprocess(x_train, y_train,
                                             word_len=1,
                                             num_words=2000,
                                             sentence_len=50)
history = clf.fit(texts_seq=texts_seq,
        texts_labels=texts_labels,
        epochs=15,
        batch_size=128,
        model=None)

plt.plot(history.history['loss'], label='Training Loss')
plt.title('Training Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.plot(history.history['acc'], label='Training Accuracy')
plt.title('Training Accuracy Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

with open('./%s.pkl' , 'wb') as f: 
    pickle.dump(clf, f)

with open('./%s.pkl', 'rb') as f:
    clf = pickle.load(f)
y_predict = clf.predict(x_test)
y_predict = [[clf.preprocess.label_set[i.argmax()]] for i in y_predict]
score = sum(y_predict == np.array(y_test)) / len(y_test)
print('score:',score)
