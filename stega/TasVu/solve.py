#!/usr/bin/python3

from PIL import Image
import sys

def usage():
	if len(sys.argv) != 4:
		print(f"Usage : {sys.argv[0]} image_1.png image_2.png output.png")
		exit()
	else:
		return sys.argv[1],sys.argv[2],sys.argv[3]

def merge_pixel(px1, px2):
	px_black = (255,255,255,255)
	if px1 == px_black or px2 == px_black:
		return px_black
	return (0,0,0,255)

if __name__ == '__main__':
	image_1, image_2, image_output = usage()
	im1 = Image.open(image_1)
	im2 = Image.open(image_2)
	result = Image.new(mode="RGBA", size=(im1.width,im1.height))
	print(f"w : {im1.width} h : {im1.height} mode : {im1.mode}")
	print(f"w2 : {im2.width} h : {im2.height} mode : {im2.mode}")

	px1 = im1.load()
	px2 = im2.load()
	result_px = result.load()
	for i in range(0,im1.width,1):
		for j in range(0,im1.height,1):
			result_px[i,j] = merge_pixel(px1[i,j],px2[i,j])

	result.save(image_output)
