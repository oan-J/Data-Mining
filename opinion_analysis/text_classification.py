from data_preprocess1 import DataPreprocess
from net import CNN
import numpy as np


class TextClassification():
    def __init__(self):
        self.preprocess = None
        self.model = None

    def get_preprocess(self, texts, labels, word_len=1, num_words=2000, sentence_len=30):

        preprocess = DataPreprocess()


        texts_cut = preprocess.cut_texts(texts, word_len)
        preprocess.train_tokenizer(texts_cut, num_words)
        texts_seq = preprocess.text2seq(texts_cut, sentence_len)


        preprocess.creat_label_set(labels)
        labels = preprocess.creat_labels(labels)
        self.preprocess = preprocess

        return texts_seq, labels

    def fit(self, texts_seq, texts_labels,epochs, batch_size, model=None):
        if model is None:
            preprocess = self.preprocess
            model = CNN(preprocess.num_words,
                        preprocess.sentence_len,
                        128,
                        len(preprocess.label_set)
                        )

        history = model.fit(texts_seq,
                  texts_labels,
                  epochs=epochs,
                  batch_size=batch_size)
        self.model = model
        return history

    def predict(self, texts):
        preprocess = self.preprocess
        word_len = preprocess.word_len
        sentence_len = preprocess.sentence_len


        texts_cut = preprocess.cut_texts(texts, word_len)
        texts_seq = preprocess.text2seq(texts_cut, sentence_len)

        return self.model.predict(texts_seq)

    def label2toptag(self, predictions, labelset):
        labels = []
        for prediction in predictions:
            label = labelset[prediction == prediction.max()]
            labels.append(label.tolist())
        return labels

    def label2half(self, predictions, labelset):
        labels = []
        for prediction in predictions:
            label = labelset[prediction > 0.5]
            labels.append(label.tolist())
        return labels

    def label2tag(self, predictions, labelset):
        labels1 = self.label2toptag(predictions, labelset)
        labels2 = self.label2half(predictions, labelset)
        labels = []
        for i in range(len(predictions)):
            if len(labels2[i]) == 0:
                labels.append(labels1[i])
            else:
                labels.append(labels2[i])
        return labels