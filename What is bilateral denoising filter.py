# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:07:07 2021

@author: abc
"""

import cv2
import numpy as np
from skimage import io, img_as_float

#read our image
img_gaussian_noisy = cv2.imread("BSE_25sigma_noisy.jpg",0)

#activate our image
img = img_gaussian_noisy

#define bilateral filter using opencv
bilateral_using_cv2 = cv2.bilateralFilter(img, 5, 20, 100, borderType=cv2.BORDER_CONSTANT)

#define bilateral filter using skimage
from skimage.restoration import denoise_bilateral
bilateral_using_skimage = denoise_bilateral(img, sigma_color=0.05, sigma_spatial=15,multichannel=False)

#show our image
cv2.imshow("Original image" , img)
cv2.imshow("CV2 Filter image", bilateral_using_cv2)
cv2.imshow("SKIMAGE filter image", bilateral_using_skimage)
cv2.waitKey(0)
cv2.destroyAllWindows()





