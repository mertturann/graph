import pandas as pd
import os
import matplotlib.pyplot as plt
from functions import getperiod, read_y_values_from_folders, draw_combined_graph, list_files
cwd = os.getcwd()
dosya_yolu = "period.xlsx"
calisma_sayfasi = "Sayfa1"
sutun_adi = "Period (sec)"
period = getperiod(dosya_yolu, calisma_sayfasi, sutun_adi)

# Örnek kullanım

klasorler = [

    
    "C:\\Users\\User\\Desktop\\code\\graph\\results\\A13",
    "C:\\Users\\User\\Desktop\\code\\graph\\results\\A14",
    "C:\\Users\\User\\Desktop\\code\\graph\\results\\A15",
    "C:\\Users\\User\\Desktop\\code\\graph\\results\\A16",
    "C:\\Users\\User\\Desktop\\code\\graph\\results\\A17",
    "C:\\Users\\User\\Desktop\\code\\graph\\results\\A18",
        

]


layers = [
    "Layer 1",
    "Layer 2",
    "Layer 3",
    "Layer 4"
]


# Y ekseni değerlerini oku
#y_verileri = read_y_values_from_folders(klasorler, dosya_adi, calisma_sayfasi, y_sutunu)

# Grafik oluştur
#draw_combined_graph(x_degeri, y_verileri, "grafik")
f = f"{cwd}\\results\\deney\\A1"
depremler = list_files(f)


ydata = []
"""
for deprem in depremler:
    for layer in layers:
        for klasor in klasorler:
            y = read_y_values_from_folders(folder=f"{cwd}\\results\\{klasor}", file_name=deprem, worksheet_name=layer, y_column=y_sutunu)
            ydata.append(y)
        graphname = f"{deprem} {layer}.png"
        draw_combined_graph(x_values=x_degeri,y_values=ydata,graphname=graphname,title=graphname)

         
y = read_y_values_from_folders(folder=f"{cwd}\\results\\A3", file_name=dosya_adi, worksheet_name="Layer 1", y_column=y_sutunu)
graphname = f"{dosya_adi} Layer 1.png"
ydata.append(list(y))
draw_combined_graph(x_values=x_degeri,y_values=y,graphname=graphname,title=graphname)
ydata.clear()
ydata.clear()
"""                        
for layer in layers:
    for deprem in depremler:
        dirname = deprem.replace("Results_profile_0_motion_","")
        dirname = dirname.replace(".xlsx","")
        if not os.path.exists("sonuclar/"+dirname):
            os.mkdir("sonuclar/"+dirname)
        y = read_y_values_from_folders(folders=klasorler,file_name=deprem,worksheet_name=layer,y_column="PSA (g)")
        grafik = f"{layer}.png"
        draw_combined_graph(x_values=period,y_values=y,graphname=grafik,title=grafik,dirname=dirname)
                
                