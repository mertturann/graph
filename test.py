import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QListWidget, QPushButton

class SelectionForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seçim Formu")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Seçenek 1", "Seçenek 2", "Seçenek 3"])
        self.layout.addWidget(self.combo_box)

        self.list_widget_1 = QListWidget()
        self.list_widget_1.addItems(["Öğe 1", "Öğe 2", "Öğe 3", "Öğe 4"])
        self.list_widget_1.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.layout.addWidget(self.list_widget_1)

        self.list_widget_2 = QListWidget()
        self.list_widget_2.addItems(["Item A", "Item B", "Item C", "Item D"])
        self.list_widget_2.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.layout.addWidget(self.list_widget_2)

        self.save_button = QPushButton("Seçimi Kaydet")
        self.save_button.clicked.connect(self.save_selection)
        self.layout.addWidget(self.save_button)

        self.finish_button = QPushButton("Kullanıcı Seçimi Bitir")
        self.finish_button.clicked.connect(self.finish_selection)
        self.layout.addWidget(self.finish_button)

        self.selected_items = []

    def save_selection(self):
        combo_text = self.combo_box.currentText()
        list_1_selected = [self.list_widget_1.item(i).text() for i in range(self.list_widget_1.count()) if self.list_widget_1.item(i).isSelected()]
        list_2_selected = [self.list_widget_2.item(i).text() for i in range(self.list_widget_2.count()) if self.list_widget_2.item(i).isSelected()]

        self.selected_items.append((combo_text, list_1_selected, list_2_selected))

        self.list_widget_1.clearSelection()
        self.list_widget_2.clearSelection()

    def finish_selection(self):
        print("Seçimler Kaydedildi:")
        for index, selection in enumerate(self.selected_items, start=1):
            print(f"Seçim {index}:")
            print(f"Combobox: {selection[0]}")
            print(f"Liste 1 Seçimleri: {selection[1]}")
            print(f"Liste 2 Seçimleri: {selection[2]}")
            print("----------------------")

        # Seçimleri sıfırla
        self.selected_items = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectionForm()
    window.show()
    sys.exit(app.exec())
