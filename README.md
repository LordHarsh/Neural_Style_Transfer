# Neural_Style_Transfer

##### This project has ability to perform neural style transfer on videos by leveraging TeansorFlow libraries.

To try this install `StyleTransferTensorFlow` using `pip`.

`pip install StyleTransferTensorFlow`


Try it now in this colab [here](https://colab.research.google.com/github/LordHarsh/Neural_Style_Transfer/blob/main/Style_Transfer.ipynb)

To use it call the function `make`.

`StyleTransferTensorFlow.make(vidpath, style_image_path,invert=False, extractframerate)`

Here
|               |               |       |
| ------------- |:-------------:| -----:|
| vidpath      | Path to the Content video file | Imporant |
| style_image_path | Path to the Style file      |   Important |
| invert | To try some different image colour      |    Optional (default-False) |
| extractframerate | rate at which to extract frames |    Optional (default-30) |
