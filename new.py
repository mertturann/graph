import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QListWidget, QTableView, QLabel, QFileDialog
from PyQt6.uic import loadUi
from functions import list_files, list_folders
HOME_PATH = os.path.expanduser('~\Documents\DEEPSOIL 7')
dirsarray = []
excelsarray = []
layersarray = []

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI dosyasını yükle
        loadUi("new.ui", self)
     
        # QMainWindow içeriğini ayarla
        self.setWindowTitle("PyQt6 UI Örneği")

        self.initUiElements()
        self.interactions()
        self.finish.clicked.connect(self.test)
    
        self.all_selections = []

    
    def dataArray(self,value: str):
        self.dirs = []
        self.excels = []
        self.layers = []
        if value == "dir":
            return self.dirs
        if value == "files":
            self.files
        if value == "layers":     
            self.layers
        else:
            pass     
      
    def test(self):
        print ("hello")
        
        
    def initUiElements(self):
        self.save = self.findChild(QPushButton, "pushButton")
        self.finish = self.findChild(QPushButton, "pushButton_2")
        self.browse = self.findChild(QPushButton, "pushButton_3")
        self.dir = self.findChild(QComboBox, "comboBox")
        self.excel = self.findChild(QListWidget, "listWidget")
        self.excel.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.layer = self.findChild(QListWidget, "listWidget_2")
        self.layer.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.table = self.findChild(QTableView, "tableView")
        self.info = self.findChild(QLabel, "label_4")

    def interactions(self):
        self.browse.clicked.connect(self.browsedir)
        self.finish.clicked.connect(self.finish_selection)
        self.save.clicked.connect(self.save_selection)
        self.dir.currentIndexChanged.connect(self.initfiles)
        self.excel.clicked.connect(self.get_selected_excels)
        self.layer.clicked.connect(self.get_selected_layers)
        
    def addlayers(self):
        self.layer.clear()
        layers = ["Layer 1","Layer 2","Layer 3","Layer 4","Layer 5","Layer 6","Layer 7","Layer 8","Layer 9","Layer 10","Layer 11","Layer 12","Layer 13","Layer 14","Layer 15","Layer 16","Layer 17","Layer 18","Layer 19","Layer 20"]
        self.layer.addItems(layers) 
        
    def get_selected_excels(self):
        data = []
        selected_indexes = self.excel.selectedIndexes()        
        for index in selected_indexes:
            selected_item = index.data()
            data.append(selected_item)
        excelsarray.extend(data)        
        
    def get_selected_layers(self):
        data = []
        selected_indexes = self.layer.selectedIndexes()        
        for index in selected_indexes:
            selected_item = index.data()
            data.append(selected_item)
        layersarray.extend(data)    
            
        """  
        def get_selected_dirs(self):
        selected_indexes = self.dir.currentIndex()      
        for index in selected_indexes:
            data = []
            selected_item = index.data()
            data.append(selected_item)
        dirsarray.append(data)  
        """                 
    def finish_selection(self):
            print("Seçimler Kaydedildi:")
            for index, selections in enumerate(self.all_selections, start=1):
                print(f"Seçim {index}:")
                print(f"Combobox: {selections[0]}")
                print(f"Liste 1 Seçimleri: {selections[1]}")
                print(f"Liste 2 Seçimleri: {selections[2]}")
                print("----------------------")               
    def browsedir(self):
        self.cleardata()
        self.path = QFileDialog.getExistingDirectory(self,directory=HOME_PATH)
        folders = list_folders(self.path)
        self.dir.addItems(folders)
        
    def initfiles(self):
        self.cleardata()
        text = self.dir.currentText()
        filespath = f"{self.path}/{text}"
        files = list_files(filespath)
        self.excel.addItems(files)
        self.addlayers()
        
    def cleardata(self):
        self.layer.clearSelection()
        self.excel.clearSelection()
    
    def savedata(self):
        self.get_selected_excels()
        self.get_selected_layers()
        self.cleardata()
        print (excelsarray)

    def save_selection(self):
        combo_text = self.dir.currentText()
        list_1_selected = [self.excel.item(i).text() for i in range(self.excel.count()) if self.excel.item(i).isSelected()]
        list_2_selected = [self.layer.item(i).text() for i in range(self.layer.count()) if self.layer.item(i).isSelected()]

        self.all_selections.append((combo_text, list_1_selected, list_2_selected))

        self.excel.clearSelection()
        self.layer.clearSelection()
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
