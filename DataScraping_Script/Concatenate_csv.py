import re
import os
import pandas as pd

num_list = [13,14,15,16,17,18,19]
rootdir = "/Users/jasonseo/Desktop/JasonMacBookAir/Stock_Data_Analysis_Project/Data_Folder/Stock_name_and_code_number/"
for num in num_list: 
	pattern = re.compile("^Data20{number}(0[28])\d*\.csv$".format(number = num))
	try:
		path_list = []
		for root, dirs, files in os.walk(rootdir):
			for file in files:
				if pattern.match(file):
					path_list.append(rootdir+file)
		csv_1 = pd.read_csv(path_list[0])[["종목코드","종목명"]]
		csv_2 = pd.read_csv(path_list[1])[["종목코드","종목명"]]
		big_frame = pd.concat([csv_1,csv_2],ignore_index=True)
		big_frame.drop_duplicates(subset ="종목코드",keep = "first", inplace = True) 
		big_frame.to_csv("/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/Codes_20{num}.csv".format(num=num),encoding="utf-8-sig")


				
	except Exception:
		raise Exception