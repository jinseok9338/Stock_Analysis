import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


#year + 1 을 해야 그 전 사업 보고서 재무제표가 나옴
def search_urls(code,year,name):  #take code and return url of Annual Report
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
	url_with_code = "http://dart.fss.or.kr/dsab002/search.ax?reportName=사업보고서&&maxResults=100&&startDate={year}0201&&endDate={year}1231&&textCrpNm={code}".format(year= year,code=code)
	url_with_name = "http://dart.fss.or.kr/dsab002/search.ax?reportName=사업보고서&&maxResults=100&&startDate={year}0201&&endDate={year}1231&&textCrpNm={name}".format(year= year,name=name)
	response = requests.get(url_with_code)
	soup = bs(response.content.decode('utf-8','replace'),features='html.parser')
	string_list = soup.findAll('a',title = "사업보고서 공시뷰어 새창", href=True)

	#find the url with name if you can't find it with code
	if string_list == []:
		response = requests.get(url_with_name)
		soup = bs(response.content.decode('utf-8','replace'),features='html.parser')
		string_list = soup.findAll('a',title = "사업보고서 공시뷰어 새창", href=True)

	string_list_to_string = ''.join(map(str, string_list))
	json_pattern = "\/dsaf001\/main\.do\?rcpNo=[0-9]*"


	url_list_to_anuual_report = "http://dart.fss.or.kr"+re.findall(json_pattern, string_list_to_string)[0]

	return url_list_to_anuual_report  #url of entire Report


def return_financial_report(url): #Return the income Statement and financial statement URL
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
	response = requests.get(url)
	soup = bs(response.content.decode('utf-8','replace'),features="html.parser")
	soup_string = str(soup)

	pattern = """{
			text: "[0-9]*\. 연결재무제표",
			id: "[0-9]*",
			cls: "text",
			listeners: {
				click: function\(\) {viewDoc\('(?P<rcpNo>[0-9]*)', '(?P<dcmNo>[0-9]*)', '(?P<eleId>[0-9]*)', '(?P<offset>[0-9]*)', '(?P<length>[0-9]*)', '(?P<dtd>dart[0-9]*\..*)'\);}
			}"""

	c_list =re.findall(pattern, soup_string)[0]
	url = "http://dart.fss.or.kr//report/viewer.do?rcpNo={rcpNo}&dcmNo={dcmNo}&eleId={eleId}&offset={offset}&length={length}&dtd={dtd}".format(rcpNo=c_list[0],dcmNo=c_list[1],eleId=c_list[2],offset=c_list[3],length=c_list[4],dtd=c_list[5])

	return url
	
#url = "http://dart.fss.or.kr/dsaf001/main.do?rcpNo=20160330003536"
#print(return_financial_report(url))
#url = "http://dart.fss.or.kr//report/viewer.do?rcpNo=20160330004092&dcmNo=5028918&eleId=13&offset=872178&length=89815&dtd=dart3.xsd"

def page_to_csv(url):
	
	df = pd.read_html(url)
	new_df = [table for table in df if len(table.columns) == 4]
	result = pd.concat(new_df, ignore_index=True)
	result = pd.DataFrame(result)
	return result



def get_finstate_income_state(code,year): # This is the function for the income statement Do not use the functions above
	year = int(year)+1
	url_list_to_anual_report = search_urls(code,str(year),name)
	finstate_url = return_financial_report(url_list_to_anual_report)
	df_for_csv = page_to_csv(finstate_url)
	return df_for_csv






















