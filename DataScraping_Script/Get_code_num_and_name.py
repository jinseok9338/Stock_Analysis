# -*- coding: utf-8 -*-

import requests
import pandas as pd
from io import BytesIO
import re


num_list = range(20010101,20200000)
year_list = []
for a in num_list:
	if re.search("^20[0-1][0-9]0[2,8]11$",str(a)):
		year_list.append(re.search("^20[0-1][0-9]0[2,8]11$",str(a)).group(0))
print(year_list)


def name_and_code_num(year):
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
	headers2 = {'Referer': 'http://marketdata.krx.co.kr/mdi', "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
	url = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx'

	query_str_params={
	'name': 'fileDown',
	'filetype': 'xls',
	'url': 'MKD/03/0304/03040101/mkd03040101T3_01',
	'ind_tp_cd': '1',
	'idx_ind_cd': '028',
	'lang': 'ko',
	'compst_isu_tp': '1',
	'schdate': str(year),
	'pagePath': '/contents/MKD/03/0304/03040101/MKD03040101T3.jsp'        
	}

	r=requests.get(url,query_str_params, headers=headers)
	#print(r)
	#print(r.content) 
	gen_req_url='http://file.krx.co.kr/download.jspx'


	form_data = {
	        'code' : r.content
	}

	r = requests.post(gen_req_url, form_data, headers=headers2)
	df = pd.read_excel(BytesIO(r.content))
	
	try:
		if df.index[0] != None:
			df = df
	except IndexError:
		print("IndexError")
		year = int(year)
		year += 1
		print(year)
		df = name_and_code_num(year)

	return df

	

#for year in year_list:
for year in year_list:
	df = name_and_code_num(year)
	df.to_csv('/Users/jasonseo/Desktop/Data Folder/Data'+year+'.csv', sep=',', na_rep='NaN',encoding="utf-8-sig")







