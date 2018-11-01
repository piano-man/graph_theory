import cv2
import numpy

def flood_fill(img, mat, r, c, mat_c):
	h, w = img.shape
	sink = []
	sink.append((r, c))

	diff = mat_c - c
	maxi = c
	while len(sink):
		r, curr_c = sink[-1]
		sink.pop()
		if r < 0 or r >= h or curr_c < 0 or curr_c >= w:
			continue

		if img[r, curr_c] != 0:
			continue

		# if mat[r, curr_c + diff] == 150:
		img[r, curr_c] = 255
		mat[r, curr_c + diff] = 0
		maxi = max(maxi, curr_c)
		sink.append((r - 1, curr_c - 1))
		sink.append((r - 1, curr_c))
		sink.append((r - 1, curr_c + 1))
		sink.append((r, curr_c - 1))
		sink.append((r, curr_c + 1))
		sink.append((r + 1, curr_c - 1))
		sink.append((r + 1, curr_c))
		sink.append((r + 1, curr_c + 1))
	return maxi - c

def spacing(img):
	cv2.imshow("binarized", img)
	cv2.waitKey(0)

	h, w = img.shape[0], img.shape[1]
	mat = numpy.full((h, w + 6000), numpy.uint8(255))

	mat_x = 0
	for c in range(w):
		for r in range(h):
			if img[r, c] == 0:
				span = flood_fill(img, mat, r, c, mat_x + 30)
				mat_x = mat_x + 30 + span
				break

	mat = mat[: , : mat_x + 15]


	# for r in range(mat.shape[0]):
	# 	for c in range(mat.shape[1]):
	# 		if mat[r, c] == 150:
	# 			mat[r, c] = 255

	cv2.imshow("contour", mat)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return mat

if __name__ == "__main__":
	img = cv2.imread("Drawing.png", 0)
	ret3,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	kernel = numpy.ones((5,5),numpy.uint8)
	img = cv2.erode(img, kernel, iterations = 1)

	img = spacing(img)

	