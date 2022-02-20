# Hacklytics-2022-ArtificiallyIntelligent
Team Project for Hacklytics 2022 to develop an autoblurrer using Google's Vision API and a DCGAN blurrer.

# Files:

<b>VideoBlurrer.py:</b> a prototype application using opencv and the Vision API to automatically blur video footage shot from a webcam. <br>
<b>DataProcessing.ipynb:</b> a notebook used to preprocess data for BlurGAN. Used the Vision API to separate images of multiple people (originally derived from the WIDER FACE dataset) into bounding box-sized images. <br>
<b>BlurGAN.ipynb:</b> a generative adversarial network developed to blur faces to a higher degree than conventional blurring algorithms, like Gaussian blur. Consists of a generator built on PyTorch and a discriminator built using the Vision AI. <br>
<b>BlurGAN-earlydemo.png:</b> A blur filter developed by BlurGAN on its second training epoch. <br>
<b>GaussianBlurDemo.png:</b> A picture with the subject's face blurred using a Gaussian Blur.

# Works Cited:

Yang, S., Luo, P., Loy, C., & Tang, X. (2016). WIDER FACE: A Face Detection Benchmark. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
