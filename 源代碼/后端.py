import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
#from keras.utils import to_categorical
from sklearn.metrics import mean_absolute_error
from keras.models import load_model
from flask import Flask
from flask_cors import CORS
from flask import request
import tensorflow_federated as tff
import collections



app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def greet():
    return "Hi I am BIT1120173716"

@app.route("/trainFederated", methods=["POST"])
def train_data_LB():
    res = request.get_data()#batch_size = 128, epochs = 10, learning-rate = 0.00001, decay = 0.00001
    str1 = str(res,'utf-8')
    str2 = eval(str1)
    numBatchSize = int(str2["batchsize"])
    numEpochs = int(str2["epochs"])
    numLearningRate = float(str2['lr'])
    numDecay = float(str2['decay'])
    tags = ['age', 'bf', 'hz', 'jl', 'tj', 'dc', 'yz', 'mb', 'eeg']
    data_train = pd.read_csv('data_res1.csv')
    data_train_1 = pd.read_csv("data_1_part1.csv")
    data_train_2 = pd.read_csv('data_1_part2.csv')
    # data_train_1 = pd.read_csv("data_2_part1.csv")
    # data_train_2 = pd.read_csv('data_2_part2.csv')
    data_train.dropna(inplace=True)
    data_train_1.dropna(inplace=True)
    data_train_2.dropna(inplace=True)
    x = data_train[tags]
    y = data_train['drug']
    x1 = data_train_1[tags]
    y1 = data_train_1['drug']
    x2 = data_train_1[tags]
    y2 = data_train_1['drug']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    x_train_1, x_test_1, y_train_1, y_test_1 = train_test_split(x1, y1, test_size=0.2)
    x_train_2, x_test_2, y_train_2, y_test_2 = train_test_split(x2, y2, test_size=0.2)
    model = keras.Sequential([
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal', input_shape=[9]),
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dense(68, activation='softmax')])
    # # 损失函数计算方法使用交叉熵，数据为数字编码用这个，数据为one-hot编码的话用categorical_crossentropy，优化器选择Adam
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=numLearningRate, decay=numDecay))
    for i in range(numEpochs):
        model_1 = model
        model_2 = model
        model_1.fit(x_train_1, y_train_1, epochs=numEpochs, batch_size=numBatchSize)
        model_2.fit(x_train_2, y_train_2, epochs=numEpochs, batch_size=numBatchSize)
        for i in range(5):
            m1 = model_1.layers[i].get_weights()
            m2 = model_2.layers[i].get_weights()
            temp_weight = m1[0]+m2[0]
            temp_weight = temp_weight / 2
            #temp_weight = m1[0]*0.764 + m2[0]*0.236
            temp_bias = (m1[1]+m2[1]) /2
            #temp_bias = m1[1]*0.764 + m2[1]*0.236
            weights = []
            weights.append(temp_weight)
            weights.append(temp_bias)
            model.layers[i].set_weights(weights)
    model.save("my_model.h5")
    s = model.predict(x_test)
    res = []
    for i in range(len(s)):
        list_tmp = []
        for j in range(len(s[i])):
            if s[i][j] >= 0.05:
                list_tmp.append(j)
        res.append(list_tmp)
    y_test = y_test.values
    cnt = 0
    for i in range(len(y_test)):
        for j in range(len(res[i])):
            if res[i][j] == y_test[i]:
                cnt += 1
    ans = cnt / len(y_test)
    print(ans)
    return ("Accuarcy=" + repr(ans))

