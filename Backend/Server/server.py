from flask import Flask, render_template, request, jsonify, make_response
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os.path as op
import sys
import cv2
import torch
import numpy as np
import yaml
sys.path.append('..')
from utils import vis_segmentation, run_inference

app = Flask(__name__)
np.random.seed(42)
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

@app.route('/')
def index():
    return render_template('index.html', image=None)
@app.route('/segment', methods=['POST'])

def segment_image():
    # Get the image from the POST request
    image = request.files['image']
    image = Image.open(image)
    #convert to numpy array 
    image = np.array(image)

    model = torch.load(config['LOAD_MODEL_PATH'],map_location=torch.device('cpu'))
    model.eval()
    predicted_masks = run_inference(model, image)
    #return image and predicted mask to api call
    vis_segmentation(image, np.array(predicted_masks), "output.png")

    seg_img = cv2.imread('output.png')
    response1 = make_response(cv2.imencode('.png', seg_img)[1].tobytes())
    response1.headers.set('Content-Type', 'image/jpeg')

    return  response1 , 200


if __name__ == '__main__':
    app.run()