from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import numpy as np

from keras.models import load_model
# from keras.preprocessing import image
import keras.utils as image
from PIL import Image, ImageEnhance, ImageOps
import os


import tensorflow as tf
import json


# Create your views here.
def index(request):
    context={'a':1}
    return render(request, 'index.html', context)

def prediction(request):
    context={'a':1}
    return render(request, 'prediction.html', context)

img_height, img_width = 150,150
# with open('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source','r') as f:
#     labelinfo=f.read()

# labelinfo=json.load(labelinfo)

def get_label_name(label):
    if label == 0:
        return "Bacterial leaf blight"
    if label == 1:
        return "Brown spot"
    if label == 2:
        return "Leaf smut"

model = load_model('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/model.h5')

def desease(request):

    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    image_dir = '.'+filePathName

    img = image.load_img(image_dir, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x/225
    x = x.reshape(1, img_height, img_width,3)
    score= model.predict(x)
    print ("SCORE:" +str(score))

    label_indx = np.argmax(score)
    accuracy = round(np.max(score), 4)
    
    predictedLabel = get_label_name(label_indx)

    context={'filePathName':filePathName, 'predictedLabel':predictedLabel, 'accuracy':accuracy}
    return render(request, 'prediction.html', context)


def dataset(request):

    train = 'C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/train'
    tleaf = len(os.listdir(train + '/Leaf smut'))
    tbrown = len(os.listdir(train + '/Brown spot'))
    tbacterial = len(os.listdir(train + '/Bacterial leaf blight'))

    
    valid = 'C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/valid'
    vleaf = len(os.listdir(valid + '/Leaf smut'))
    vbrown = len(os.listdir(valid + '/Brown spot'))
    vbacterial = len(os.listdir(valid + '/Bacterial leaf blight'))

    test = 'C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/test'
    teleaf = len(os.listdir(test + '/Leaf smut'))
    tebrown = len(os.listdir(test + '/Brown spot'))
    tebacterial = len(os.listdir(test + '/Bacterial leaf blight'))

    print(tleaf, tbrown, tbacterial)

    # train = [str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/train/Leaf smut'))),
    # str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/train/Brown spot'))),
    # str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/train/Bacterial leaf blight')))]

    # validation = [str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/valid/Leaf smut'))),
    # str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/valid/Brown spot'))),
    # str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/valid/Bacterial leaf blight')))]

    # test = [str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/test/Leaf smut'))),
    # str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/test/Brown spot'))),
    # str(len(os.listdir('C:/Users/LENOVO/Documents/project deteksi penyakit tanaman padi/source/PaddyLeafDiseaseUCI/test/Bacterial leaf blight')))]
    
    # 'validation':validation,'test':test
    context={'tleaf':tleaf, 'tbrown':tbrown, 'tbacterial':tbacterial,
             'vleaf':vleaf, 'vbrown':vbrown, 'vbacterial':vbacterial,
             'teleaf':teleaf, 'tebrown':tebrown, 'tebacterial':tebacterial,
    }
    return render(request, 'dataset.html', context)

def accouracy(request):

    context={'a':1}
    return render(request, 'accouracy.html', context)

def about(request):
    context={'a':1}
    return render(request, 'about.html', context)