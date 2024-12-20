from PySide6.QtWidgets import QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt

class StudentDialog(QDialog):
    def __init__(self, parent=None, student_data=None):
        super().__init__(parent)
        
        # 设置窗口标志
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowModality(Qt.WindowModal)
        
        # 加载UI
        loader = QUiLoader()
        self.ui = loader.load('student_dialog.ui')
        
        # 设置对话框大小和布局
        self.resize(400, 300)
        layout = self.layout()
        if not layout:
            from PySide6.QtWidgets import QVBoxLayout
            layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 如果有学生数据，填充表单
        if student_data:
            self.ui.student_id.setText(student_data[0])
            self.ui.name.setText(student_data[1])
            self.ui.gender.setCurrentText(student_data[2])
            self.ui.age.setValue(int(student_data[3]))
            self.ui.class_name.setText(student_data[4])
            
        # 连接信号
        self.ui.save_button.clicked.connect(self.accept)
        self.ui.cancel_button.clicked.connect(self.reject)
        
    def get_student_data(self):
        """获取表单数据"""
        return [
            self.ui.student_id.text(),
            self.ui.name.text(),
            self.ui.gender.currentText(),
            str(self.ui.age.value()),
            self.ui.class_name.text()
        ] 