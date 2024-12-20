import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from student_management import StudentManagementWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentManagementWindow()
    window.show()
    sys.exit(app.exec()) 