import OpenDartReader
import pandas as pd
import re
import os

api_key = '1bb59e2a4ed4ced80e181370f312d48a424d4394'

dart = OpenDartReader(api_key)
rootdir = "/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/Stock_codes_names/"
rootdir_for_result = "/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/finstate/{year}/"
files = ['Codes_20'+str(num) for num in range(13,20)]
year_pattern = "^Codes_([0-9]*)\.csv$"
for file in files:
    csv_file_path = rootdir+file
    df = pd.read_csv(csv_file_path)
    year = re.findall(year_pattern,file)[0]
    for index, row in df.iterrows():
        code = row["종목코드"]
        name = row["종목명"]

        if year == 2013:
            year = 2015
            dart_finstate = dart.finstate_all(str(code), year, reprt_code='11011')
            if not dart_finstate:
                dart_finstate = dart.finstate_all(name, year, reprt_code='11011')
            dart_finstate = dart_finstate[['fs_nm', 'sj_nm','account_nm','bfefrmtrm_dt','bfefrmtrm_amount']]
            year = 2013
            if not os.path.exists(rootdir_for_result.format(str(year))):
                os.makedirs(rootdir_for_result.format(str(year)))
            dart_finstate.to_csv(rootdir_for_result+"{year}{code}{name}.csv".format(year = str(year),code=str(code),name = name), encoding="utf-8-sig")

        elif year == 2014:
            year = 2015
            dart_finstate = dart.finstate_all(str(code), year, reprt_code='11011')
            if not dart_finstate:
                dart_finstate = dart.finstate_all(name, year, reprt_code='11011')
            dart_finstate = dart_finstate[['fs_nm', 'sj_nm', 'account_nm', 'frmtrm_dt', 'frmtrm_amount']]
            year = 2014
            if not os.path.exists(rootdir_for_result.format(str(year))):
                os.makedirs(rootdir_for_result.format(str(year)))
            dart_finstate.to_csv(rootdir_for_result+"{year}{code}{name}.csv".format(year = str(year),code=str(code),name = name), encoding="utf-8-sig")


        else:
            dart_finstate = dart.finstate_all(str(code), year, reprt_code='11011')
            if not dart_finstate:
                dart_finstate = dart.finstate_all(name, year, reprt_code='11011')
            dart_finstate = dart_finstate[['fs_nm', 'sj_nm', 'account_nm', 'thstrm_dt', 'thstrm_amount']]
            if not os.path.exists(rootdir_for_result.format(str(year))):
                os.makedirs(rootdir_for_result.format(str(year)))
            dart_finstate.to_csv(rootdir_for_result+"{year}{code}{name}.csv".format(year = str(year),code=str(code),name = name), encoding="utf-8-sig")










