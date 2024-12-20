from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtCore import Qt, QPoint
from PySide6.QtUiTools import QUiLoader
from student_dialog import StudentDialog

class StudentManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置无边框窗口
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 加载UI文件
        loader = QUiLoader()
        self.ui = loader.load('student_management.ui')
        self.setCentralWidget(self.ui)
        
        # 设置表格
        self.setup_table()
        
        # 连接信号和槽
        self.setup_connections()
        
        # 窗口拖动相关
        self._drag_pos = QPoint()
        
        # 添加示例数据
        self.students = [
            ["2024001", "张三", "男", "18", "计算机1班"],
            ["2024002", "李四", "女", "19", "计算机1班"],
            ["2024003", "王五", "男", "20", "计算机2班"],
            ["2024004", "赵六", "女", "18", "计算机2班"],
            ["2024005", "孙七", "男", "19", "计算机3班"],
        ]
        self.refresh_table()
        
    def mousePressEvent(self, event):
        """重写鼠标按下事件"""
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.pos()
            event.accept()
    
    def mouseMoveEvent(self, event):
        """重写鼠标移动事件"""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        """重写鼠标释放事件"""
        self._drag_pos = QPoint()
        event.accept()
        
    def setup_connections(self):
        """设置信号和槽的连接"""
        self.ui.add_button.clicked.connect(self.add_student)
        self.ui.edit_button.clicked.connect(self.edit_student)
        self.ui.delete_button.clicked.connect(self.delete_student)
        self.ui.search_button.clicked.connect(self.search_student)
        
        # 窗口控制按钮
        self.ui.minimizeButton.clicked.connect(self.showMinimized)
        self.ui.maximizeButton.clicked.connect(self.toggle_maximize)
        self.ui.closeButton.clicked.connect(self.close)
        
    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
    def setup_table(self):
        """设置表格"""
        headers = ["学号", "姓名", "性别", "年龄", "班级"]
        self.ui.table.setColumnCount(len(headers))
        self.ui.table.setHorizontalHeaderLabels(headers)
        
        # 设置表格列宽自动调整
        header = self.ui.table.horizontalHeader()
        for i in range(len(headers)):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
            
    def refresh_table(self):
        """刷新表格数据"""
        self.ui.table.setRowCount(len(self.students))
        for row, student in enumerate(self.students):
            for col, value in enumerate(student):
                item = QTableWidgetItem(value)
                self.ui.table.setItem(row, col, item)
                
    def add_student(self):
        """添加学生"""
        dialog = StudentDialog(self)
        if dialog.exec_():
            student_data = dialog.get_student_data()
            # 检查学号是否已存在
            if any(s[0] == student_data[0] for s in self.students):
                QMessageBox.warning(self, "错误", "学号已存在！")
                return
            self.students.append(student_data)
            self.refresh_table()
            
    def edit_student(self):
        """编辑学生"""
        current_row = self.ui.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "警告", "请先选择一个学生！")
            return
            
        dialog = StudentDialog(self, self.students[current_row])
        if dialog.exec_():
            student_data = dialog.get_student_data()
            # 检查学号是否与其他学生重复
            if student_data[0] != self.students[current_row][0] and \
               any(s[0] == student_data[0] for s in self.students):
                QMessageBox.warning(self, "错误", "学号已存在！")
                return
            self.students[current_row] = student_data
            self.refresh_table()
            
    def delete_student(self):
        """删除学生"""
        current_row = self.ui.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "警告", "请先选择一个学生！")
            return
            
        reply = QMessageBox.question(self, "确认", "确定要删除这个学生吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.students.pop(current_row)
            self.refresh_table()
            
    def search_student(self):
        """搜索学生"""
        keyword = self.ui.search_input.text().strip()
        if not keyword:
            self.refresh_table()
            return
            
        # 在所有字段中搜索
        filtered_students = []
        for student in self.students:
            if any(keyword.lower() in str(field).lower() for field in student):
                filtered_students.append(student)
                
        self.ui.table.setRowCount(len(filtered_students))
        for row, student in enumerate(filtered_students):
            for col, value in enumerate(student):
                item = QTableWidgetItem(value)
                self.ui.table.setItem(row, col, item) 