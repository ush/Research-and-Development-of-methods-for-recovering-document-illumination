import cv2
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--gt_path', type=str)
parser.add_argument('--rm_path', type=str)
parser.add_argument('--img_num', type=str)
parser.add_argument('--out_path', type=str)
args = parser.parse_args()

def mse(img1, img2):
   h, w = img1.shape[:2]
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse

img_gt = cv2.imread(args.gt_path)
img_rm = cv2.imread(args.rm_path)
rmse = np.sqrt(mse(img_gt, img_rm))
line = args.img_num[:-4] + ", " + str(rmse) + "\n"

with open(args.out_path , 'a') as file:
	file.write(line)
