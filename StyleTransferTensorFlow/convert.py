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

def ConvertTensorToCV2(generated_tensor, invert=False):
  # Tensorflow array to PIL image
  generated_pil_img_array = [tf.keras.preprocessing.image.array_to_img(generated_tensor[i][0][0]) for i in range(len(generated_tensor))]

  # PIL image to cv2 image
  if invert:
      generated_cv2_img_array = [np.array(generated_pil_img_array[i], dtype=np.uint8).copy()  for i in range(len(generated_pil_img_array))]
  else:
      generated_cv2_img_array = [np.array(generated_pil_img_array[i], dtype=np.uint8)[:, :, ::-1].copy()  for i in range(len(generated_pil_img_array))]
  print("-----------Image conversion completed-----------")
  return generated_cv2_img_array

def ConvertImagesToVideo(final_cv2_image_list, length=1):
  height, width, layers = final_cv2_image_list[0].shape
  size = (width,height)

  path = os.path.join(os.getcwd(), 'StyleVideo.avi')
  out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'DIVX'), length, size)
  
  for i in range(len(final_cv2_image_list)):
    out.write(final_cv2_image_list[i])
    
  out.release()
  print("-----------Video construction completed-----------")
  return path

def convert_avi_to_mp4(avi_file_path):
  mp4_path = os.path.join(os.getcwd(), 'StyleVideo.mp4')
  if os.path.exists(mp4_path):
    os.remove(mp4_path)

  ff = ffmpy.FFmpeg(
      inputs={os.path.basename(avi_file_path): None},
      outputs={os.path.basename(mp4_path): None}
  )
  ff.run()

  print("-----------Video conversion completed-----------")
  return mp4_path