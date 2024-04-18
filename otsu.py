# -*- coding: utf-8 -*-

"""
Created on Thu Apr 18, 2024

@author: https://github.com/sf0831
"""


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image




# OTSU FUNCTION
def binarize_image_otsu(file_path):
    input_image = Image.open(file_path).convert("L")



    input_array  = np.array(input_image)

    histogram_count, bins_count = np.histogram(input_image, bins=256, range=(0, 255))

    pdf= histogram_count / np.sum(histogram_count)
    cdf = np.cumsum(pdf)

    otsu_threshold = 0
    max_variance = 0

    intensities = np.arange(256)
    
    
    for t in range(1, 256):
        p0 = cdf[t]  # cumulative density function of class 0
        p1 = 1 - p0  # cumulative density function of class 1
        
        
        # skipping division by zero
        if p0 == 0 or p1 == 0:
            continue
        
        # class means
        m0 = np.sum(intensities[:t] * pdf[:t]) / p0  # mean of class 0 (background)
        m1 = np.sum(intensities[t:] * pdf[t:]) / p1  # mean of class 1 (foreground)
        
        
        # between-class variance
        between_class_variance = p0 * p1 * (m0 - m1)**2
        
        # updating the optimal threshold
        if between_class_variance > max_variance:
            max_variance = between_class_variance
            otsu_threshold = t
        
        
        if between_class_variance > max_variance:
            max_variance = between_class_variance
            otsu_threshold = t
            
            
    # binarize the input image using the computed Otsu's threshold
   
    binary_array = input_array > otsu_threshold
    binary_image = Image.fromarray(binary_array.astype(np.uint8) * 255)

    return binary_image
    
                                           
                                          
                                            
# TESTER CODE


# FIRST IMAGE - MENINGIOMA BRAIN TUMOR
file_path_meningioma = r"Te-meTr_0000.jpg"
binary_result_meningioma = binarize_image_otsu(file_path_meningioma)
plt.figure(figsize=(12, 6))

# input image
''' input images source : Kaggel
(https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
'''


plt.subplot(1, 2, 1)
meningioma = Image.open(file_path_meningioma).convert("L")
plt.imshow(meningioma, cmap='gray')
plt.title("MENINGIOMA Image")
plt.axis('off')

# binarized Image (Otsu's Threshold)
plt.subplot(1, 2, 2)
plt.imshow(binary_result_meningioma, cmap='binary')
plt.title("Binarized Image (Otsu's Threshold)")
plt.axis('off')

plt.tight_layout()
plt.show()


# SECOND IMAGE - GLIOMA BRAIN TUMOR
file_path_glioma = r"Te-glTr_0005.jpg"
binary_result_glioma = binarize_image_otsu(file_path_glioma)
plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
glioma = Image.open(file_path_glioma).convert("L")
plt.imshow(glioma, cmap='gray')
plt.title("GLIOMA Image")
plt.axis('off')

# binarized Image (Otsu's Threshold)
plt.subplot(1, 2, 2)
plt.imshow(binary_result_glioma, cmap='binary')
plt.title("Binarized Image (Otsu's Threshold)")
plt.axis('off')

plt.tight_layout()
plt.show()

