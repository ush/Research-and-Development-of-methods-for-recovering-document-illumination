import os
import re

raw_files_list = []
trained_files_list = [] 

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

for root, _, files in os.walk("../test_results/raw_Tesseract/"):
	for fil in sorted(files, key=natural_keys):
		raw_files_list.append(os.path.join(root,fil))

for root, _, files in os.walk("../test_results/trained_Tesseract/"):
	for fil in sorted(files, key=natural_keys):
		trained_files_list.append(os.path.join(root,fil))

for i in range(0,len(raw_files_list)):
	print(raw_files_list[i])
	print(trained_files_list[i])
	raw_data = open(raw_files_list[i], "rt").read()
	trained_data = open(trained_files_list[i], "rt").read()
	raw_num = len(raw_data.split())
	trained_num = len(trained_data.split())
	if raw_num == 0:
		raw_num += 1
	percent = int(((trained_num * 100)/raw_num)) - 100 
	msg = "Percent difference between raw and trained ST-CGAN on image " + str(i+1) + " is: " + str(percent) + "%\n" 
	open("../test_results/statistics.txt", "a").write(msg)

print("Finished")

