from keras.models import Model
from keras.layers import Dense, Embedding, Input
from keras.layers import Conv1D, GlobalMaxPool1D, Dropout
from tensorflow.keras.utils import plot_model
import matplotlib.pyplot as plt
# from keras.utils import plot_model
from tensorflow.keras.utils import plot_model
from IPython.display import Image

def CNN(input_dim,
        input_length,
        vec_size,
        output_shape):

    data_input = Input(shape=[input_length])
    word_vec = Embedding(input_dim=input_dim + 1,
                         input_length=input_length,
                         output_dim=vec_size)(data_input)
    x = Conv1D(filters=128,
               kernel_size=[3],
               strides=1,
               padding='same',
               activation='relu')(word_vec)
    x = GlobalMaxPool1D()(x)
    x = Dense(500, activation='relu')(x)
    x = Dropout(0.1)(x)

    x = Dense(output_shape, activation='softmax')(x)
    model = Model(inputs=data_input, outputs=x)
    model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['acc'])

    return model


if __name__ == '__main__':
    model = CNN(input_dim=10, input_length=10, vec_size=10, output_shape=10)
    #input_shape：即张量的shape。从前往后对应由外向内的维度。
    #input_length：代表序列长度，可以理解成有多少个样本
    #input_dim：代表张量的维度，（很好理解，之前3个例子的input_dim分别为2,3,1）


    model.summary()
    # plot_model(model, to_file='cnn_model.png', show_shapes=True, show_layer_names=True)
    #
    # # Display the model architecture using Matplotlib
    # img = plt.imread('cnn_model.png')
    # plt.figure(figsize=(10, 10))
    # plt.imshow(img)
    # plt.show()

    plot_model(model, to_file='model.png', show_shapes=True)

    # 显示模型结构图
    Image('model.png')