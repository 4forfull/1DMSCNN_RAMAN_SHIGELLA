import numpy as np
from pandas import read_csv, DataFrame
from sklearn.preprocessing import MinMaxScaler
from keras.models import model_from_json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def CNN_pre(filepath):
    print('Analysis starts. Please wait while enjoying your coffee...')
    df = read_csv(filepath)

    X = np.expand_dims(df.values[:, 0:630].astype(float), axis=2)

    json_file = open(r"Multiscale-CNN.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("Multiscale-CNN.h5")

    predicted_label = loaded_model.predict(X)
    predicted_label = np.argmax(predicted_label, axis=1)
    predicted_pro = loaded_model.predict(X)
    predicted_pro = np.max(predicted_pro)

    if predicted_label == 0:
        print("Analysis result: the species is Shigella Sonnei and the predicted accuracy is {:.2%}".format(predicted_pro))

    elif predicted_label == 1:
        print("Analysis result: the species is Shigella flexneri and the predicted accuracy is {:.2%}".format(predicted_pro))

    elif predicted_label == 2:
        print("Analysis result: the species is Shigella boydii and the predicted accuracy is {:.2%}".format(predicted_pro))

    else:
        print("Analysis result: the species is Shigella dysenteriae and the predicted accuracy is {:.2%}".format(predicted_pro))


if __name__ == "__main__":
    file_path = './demo.csv'
    CNN_pre(file_path)
