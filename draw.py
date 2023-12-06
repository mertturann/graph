from functions import getperiod, list_files, draw_excel_chart
from datetime import datetime

dirs=[["A1","A2","A3","A4","A5","A6"],["A7","A8","A9","A10","A11","A12"],["A13","A14","A15","A16","A17","A18"]]
basedir = f"C:\\Users\\User\\Desktop\\results"

dosya_yolu = "period.xlsx"
calisma_sayfasi = "Sayfa1"
sutun_adi = "Period (sec)"
period = getperiod(dosya_yolu, calisma_sayfasi, sutun_adi)

folders = f"{basedir}\A1"
files = list_files(folders)
for file in files:
    pass
    #print (file)


testexcel = "Results_profile_0_motion_a-10410337- la fresa m=4.7-el.xlsx"
yvalues = []      
"""
for dir in dirs:
    for dirx in dir:
        path = f"{basedir}\{dirx}\{testexcel}"
        for i in range(1,5):
            worksheet = f"Layer {i}"
            psa = getperiod(file_path=path,worksheet_name=worksheet,column_name="PSA (g)")
            yvalues.append(psa)
        #print
        pass
"""    
for dir in dirs[0]:
    path = f"{basedir}//{dir}//{testexcel}"
    psa = getperiod(file_path=path,worksheet_name="Layer 1",column_name="PSA (g)")
    yvalues.append(psa)
        #print
draw_excel_chart(file_path="./period.xlsx",x_column="Period (sec)",y_columns=yvalues,output_file="./output.xlsx")        
