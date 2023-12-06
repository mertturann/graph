import os
import pandas as pd

def check_column_in_worksheets(basedir,folder_name, file_name, column_name):
    dir = f"{basedir}\{folder_name}"
    file_path = os.path.join(dir, file_name)

    try:
        excel_file = pd.ExcelFile(file_path)
        worksheets = excel_file.sheet_names

        for worksheet in worksheets:
            excel_data = pd.read_excel(file_path, sheet_name=worksheet)
            columns = excel_data.columns.tolist()

            if column_name in columns:
                print(f"{column_name} sütunu, {worksheet} çalışma sayfasında bulundu.")
            else:
                print(f"{column_name} sütunu, {worksheet} çalışma sayfasında bulunamadı.")
    except FileNotFoundError:
        print(f"{file_name} dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Örnek kullanım
basedir="C:\\Users\\User\\Documents\\DEEPSOIL 7\\results\\"
folder="A2"
dosya="Results_profile_0_motion_A-Denali, Alaska-TAPS Pump Station #08 M=7.9-EL.xlsx"
sütun="PSA (g)"

check_column_in_worksheets(basedir,folder, dosya, sütun)
