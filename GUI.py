import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QComboBox, QMessageBox
from PyQt6.QtCore import QStandardPaths
from ytdownload import download_stream

class YoutubeDownloaderGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Widgets
        self.url_label = QLabel("YouTube URL:")
        self.url_input = QLineEdit()

        self.path_label = QLabel("Save Path:")
        self.path_input = QLineEdit()
        self.path_button = QPushButton("Select Path")
        self.path_button.clicked.connect(self.select_path)

        self.name_label = QLabel("File Name:")
        self.name_input = QLineEdit()

        self.format_label = QLabel("File Format:")
        self.format_combobox = QComboBox()
        self.format_combobox.addItems(["mp4", "mp3", "wav"])

        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.download)


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.path_label)
        layout.addWidget(self.path_input)
        layout.addWidget(self.path_button)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.format_label)
        layout.addWidget(self.format_combobox)
        layout.addWidget(self.go_button)
        layout.setSpacing(10)
        self.setLayout(layout)
        
        self.setWindowTitle("YouTube Downloader")
        self.resize(600, 400)

        # Apply style sheet for a more visually appealing look
        self.setStyleSheet(
            """
            QWidget {
                background-color: #2E2E2E;  /* Dark gray background */
                color: #FFFFFF;  /* White text color */
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 5px;
                font-size: 12px;
                background-color: #424242;  /* Darker gray background for input fields */
                color: #FFFFFF;  /* White text color for input fields */
            }
            QPushButton {
                padding: 8px;
                font-size: 14px;
                background-color: #4CAF50;  /* Green button color */
                color: white;
                border: 1px solid #4CAF50;
                border-radius: 4px;
            }
            QComboBox {
                padding: 5px;
                font-size: 12px;
                background-color: #424242;  /* Darker gray background for combo box */
                color: #FFFFFF;  /* White text color for combo box */
            }
            """
        )

    # Set spacing between widgets


    def select_path(self):
    
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation))
        if folder_path:
            self.path_input.setText(folder_path)



    def download(self):
        url = self.url_input.text()
        path = self.path_input.text()
        name = self.name_input.text()
        format = self.format_combobox.currentText()

        try:
            result = download_stream(url, path, name, format)
            #check if result starts with "ERROR"
            if result.startswith("ERROR"):
                QMessageBox.critical(self, "Error", result)
            else:
                QMessageBox.information(self, "Success", f"Download successful!\nFile saved at:\n{result}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred:\n{str(e)}")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YoutubeDownloaderGUI()
    window.show()
    sys.exit(app.exec())

