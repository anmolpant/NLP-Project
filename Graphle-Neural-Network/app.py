from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np

# Keras and pytorch
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
import torch                                        
from torch.utils.data import Dataset, Dataloader
import torch.autograd as autograd         
from torch import Tensor                  
import torch.nn as nn                     
import torch.nn.functional as F           
import torch.optim as optim               
from torch.jit import script, trace           

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

#flask app
app = Flask(__name__)
MODEL_PATH1 = 'decoder.pt'
MODEL_PATH2 = 'encoder.pt'

# Load your trained model
model1 = load_model(MODEL_PATH1)
model1._make_predict_function()
model2 = load_model(MODEL_PATH2)
model2._make_predict_function()          


def model_predict(sentence, model1, model2):
    sent = sentence.preprocess_input(model1)
    x = model2.Tensor(sent)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='caffe')
    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        # Make prediction
        preds = model_predict(sent, model1, model2)
        # Simple argmax
        pred_class = decode_predictions(preds, top=1)  
        result = str(pred_class[0][0][1])        
        return result
    return None

if __name__ == '__main__':
    app.run(debug=True)