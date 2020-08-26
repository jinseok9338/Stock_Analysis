import pandas as pd
import re
files = ["Codes_2013.csv","Codes_2014.csv","Codes_2015.csv","Codes_2016.csv","Codes_2017.csv","Codes_2018.csv","Codes_2019.csv"]
rootdir = "/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/Stock_codes_names/"

csv_file_dir = [rootdir+file for file in files]
for csv in csv_file_dir:
    csv_file = pd.read_csv(csv)[["종목코드","종목명"]]
    column_1 = []
    column_2 = []
    title = re.findall("Codes_[0-9]*\.csv",csv)[0]

    for index, row in csv_file.iterrows():
        a = str(row["종목코드"])
        b = row["종목명"]
        while len(a) <6:
           a = "0"+a
        column_1.append(str(a))
        column_2.append(b)
    new_csv = pd.DataFrame({"종목코드":column_1,
                            "종목명":column_2})
    new_csv.to_csv("/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/Stock_codes_name2/"+title,encoding="utf-8-sig")
