# Hacklytics-2022-ArtificiallyIntelligent
Team Project for Hacklytics 2022 to develop an autoblurrer using Google's Vision API and a GAN blurrer

# Files:

VideoBlurrer.py: a prototype application using opencv and the Vision API to automatically blur video footage shot from a webcam. <br>
DataProcessing.ipynb: a notebook used to preprocess data for BlurGAN. Used the Vision API to separate images of multiple people (originally derived from the WIDER FACE dataset) into bounding box-sized images. <br>
BlurGAN.ipynb: a generative adversarial network developed to blur faces to a higher degree than conventional blurring algorithms, like Gaussian blur. Consists of a generator built on PyTorch and a discriminator built using the Vision AI. <br>

# Works Cited:

Yang, S., Luo, P., Loy, C., & Tang, X. (2016). WIDER FACE: A Face Detection Benchmark. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
