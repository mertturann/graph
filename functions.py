import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)

def list_folders(directory: str):
    directory = directory.replace("file://","")
    folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    return folders

def list_files(directory: str):
    directory = directory.replace("file://","")
     #if f.endswith(".xlsx")
    folders = [f for f in os.listdir(directory)]
    return folders

def getcurrentime():
    c = datetime.now()
    current_time = c.strftime('%H:%M')
    return str(current_time)


def getperiod(file_path, worksheet_name, column_name):
    try:
        excel_data = pd.read_excel(file_path, sheet_name=worksheet_name)
        selected_column = excel_data[column_name].dropna().tolist()
        return selected_column
    except FileNotFoundError:
        return f"{file_path} dosyası bulunamadı."
    except Exception as e:
        return f"Hata oluştu: {e}"



def draw_excel_chart(file_path, x_column, y_columns, output_file):
    try:
        excel_data = pd.read_excel(file_path)
        
        # X ekseni için verileri al
        x_values = excel_data[x_column]

        wb = Workbook()
        ws = wb.active

        # Y ekseni için verileri al ve grafik olarak çiz
        chart = ScatterChart()
        chart.title = "Excel Tablosundan Grafik Oluşturma"

        for y_column in y_columns:
            y_values = excel_data[y_column]
            plt.plot(x_values, y_values, label=y_column)  # Farklı renkler için label kullanılır

            values = Reference(ws, min_col=1, min_row=1, max_row=len(x_values))
            series = Series(values, title=y_column)
            chart.series.append(series)

        ws.add_chart(chart, "D1")
        wb.save(output_file)
        plt.show()

    except FileNotFoundError:
        print(f"{file_path} dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")


def read_y_values_from_folders(folders, file_name, worksheet_name, y_column):
    all_y_values = []

    for folder in folders:
        file_path = os.path.join(folder, file_name)
        if os.path.exists(file_path):
            try:
                excel_data = pd.read_excel(file_path, sheet_name=worksheet_name)
                y_values = excel_data[y_column].dropna().tolist()
                all_y_values.append(y_values)
            except Exception as e:
                print(f"{file_name} dosyasını okuma sırasında hata oluştu: {e}")
        else:
            print(f"{file_name} dosyası bulunamadı: {file_path}")

    return all_y_values
    

def draw_combined_graph(x_values, y_values,graphname: str, title: str,dirname: str):
    plt.figure(figsize=(15, 9))

    for idx, y_data in enumerate(y_values, start=13):
        plt.plot(x_values, y_data, marker='.' ,label=f"A{idx}")

    plt.xlabel("Periyot (X)")
    plt.ylabel("PSA (g) (y)")
    plt.title(str(title))
    plt.legend()
    plt.savefig(f"sonuclar/{dirname}/{graphname}")
    plt.close()


