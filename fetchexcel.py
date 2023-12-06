import os
import pandas as pd

def read_excel_column(folder_name, file_name, worksheet_name, column_name):
    # Verilen klasördeki dosya yolunu oluştur
    file_path = os.path.join(folder_name, file_name)

    try:
        # Excel dosyasını oku
        excel_data = pd.read_excel(file_path, sheet_name=worksheet_name)

        # Belirtilen sütunu seç
        if column_name in excel_data.columns:
            selected_column = excel_data[column_name].dropna().tolist()
            return selected_column
        else:
            return "Belirtilen sütun bulunamadı."
    except FileNotFoundError:
        return f"{file_name} dosyası bulunamadı."
    except Exception as e:
        return f"Hata oluştu: {e}"

# Örnek kullanım
folder_name="C:\\Users\\User\\Documents\\DEEPSOIL 7\\results\\A3\\"
file_name="Results_profile_0_motion_A-Denali, Alaska-TAPS Pump Station #08 M=7.9-EL.xlsx"
worksheet_name="Layer 3"
column_name="PSA (g)"

veriler = read_excel_column(folder_name, file_name, worksheet_name, column_name)
if isinstance(veriler, list):
    print(f"{file_name} dosyasındaki {worksheet_name} çalışma sayfasında {column_name} sütunundaki veriler:")
    print(veriler)
else:
    print(veriler)


