import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np


def transfer(content_img_path, style_img_path):
  content_img = plt.imread(content_img_path)
  style_img = plt.imread(style_img_path)

  content_img = content_img.astype(np.float32)[np.newaxis, ...] / 255.0
  style_img = style_img.astype(np.float32)[np.newaxis, ...] / 255.0
  
  style_img =tf.image.resize(style_img, (265, 265))
  hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
  outputs = hub_module(tf.constant(content_img), tf.constant(style_img))
  stylized_image = outputs[0]
  return stylized_image