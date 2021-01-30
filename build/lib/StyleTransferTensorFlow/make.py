import os
from StyleTransferTensorFlow import extract
from StyleTransferTensorFlow import style
from StyleTransferTensorFlow import convert


def MakeVideo(vidpath, style_image_path,invert=False, extractframerate=30):
  current_directory = os.getcwd()
  onlyfiles, imgfolderpath = extract.ExtractFrames(vidpath, current_directory, extractframerate)
  content_img_path_list = [os.path.join(imgfolderpath, pp) for pp in onlyfiles]
  #style_image_path = os.path.join(os.getcwd(),'style.jpg')
  generated_img_list_output = style.StyleTransferVideo(content_img_path_list, style_image_path)
  final_cv2_image_list = convert.ConvertTensorToCV2(generated_img_list_output, invert)
  avi_video_path = convert.ConvertImagesToVideo(final_cv2_image_list)
  mp4_video_path = convert.convert_avi_to_mp4(avi_video_path)
  print("Path of the new video:" +mp4_video_path)
  return mp4_video_path
  
  
if __name__ == "__main__":
  import sys
  MakeVideo(sys.argv[1], sys.argv[2])