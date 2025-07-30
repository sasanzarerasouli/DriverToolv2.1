import os
import sys
import subprocess
import ctypes
from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea,
    QLabel, QFileDialog, QMessageBox, QTextEdit, QFrame, QDialog,
    QCheckBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Driver file selection with checkbox
class FileSelectionDialog(QDialog):
    def __init__(self, file_paths, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Files to Install")
        # self.setFixedSize(400, 500)
        self.setGeometry(350, 150, 400, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Main vertical layout
        main_layout = QVBoxLayout(self)

        # Title
        title = QLabel("Choose <b>DRIVERS</b> to install:")
        title.setFont(QFont("Segoe UI", 10))
        title.setStyleSheet("color: black;")
        main_layout.addWidget(title)

        # Scrollable area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)

        self.checkboxes = []
        for path in file_paths:
            cb = QCheckBox(os.path.basename(path))
            cb.setFont(QFont("Segoe UI", 9))
            cb.setChecked(True)
            scroll_layout.addWidget(cb)
            self.checkboxes.append((cb, path))

        scroll_layout.addStretch()  # Keeps layout tidy
        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

        # Confirm button
        confirm_btn = QPushButton("Install Selected Ddivers")
        confirm_btn.setFont(QFont("Segoe UI", 10))
        confirm_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: skyblue;
                color: white;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: blue;
            }
        """)
        confirm_btn.clicked.connect(self.accept)
        main_layout.addWidget(confirm_btn)

    def get_selected_paths(self):
        return [p for cb, p in self.checkboxes if cb.isChecked()]


# Main class of application
class DriverTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DriverTool")
        self.setGeometry(300, 100, 800, 400)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.init_ui()
        

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Buttons panel
        button_frame = QFrame()
        button_layout = QVBoxLayout(button_frame)

        # Title of section in left panel
        title = QLabel("Driver Tool")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(title)

        # Description 
        note = QLabel("Built with your comfort in mind.")
        note.setFont(QFont("Segoe UI", 9))
        note.setStyleSheet("color: gray;")
        note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(note)

        # Buttons GUI
        export_btn = QPushButton("Export Drivers")
        install_btn = QPushButton("Install Drivers")
        for btn in (export_btn, install_btn):
            btn.setFont(QFont("Segoe UI", 10))
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: skyblue;
                    color: white;
                    padding: 10px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: blue;
                }
            """)
        export_btn.clicked.connect(self.export_drivers)
        install_btn.clicked.connect(self.install_drivers)
        button_layout.addWidget(export_btn)
        button_layout.addWidget(install_btn)
        button_layout.addStretch()

        # Creator name and description in buttom-left
        powered = QLabel("Powered by Sasan Zare\nFor PAYAMED Users")
        powered.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold, italic=True))
        powered.setStyleSheet("color: gray;")
        powered.setAlignment(Qt.AlignmentFlag.AlignLeft)
        button_layout.addWidget(powered)

        # Log panel
        log_frame = QFrame()
        log_layout = QVBoxLayout(log_frame)

        # Attention note on right pannel 
        des_label = QLabel("This Application must be Run As Administrator")
        des_label.setFont(QFont("Segoe UI", 13, QFont.Weight.Bold))
        des_label.setStyleSheet("color: red;")
        des_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        log_layout.addWidget(des_label)    

        # Logbox title
        log_title = QLabel("Logs Box:")
        log_title.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        log_layout.addWidget(log_title)

        # Real-time log viewer
        self.output_box = QTextEdit()
        self.output_box.setFont(QFont("Consolas", 9))
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: white; border: 1px solid gray;")
        log_layout.addWidget(self.output_box)
        
        # version lable in buttom-right
        version_label = QLabel("Version: 2.1 ")
        version_label.setFont(QFont("Segoe UI", 7, QFont.Weight.Bold))
        version_label.setStyleSheet("color: gray;")
        version_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        log_layout.addWidget(version_label)

        # main layout
        main_layout.addWidget(button_frame, 2)
        main_layout.addWidget(log_frame, 5)
        self.setLayout(main_layout)

    # Log massages methode. import logs from cmd terminal.(process events)
    def log_message(self, message):
        self.output_box.append(message)
        QApplication.processEvents()

    # Export driver button methode
    def export_drivers(self):
        dest = QFileDialog.getExistingDirectory(self, "Select folder to export drivers")
        if dest:
            self.log_message(f"Exporting drivers to: {dest}")
            cmd = ['dism', '/online', '/export-driver', f'/destination:{dest}']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                self.log_message(line.strip())
            process.wait()
            if process.returncode == 0:
                QMessageBox.information(self, "Success", "Driver backup completed successfully!")
            else:
                QMessageBox.critical(self, "Error", "An error occurred during driver backup.")
            self.log_message("Export operation finished.\n")


    # Install driver button methode
    def install_drivers(self):
        src = QFileDialog.getExistingDirectory(self, "Select folder to install drivers")
        if src:
            file_paths = []
            for root, _, files in os.walk(src):
                for file in files:
                    if file.lower().endswith(".inf") or file.lower().endswith(".com"):
                        file_paths.append(os.path.join(root, file))

            if not file_paths:
                QMessageBox.warning(self, "No Files", "No .INF or .COM files found.")
                return

            dialog = FileSelectionDialog(file_paths, self)
            if dialog.exec():
                selected = dialog.get_selected_paths()
                self.log_message(f"Installing from: {src}")
                for path in selected:
                    name = os.path.basename(path)
                    self.log_message(f"Installing: {name}")
                    if path.endswith(".inf"):
                        cmd = ['pnputil', '/add-driver', path, '/install']
                    elif path.endswith(".com"):
                        cmd = [path]
                    try:
                        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                        self.log_message(result.stdout.strip())
                    except Exception as e:
                        self.log_message(f"Error with {name}: {e}")
                QMessageBox.information(self, "Done", "Driver installation completed.")
                self.log_message("Installation operation finished.\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DriverTool()
    window.show()
    sys.exit(app.exec())
