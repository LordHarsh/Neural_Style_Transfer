# Neural_Style_Transfer

##### This project has the ability to perform neural style transfer on videos by leveraging TensorFlow libraries.

To try this install `StyleTransferTensorFlow` using `pip`.

`pip install StyleTransferTensorFlow`


Try it now in this colab [here](https://colab.research.google.com/github/LordHarsh/Neural_Style_Transfer/blob/main/Style_Transfer.ipynb)

<a href="https://colab.research.google.com/github/LordHarsh/Neural_Style_Transfer/blob/main/Style_Transfer.ipynb" target="_blank" rel="noopener noreferrer">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

To use it call the function `make`.

`StyleTransferTensorFlow.make(vidpath, style_image_path,invert=False, extractframerate)`

Here
| Parameter | Description | Category |
| :-------------: |:-------------:| :-----:|
| vidpath      | Path to the Content video file | Important |
| style_image_path | Path to the Style file      |   Important |
| invert | To try some different image colour      |    Optional (default-False) |
| extractframerate | rate at which to extract frames |    Optional (default-30) |
