import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gt_path', type=str)
parser.add_argument('--rm_path', type=str)
parser.add_argument('--img_num', type=str)
parser.add_argument('--out_path', type=str)
args = parser.parse_args()

img_gt = cv2.imread(args.gt_path)
img_rm = cv2.imread(args.rm_path)
psnr = cv2.PSNR(img_gt, img_rm)
line = args.img_num[:-4] + ", " + str(psnr) + "\n"

with open(args.out_path , 'a') as file:
	file.write(line)

