# Otsu-Thresholding - Application on Brain Tumor MRI images
Image processing - Segmentation using the famous Otsu algorithm 
This repository contains a simple Python implementation of image binarization using Otsu's thresholding method. Image binarization is the process of converting a grayscale image into a binary image, where each pixel is either black or white based on a calculated threshold.

## Example 1: FIRST IMAGE - MENINGIOMA BRAIN TUMOR
![image](https://github.com/sf0831/Otsu-Thresholding/assets/81633609/be626416-e89d-4b56-8d60-7da1bc6e0a17)

## Example 2: SECOND IMAGE - GLIOMA BRAIN TUMOR
![image](https://github.com/sf0831/Otsu-Thresholding/assets/81633609/d85c89a9-bbc2-44d8-850b-b89f2fd9e867)


### Image sources:
I have used the kaggle dataset for this images, at the link below:
https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset

## IMPORTANT NOTE
1- Use PIL library for loading images, proven to work better than skimage library
2- Images are flattened (converted to an array) in order to computation process to work smoothly!
3 - Using of Spider as your python IDE is recommended.
