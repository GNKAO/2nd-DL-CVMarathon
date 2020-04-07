# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:24:53 2020

@author: user
"""

import cv2 
import numpy as ny
img = cv2.imread('lena.png',cv2.IMREAD_COLOR)
img2 = cv2.cvtColor(img,cv2.COLOR__BGR2HSV)
cv2.imshow("lena",img)
cv2.imshow("lena change",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()