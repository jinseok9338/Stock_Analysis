import OpenDartReader
import pandas as pd
import re
import os
import Get_Annual_Report

api_key = '1bb59e2a4ed4ced80e181370f312d48a424d4394'
dart = OpenDartReader(api_key)

rootdir = "/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/Stock_codes_name2/"
rootdir_for_result = "/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/finstate/{year}"
files = ["Codes_2013.csv","Codes_2014.csv","Codes_2015.csv","Codes_2016.csv","Codes_2017.csv","Codes_2018.csv","Codes_2019.csv"]
code_csv_files = [rootdir+file for file in files]
years = ["2015","2016","2017","2018","2019"]



def get_annual_report(code_csv,year):
    df = pd.read_csv(code_csv, dtype={'종목코드': str})
    for index, row in df.iterrows():
        code = row["종목코드"]
        name = row["종목명"]
        print(code,name)
        try:
            if type(dart.finstate_all(code, year, reprt_code='11011')).__name__ != "NoneType":
                dart_finstate = dart.finstate_all(code, year, reprt_code='11011')
                print("Yes for "+str(code)+" "+name + " 1")

            elif type(Get_Annual_Report.get_finstate_income_state(code, year,name)).__name__ != "NoneType":
                dart_finstate = Get_Annual_Report.get_finstate_income_state(code, year,name)
                print("Yes for "+str(code)+" "+name + " 2")

            else:
                print("No Annual Report for"+str(code)+name)
                raise SystemExit
            print(dart_finstate)
        except:
            pass
        try:
            if not os.path.exists(rootdir_for_result.format(year = str(year))):
                os.makedirs(rootdir_for_result.format(year = str(year)))
            dart_finstate.to_csv(rootdir_for_result.format(year = str(year))+"/{year}_{code}_{name}.csv".format(year = str(year),code=str(code),name = name), encoding="utf-8-sig")
        except:
            pass

for i in range(len(years)):
    code_csv = code_csv_files[i]
    year = years[i]
    if year == "2013" or year == "2014":
        year = "2015"
    get_annual_report(code_csv,year)











