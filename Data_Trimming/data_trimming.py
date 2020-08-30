import pandas as pd
from glob import glob
import re
import os


code_year_name_pattern_from_filename = "\/Users\/jasonseo\/Desktop\/Project_Folder\/Stock_Analysis\/Data\/finstate\/[0-9]*\/[0-9]{4}_([0-9]*)_(.*[가-힣]*.*)\.csv"
years = ["2016","2017","2018","2019"]
filenames_for_csv_finstate = glob('/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/finstate/{year}/*')
dir_csv_stock_price ="/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/Stock_Price/marcap-{year}.csv"
output_dir_for_finstate_and_stockprice = "/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/Trimmed_Data/{year}/{code}{name}/"

for year in years:
    filenames_for_csv_finstate = glob('/Users/jasonseo/Desktop/Project_Folder/Stock_Analysis/Data/finstate/{year}/*'.format(year=year))

    for f in filenames_for_csv_finstate:
        print(f)
        code = re.findall(code_year_name_pattern_from_filename,f)[0][0]
        name = re.findall(code_year_name_pattern_from_filename,f)[0][1]
        print(code,name)
        csv_original_for_finstate = pd.read_csv(f)
        csv_original_stock_price = pd.read_csv(dir_csv_stock_price.format(year=year))
        try:
            if len(csv_original_for_finstate.columns) ==4:
                csv_motified_for_finstate =  csv_original_for_finstate[csv_original_for_finstate.columns[0:2]]
            else:
                csv_motified_for_finstate = csv_original_for_finstate[["account_nm","thstrm_amount"]]

            csv_motified_for_stock_price = csv_original_stock_price[csv_original_stock_price["Code"]==code]

            if not os.path.exists(output_dir_for_finstate_and_stockprice.format(year=year,code=code,name=name)):
                os.makedirs(output_dir_for_finstate_and_stockprice.format(year=year,code=code,name=name))

            csv_motified_for_finstate.to_csv((output_dir_for_finstate_and_stockprice+"{year}_{code}_{name}_finstate.csv").format(year = year,code=code,name=name),encoding="utf-8-sig")
            csv_motified_for_stock_price.to_csv((output_dir_for_finstate_and_stockprice+"{year}_{code}_{name}_stock_price.csv").format(year = year,code=code,name=name),encoding="utf-8-sig")
        except KeyError:
            print("Key Error for " +code)






