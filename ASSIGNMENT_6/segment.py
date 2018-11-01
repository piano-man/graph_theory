import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

import os
os.environ["MKL_THREADING_LAYER"] = "GNU"

import numpy

import cv2
import math
from utility_modules import evaluate, space_contours

# Global Variables Declaration



def add_padding(im):
	old_size = im.shape[:2]
	print(old_size,'hello')
	desired_size = 45

	ratio = float(desired_size)/max(old_size)
	new_size = tuple([int(x*ratio) for x in old_size])

	im = cv2.resize(im, (new_size[1], new_size[0]))

	delta_w = desired_size - new_size[1]
	delta_h = desired_size - new_size[0]
	top, bottom = delta_h//2, delta_h-(delta_h//2)
	left, right = delta_w//2, delta_w-(delta_w//2)

	color = [255]
	new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
	return new_im





def process_expression(img_addr, chars):
	# binarized = cv2.adaptiveThreshold(cv2.imread(img_addr, 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	# binarized = cv2.fastNlMeansDenoisingColored(cv2.imread(img_addr),None,10,10,7,21)
	# binarized = cv2.cvtColor(binarized, cv2.COLOR_RGB2GRAY)
	binarized = cv2.imread(img_addr, 0)
	for r in range(binarized.shape[0]):
		for c in range(binarized.shape[1]):
			if binarized[r, c] < 127:
				binarized[r, c] = 0
			else:
				binarized[r, c] = 255
	# ret3,binarized = cv2.threshold(binarized, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	kernel = numpy.ones((3, 3),numpy.uint8)
	binarized = cv2.erode(binarized, kernel, iterations = 1)
	# binarized = cv2.dilate(binarized, kernel, iterations = 1)
	binarized = space_contours.spacing(binarized)
	cv2.imshow("Image after Spacing", binarized)
	cv2.waitKey(0)
	(cnts, heirarchy) = cv2.findContours(binarized.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	contours = []

	for k in range(len(cnts)):
		if heirarchy[0][k][3] == 0:
			contours.append(cv2.boundingRect(cnts[k]))

	contours.sort()

	
		#uncomment the below code to view segmented tokens 
	temp = binarized.copy()
	for x, y, w, h in contours:
		cv2.rectangle(temp, (x, y), (x + w, y + h), 1)
	cv2.imshow("contours", temp)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	

	tokens = []

	for k in range(len(contours)):
		x, y, w, h = contours[k]
		chars.append(binarized[y : y + h, x : x + w])
		tokens.append(add_padding(binarized[y : y + h, x : x + w]))
		cv2.imshow("cropped_image"+str(k), add_padding(binarized[y : y + h, x : x + w]))
		cv2.waitKey(0)
	tokens = numpy.array(tokens)
	tokens = tokens.reshape(tokens.shape[0], 1, 45, 45).astype('float32')
	tokens = tokens / 255
	return tokens



if __name__ == "__main__":
	while True:
		img_addr = raw_input("Enter Image Address--->").strip()
		try:
			if img_addr == "":
				continue
			chars = []
			process_expression(img_addr, chars)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		except:
			continue
