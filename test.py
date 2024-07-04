import numpy as np
import cv2
image = cv2.imread('contoh.jpg')


cv.imshow('text', image1 / variable)
cv.imshow('text', image2 / variable)
cv2.waitKey(0)
cv2.destroyAllWindows()

rgb2gray = cv2.imread('contoh.jpg')

b, g, r = cv2.split(rgb2gray)
rgb2gray = cv2.merge((b, g, r))

x = rgb2gray[:, :, 0]

cv2.imshow('Original', rgb2gray)
cv2.imshow('After Effect', x)
cv2.waitKey(0)
cv2.destroyAllWindows()

original = cv2.imread('001.jpg')

blurimage = cv2.blur(original, (11, 11))

cv2.imshow('Original', original)
cv2.imshow('After Effect', blurimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

original = cv2.imread('005.jpg')

medianblurimage = cv2.medianBlur(original, 5)

cv2.imshow('Original', original)
cv2.imshow('After Effect', medianblurimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

original = cv2.imread('004.jpg')

sharpening_filter = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])

sharpened_image = cv2.filter2D(original, -1, sharpening_filter)

cv2.imshow('Original', original)
cv2.imshow('After Effect', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
