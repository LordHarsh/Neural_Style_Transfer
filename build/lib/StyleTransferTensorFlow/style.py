import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from pytube import YouTube
import os
import cv2
from PIL import Image
import shutil
import glob
import ffmpy

def transfer(content_img_path, style_img_path, tfhub_module='https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'):
  content_img = plt.imread(content_img_path)
  style_img = plt.imread(style_img_path)

  content_img = content_img.astype(np.float32)[np.newaxis, ...] / 255.0
  style_img = style_img.astype(np.float32)[np.newaxis, ...] / 255.0
  
  style_img =tf.image.resize(style_img, (265, 265))
  hub_module = hub.load(tfhub_module)
  outputs = hub_module(tf.constant(content_img), tf.constant(style_img))
  stylized_image = outputs[0]
  return stylized_image

def StyleTransferVideo(list_content_img_path, style_img_path, tfhub_module='https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'):
  content_img_list = [plt.imread(content_img_path) for content_img_path in list_content_img_path]
  style_img = plt.imread(style_img_path)

  content_img_list = [content_img.astype(np.float32)[np.newaxis, ...] / 255.0 for content_img in content_img_list]
  style_img = style_img.astype(np.float32)[np.newaxis, ...] / 255.0
  
  style_img =tf.image.resize(style_img, (265, 265))
  

  hub_module = hub.load(tfhub_module)
  outputs = [hub_module(tf.constant(content_img), tf.constant(style_img)) for content_img in content_img_list]
  print("-----------Style Transfer completed on all images-----------")
  return outputs


if __name__ == "__main__":
    import sys
    transfer(sys.argv[1], sys.argv[2])