@app.route("/trainNeuralNetwork", methods=["POST"])
def train_data_NN():
    res = request.get_data()
    str1 = str(res,'utf-8')
    str2 = eval(str1)
    numBatchSize = int(str2["batchsize"])
    numEpochs = int(str2["epochs"])
    numLearningRate = float(str2['lr'])
    numDecay = float(str2['decay'])
    tags = ['age', 'bf', 'hz', 'jl', 'tj', 'dc', 'yz', 'mb', 'eeg']
    data_train = pd.read_csv('data_res.csv')
    data_train.dropna(inplace=True)
    x = data_train[tags]
    y = data_train['drug']
    # # 获得y值
    # y = data_train['price'].values
    # 切分数据集  test_size ：80%训练，20%测试
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # dense 一层n个神经元的全连接网络，激活层relu，input_shape是输入的特征维数
    model = keras.Sequential([
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal', input_shape=[9]),
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dense(24, activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dense(68, activation='softmax')])
    # # 损失函数计算方法使用交叉熵，数据为数字编码用这个，数据为one-hot编码的话用categorical_crossentropy，优化器选择Adam
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer= tf.keras.optimizers.Adam(learning_rate=numLearningRate, decay=numDecay))
    # # lr为学习率，decay为每次参数更新后学习率的衰减值
    # # batch_size和epochs 大概是把数据拆成50份，每份2048个，
    # # 当一个完整的数据集通过神经网络一次并返回一次的过程称为一个epoch
    # # 随着epochs的增加，权重更新次数也会增加，如果过少可能欠拟合，过多可能过拟合
    model.fit(x_train, y_train, epochs=numEpochs, batch_size=numBatchSize)
    model.save("my_model.h5")
    model = load_model("my_model.h5")
    print(x_test)
    print(type(x_test))
    s = model.predict(x_test)
    print(s[0])
    print(s[0][1])
    print(len(s))
    print(len(s[0]))
    print(s)
    res = []
    for i in range(len(s)):
        list_tmp = []
        for j in range(len(s[i])):
            if s[i][j] >= 0.08:
                list_tmp.append(j)
        res.append(list_tmp)
    y_test = y_test.values
    cnt = 0
    for i in range(len(y_test)):
        for j in range(len(res[i])):
            if res[i][j] == y_test[i]:
                cnt += 1
    ans = cnt/len(y_test)
    print(ans)
    return("Accuarcy="+repr(ans))


@app.route("/test", methods=["POST"])
def test_data():
    model = load_model('my_model.h5')
    res = request.get_data()
    str1 = str(res, 'utf-8')
    str2 = eval(str1)
    str3 = [[float(i) for i in str2.values()]]
    temp_test = pd.DataFrame(str3,columns=['age','bf','hz','jl','tj','dc','yz','mb','eeg'])
    res = model.predict(temp_test)
    drugs_result = ['ACTH', 'CBZ', 'CLB', 'CZP', 'DZP', 'ESM', 'LCM', 'LEV', 'LTG', 'NZP', 'None', 'OXC', 'PB', 'PHT', 'PRP', 'TPM', 'VGB', 'VPA', 'ZNS', '丙戊酰胺', '中成药', '优甲乐', '利培酮', '加巴喷丁', '劳拉西泮', '可乐定', '右美沙芬', '叶酸', '吡拉西坦', '咪达唑仑', '大麻二酚', '奎硫平', '奥氮平', '安坦', '尼莫地平', '左卡尼汀', '希力舒', '强的松', '文拉法辛', '普瑞巴林', '氟桂利嗪', '氯氮平', '水合氯醛', '治痫灵', '泼尼松', '环磷酰胺', '生酮饮食', '甲强龙', '益脑灵', '盐酸托莫西汀', '硫必利', '碳酸锂', '维生素B6', '羊痫丸', '美多巴', '舍曲林', '舍曲林分散片', '舒必利', '艾司唑仑', '苯海索', '苯溴马隆', '补脑丸', '西罗莫司', '醋酸强的松', '醋酸泼尼松', '阿立哌唑', '雷帕霉素', '静灵口服液']
    res2 = []
    print(res)
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] >= 0.08:
                if j == 10:
                    if res[i][j] >= 0.15:
                        res2 = None
                        break
                else:
                    res2.append(drugs_result[j])
    res3 = repr(res2)
    return res3

app.run()