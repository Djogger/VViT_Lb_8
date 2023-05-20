import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget,
                             QAbstractScrollArea, QVBoxLayout,
                             QHBoxLayout, QTableWidget,
                             QGroupBox, QTableWidgetItem,
                             QPushButton, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Информационная Таблица МТУСИ")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()


    def _connect_to_db(self):
        self.conn = psycopg2.connect(
            database='Raspisanie_VViT',
            user='postgres',
            password='Dan12345',
            host='localhost',
            port='5432'
        )

        self.cursor = self.conn.cursor()


    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Расписание")

        self._create_shedule_tab_week()

###                                                     ###
        self.shedule_tab2 = QWidget()
        self.tabs.addTab(self.shedule_tab2, "Предметы")

        self._create_lessons_tab()
###                                                     ###

        self.shedule_tab3 = QWidget()
        self.tabs.addTab(self.shedule_tab3, "Преподаватели")

        self._create_teacher_tab()


    def _create_teacher_tab(self):
        self.name_box = QGroupBox("Сенсеи")

        self.qvbox = QVBoxLayout()
        self.qhbox = QHBoxLayout()
        self.qhbox1 = QHBoxLayout()

        self.qvbox.addLayout(self.qhbox)
        self.qvbox.addLayout(self.qhbox1)

        self.qhbox.addWidget(self.name_box)

        self.shedule_tab3.setLayout(self.qvbox)

        self._create_that_tab()


    def _create_that_tab(self):
        self.teacher_tab = QTableWidget()
        self.teacher_tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_tab.setColumnCount(4)
        self.teacher_tab.setHorizontalHeaderLabels(["Фамилия И.О.","Предмет", "", ""])

        self.qvbox1 = QVBoxLayout()
        self.qvbox1.addWidget(self.teacher_tab)
        self.name_box.setLayout(self.qvbox1)

        self._update_teacher_tab()


    def _update_teacher_tab(self):
        self.cursor.execute("select * from teacher;")
        records = list(self.cursor.fetchall())

        button = QPushButton("Обновить")
        self.qhbox1.addWidget(button)

        self.teacher_tab.setRowCount(len(records) + 1)

        a = len(records)

        for i, records in enumerate(records):

            self.teacher_tab.setItem(i, 0, QTableWidgetItem(str(records[1])))
            self.teacher_tab.setItem(i, 1, QTableWidgetItem(str(records[2])))

            changeButton = QPushButton("Изменить")
            changeButton1 = QPushButton("Изменить")
            changeButton2 = QPushButton("Изменить")
            changeButton3 = QPushButton("Изменить")
            changeButton4 = QPushButton("Изменить")
            changeButton5 = QPushButton("Изменить")
            changeButton6 = QPushButton("Изменить")

            deleteButton = QPushButton("Удалить")
            deleteButton1 = QPushButton("Удалить")
            deleteButton2 = QPushButton("Удалить")
            deleteButton3 = QPushButton("Удалить")
            deleteButton4 = QPushButton("Удалить")
            deleteButton5 = QPushButton("Удалить")
            deleteButton6 = QPushButton("Удалить")

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.teacher_tab.setCellWidget(0, 2, changeButton)
            self.teacher_tab.setCellWidget(1, 2, changeButton1)
            self.teacher_tab.setCellWidget(2, 2, changeButton2)
            self.teacher_tab.setCellWidget(3, 2, changeButton3)
            self.teacher_tab.setCellWidget(4, 2, changeButton4)
            self.teacher_tab.setCellWidget(5, 2, changeButton5)
            self.teacher_tab.setCellWidget(6, 2, changeButton6)

            self.teacher_tab.setCellWidget(0, 3, deleteButton)
            self.teacher_tab.setCellWidget(1, 3, deleteButton1)
            self.teacher_tab.setCellWidget(2, 3, deleteButton2)
            self.teacher_tab.setCellWidget(3, 3, deleteButton3)
            self.teacher_tab.setCellWidget(4, 3, deleteButton4)
            self.teacher_tab.setCellWidget(5, 3, deleteButton5)
            self.teacher_tab.setCellWidget(6, 3, deleteButton6)

            self.teacher_tab.setItem(a, 0, QTableWidgetItem(""))
            self.teacher_tab.setItem(a, 1, QTableWidgetItem(""))
            self.teacher_tab.setCellWidget(a, 2, NoneButton)
            self.teacher_tab.setCellWidget(a, 3, addButton)

            changeButton.clicked.connect(lambda num: self._change_item_from_teachertable(num=1))
            changeButton1.clicked.connect(lambda num: self._change_item_from_teachertable(num=2))
            changeButton2.clicked.connect(lambda num: self._change_item_from_teachertable(num=3))
            changeButton3.clicked.connect(lambda num: self._change_item_from_teachertable(num=4))
            changeButton4.clicked.connect(lambda num: self._change_item_from_teachertable(num=5))
            changeButton5.clicked.connect(lambda num: self._change_item_from_teachertable(num=6))
            deleteButton6.clicked.connect(lambda num: self._change_item_from_teachertable(num=7))

            deleteButton.clicked.connect(lambda num: self._delete_item_from_teachertable(num=0))
            deleteButton1.clicked.connect(lambda num: self._delete_item_from_teachertable(num=1))
            deleteButton2.clicked.connect(lambda num: self._delete_item_from_teachertable(num=2))
            deleteButton3.clicked.connect(lambda num: self._delete_item_from_teachertable(num=3))
            deleteButton4.clicked.connect(lambda num: self._delete_item_from_teachertable(num=4))
            deleteButton5.clicked.connect(lambda num: self._delete_item_from_teachertable(num=5))
            deleteButton6.clicked.connect(lambda num: self._delete_item_from_teachertable(num=6))

            addButton.clicked.connect(lambda: self._add_item_to_teachertable())

        if len(records) == 0:

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.teacher_tab.setItem(0, 0, QTableWidgetItem(""))
            self.teacher_tab.setItem(0, 1, QTableWidgetItem(""))
            self.teacher_tab.setCellWidget(0, 2, NoneButton)
            self.teacher_tab.setCellWidget(0, 3, addButton)

            addButton.clicked.connect(lambda: self._add_item_to_teachertable())

        self.teacher_tab.resizeRowsToContents()


    def _add_item_to_teachertable(self):

        self.cursor.execute("select * from teacher;")
        records = list(self.cursor.fetchall())

        a = len(records)

        row = list()

        row.append(self.teacher_tab.item(a, 0).text())
        row.append(self.teacher_tab.item(a, 1).text())

        if a >= 7:
            QMessageBox.about(self, "Error!", "Лимит на добавление информации в таблицу.")
        else:
            if row[0] == "" or row[1] == "":
                QMessageBox.about(self, "Error!", "Добавьте значения во все колонки.")
            else:
                self.cursor.execute(
                    "insert into teacher(full_name, subject) values ('" + row[0] + "', '" + row[1] + "');")
                self.conn.commit()

                QMessageBox.about(self, "Действие", "Добавлена строка.")

                self._update_teacher_tab()


    def _change_item_from_teachertable(self, num):

        row = list()

        row.append(self.teacher_tab.item(num - 1, 0).text())
        row.append(self.teacher_tab.item(num - 1, 1).text())

        rowi = list()

        for i in range(self.teacher_tab.rowCount()):
            rowi.append(self.teacher_tab.item(i, 0).text())
            rowi.append(self.teacher_tab.item(i, 1).text())
        #############################################################################################################
        self.cursor.execute("select * from teacher where id_t = '" + str(num) + "';")
        record = list(self.cursor.fetchall())

        if str(row[0]) == str(record[0][1]) and str(row[1]) == str(record[0][2]):
            QMessageBox.about(self, "Error!", "Измените запись.")
        else:
            if self.teacher_tab.rowCount() == 8:
                self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "'), ('" + str(rowi[6]) +"', '" + str(rowi[7]) + "'), ('" + str(rowi[8]) +"', '" + str(rowi[9]) + "'), ('" + str(rowi[10]) +"', '" + str(rowi[11]) + "'), ('" + str(rowi[12]) +"', '" + str(rowi[13]) + "');")
            if self.teacher_tab.rowCount() == 7:
                self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "'), ('" + str(rowi[6]) +"', '" + str(rowi[7]) + "'), ('" + str(rowi[8]) +"', '" + str(rowi[9]) + "'), ('" + str(rowi[10]) +"', '" + str(rowi[11]) + "');")
            if self.teacher_tab.rowCount() == 6:
                self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "'), ('" + str(rowi[6]) +"', '" + str(rowi[7]) + "'), ('" + str(rowi[8]) +"', '" + str(rowi[9]) + "');")
            if self.teacher_tab.rowCount() == 5:
                self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "'), ('" + str(rowi[6]) +"', '" + str(rowi[7]) + "');")
            if self.teacher_tab.rowCount() == 4:
                self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "');")
            if self.teacher_tab.rowCount() == 3:
                self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "');")
            if self.teacher_tab.rowCount() == 2:
                self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "');")

            QMessageBox.about(self, "Действие", "Запись изменена.")

            self.conn.commit()

            self._update_teacher_tab()


    def _delete_item_from_teachertable(self, num):
        row = list()

        row.append(self.teacher_tab.item(num, 0).text())
        row.append(self.teacher_tab.item(num, 1).text())

        rowi = list()

        for i in range(self.teacher_tab.rowCount()):
            rowi.append(self.teacher_tab.item(i, 0).text())
            rowi.append(self.teacher_tab.item(i, 1).text())

        self.cursor.execute("delete from teacher where subject = '" + str(row[1]) + "';")
        self.conn.commit()

        rowi.remove(str(row[0]))
        rowi.remove(str(row[1]))

        if self.teacher_tab.rowCount() == 8:
            self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "'), ('" + str(rowi[6]) +"', '" + str(rowi[7]) + "'), ('" + str(rowi[8]) +"', '" + str(rowi[9]) + "'), ('" + str(rowi[10]) +"', '" + str(rowi[11]) + "');")
        if self.teacher_tab.rowCount() == 7:
            self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "'), ('" + str(rowi[6]) +"', '" + str(rowi[7]) + "'), ('" + str(rowi[8]) +"', '" + str(rowi[9]) + "');")
        if self.teacher_tab.rowCount() == 6:
            self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "'), ('" + str(rowi[6]) +"', '" + str(rowi[7]) + "');")
        if self.teacher_tab.rowCount() == 5:
            self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "'), ('" + str(rowi[4]) +"', '" + str(rowi[5]) + "');")
        if self.teacher_tab.rowCount() == 4:
            self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "'), ('" + str(rowi[2]) +"', '" + str(rowi[3]) + "');")
        if self.teacher_tab.rowCount() == 3:
            self.cursor.execute("drop table if exists teacher cascade; create table teacher(id_t integer generated always as identity, full_name varchar(55), subject varchar(90)); insert into teacher(full_name, subject) values ('" + str(rowi[0]) + "', '" + str(rowi[1]) + "');")

        self.conn.commit()

        self._update_teacher_tab()


    def _create_lessons_tab(self):
        self.name_box = QGroupBox("Дисциплины")

        self.qvbox = QVBoxLayout()
        self.qhbox = QHBoxLayout()
        self.qhbox1 = QHBoxLayout()

        self.qhbox.addWidget(self.name_box)

        self.qvbox.addLayout(self.qhbox)
        self.qvbox.addLayout(self.qhbox1)

        self.button = QPushButton("Обновить")
        self.qhbox1.addWidget(self.button)

        self.shedule_tab2.setLayout(self.qvbox)

        self._create_tab()


    def _create_tab(self):
        self.lesson_tab = QTableWidget()
        self.lesson_tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.lesson_tab.setColumnCount(3)
        self.lesson_tab.setHorizontalHeaderLabels(["Предметы", "", ""])

        self._update_lesson_tab()

        self.box_qvbox = QVBoxLayout()
        self.box_qvbox.addWidget(self.lesson_tab)
        self.name_box.setLayout(self.box_qvbox)


    def _update_lesson_tab(self):
        self.cursor.execute("select * from subject;")
        records = list(self.cursor.fetchall())

        self.lesson_tab.setRowCount(len(records) + 1)

        a = len(records)

        for i, records in enumerate(records):

            changeButton = QPushButton("Изменить")
            changeButton1 = QPushButton("Изменить")
            changeButton2 = QPushButton("Изменить")
            changeButton3 = QPushButton("Изменить")
            changeButton4 = QPushButton("Изменить")
            changeButton5 = QPushButton("Изменить")
            changeButton6 = QPushButton("Изменить")
            changeButton7 = QPushButton("Изменить")
            changeButton8 = QPushButton("Изменить")
            changeButton9 = QPushButton("Изменить")

            deleteButton = QPushButton("Удалить")
            deleteButton1 = QPushButton("Удалить")
            deleteButton2 = QPushButton("Удалить")
            deleteButton3 = QPushButton("Удалить")
            deleteButton4 = QPushButton("Удалить")
            deleteButton5 = QPushButton("Удалить")
            deleteButton6 = QPushButton("Удалить")
            deleteButton7 = QPushButton("Удалить")
            deleteButton8 = QPushButton("Удалить")
            deleteButton9 = QPushButton("Удалить")

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")


            self.lesson_tab.setItem(i, 0, QTableWidgetItem(str(records[1])))

            self.lesson_tab.setCellWidget(0, 1, changeButton)
            self.lesson_tab.setCellWidget(1, 1, changeButton1)
            self.lesson_tab.setCellWidget(2, 1, changeButton2)
            self.lesson_tab.setCellWidget(3, 1, changeButton3)
            self.lesson_tab.setCellWidget(4, 1, changeButton4)
            self.lesson_tab.setCellWidget(5, 1, changeButton5)
            self.lesson_tab.setCellWidget(6, 1, changeButton6)
            self.lesson_tab.setCellWidget(7, 1, changeButton7)
            self.lesson_tab.setCellWidget(8, 1, changeButton8)
            self.lesson_tab.setCellWidget(9, 1, changeButton9)

            self.lesson_tab.setCellWidget(0, 2, deleteButton)
            self.lesson_tab.setCellWidget(1, 2, deleteButton1)
            self.lesson_tab.setCellWidget(2, 2, deleteButton2)
            self.lesson_tab.setCellWidget(3, 2, deleteButton3)
            self.lesson_tab.setCellWidget(4, 2, deleteButton4)
            self.lesson_tab.setCellWidget(5, 2, deleteButton5)
            self.lesson_tab.setCellWidget(6, 2, deleteButton6)
            self.lesson_tab.setCellWidget(7, 2, deleteButton7)
            self.lesson_tab.setCellWidget(8, 2, deleteButton8)
            self.lesson_tab.setCellWidget(9, 2, deleteButton9)

            self.lesson_tab.setItem(a, 0, QTableWidgetItem(""))
            self.lesson_tab.setCellWidget(a, 1, NoneButton)
            self.lesson_tab.setCellWidget(a, 2, addButton)

            changeButton.clicked.connect(lambda num: self._change_item_from_table(num = 1))
            changeButton1.clicked.connect(lambda num: self._change_item_from_table(num = 2))
            changeButton2.clicked.connect(lambda num: self._change_item_from_table(num = 3))
            changeButton3.clicked.connect(lambda num: self._change_item_from_table(num = 4))
            changeButton4.clicked.connect(lambda num: self._change_item_from_table(num = 5))
            changeButton5.clicked.connect(lambda num: self._change_item_from_table(num = 6))
            changeButton6.clicked.connect(lambda num: self._change_item_from_table(num = 7))
            changeButton7.clicked.connect(lambda num: self._change_item_from_table(num = 8))
            changeButton8.clicked.connect(lambda num: self._change_item_from_table(num = 9))
            changeButton9.clicked.connect(lambda num: self._change_item_from_table(num = 10))

            deleteButton.clicked.connect(lambda num: self._delete_item_from_table(num = 0))
            deleteButton1.clicked.connect(lambda num: self._delete_item_from_table(num = 1))
            deleteButton2.clicked.connect(lambda num: self._delete_item_from_table(num = 2))
            deleteButton3.clicked.connect(lambda num: self._delete_item_from_table(num = 3))
            deleteButton4.clicked.connect(lambda num: self._delete_item_from_table(num = 4))
            deleteButton5.clicked.connect(lambda num: self._delete_item_from_table(num = 5))
            deleteButton6.clicked.connect(lambda num: self._delete_item_from_table(num = 6))
            deleteButton7.clicked.connect(lambda num: self._delete_item_from_table(num = 7))
            deleteButton8.clicked.connect(lambda num: self._delete_item_from_table(num = 8))
            deleteButton9.clicked.connect(lambda num: self._delete_item_from_table(num = 9))

            addButton.clicked.connect(lambda: self._add_item_to_lessontable())

        if len(records) == 0:

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.lesson_tab.setItem(0, 0, QTableWidgetItem(""))
            self.lesson_tab.setCellWidget(0, 1, NoneButton)
            self.lesson_tab.setCellWidget(0, 2, addButton)

            addButton.clicked.connect(lambda: self._add_item_to_lessontable())

        self.lesson_tab.resizeRowsToContents()


    def _add_item_to_lessontable(self):

        self.cursor.execute("select * from subject;")
        records = list(self.cursor.fetchall())

        a = len(records)

        row = list()

        row.append(self.lesson_tab.item(a, 0).text())

        if a >= 10:
            QMessageBox.about(self, "Error!", "Лимит на добавление информации в таблицу.")
        else:
            if row[0] == "":
                QMessageBox.about(self, "Error!", "Добавьте значение в колонку.")
            else:
                self.cursor.execute("insert into subject(namee) values ('" + row[0] + "');")
                self.conn.commit()

                QMessageBox.about(self, "Действие", "Добавлена строка.")

                self._update_lesson_tab()


    def _change_item_from_table(self, num):

        row = list()

        row.append(self.lesson_tab.item(num - 1, 0).text())

        rowi = list()

        for i in range(self.lesson_tab.rowCount()):
            rowi.append(self.lesson_tab.item(i, 0).text())
#############################################################################################################
        self.cursor.execute("select * from subject where id_ = '" + str(num) + "';")
        record = list(self.cursor.fetchall())

        if str(row[0]) == str(record[0][1]):
            QMessageBox.about(self, "Error!", "Измените запись.")
        else:
            if self.lesson_tab.rowCount() == 11:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "'), ('" + str(rowi[6]) + "'), ('" + str(rowi[7]) + "'), ('" + str(rowi[8]) + "'), ('" + str(rowi[9]) + "');")
            if self.lesson_tab.rowCount() == 10:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "'), ('" + str(rowi[6]) + "'), ('" + str(rowi[7]) + "'), ('" + str(rowi[8]) + "');")
            if self.lesson_tab.rowCount() == 9:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "'), ('" + str(rowi[6]) + "'), ('" + str(rowi[7]) + "');")
            if self.lesson_tab.rowCount() == 8:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "'), ('" + str(rowi[6]) + "');")
            if self.lesson_tab.rowCount() == 7:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "');")
            if self.lesson_tab.rowCount() == 6:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "');")
            if self.lesson_tab.rowCount() == 5:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "');")
            if self.lesson_tab.rowCount() == 4:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "');")
            if self.lesson_tab.rowCount() == 3:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "');")
            if self.lesson_tab.rowCount() == 2:
                self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "');")

            QMessageBox.about(self, "Действие", "Запись изменена.")

            self.conn.commit()

            self._update_lesson_tab()



    def _delete_item_from_table(self, num):
        row = list()

        row.append(self.lesson_tab.item(num, 0).text())

        rowi = list()

        for i in range(self.lesson_tab.rowCount()):
            rowi.append(self.lesson_tab.item(i, 0).text())

        self.cursor.execute("delete from subject where namee = '" + str(row[0]) + "';")
        self.conn.commit()

        rowi.remove(str(row[0]))

        if self.lesson_tab.rowCount() == 11:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "'), ('" + str(rowi[6]) + "'), ('" + str(rowi[7]) + "'), ('" + str(rowi[8]) + "');")
        if self.lesson_tab.rowCount() == 10:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "'), ('" + str(rowi[6]) + "'), ('" + str(rowi[7]) + "');")
        if self.lesson_tab.rowCount() == 9:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "'), ('" + str(rowi[6]) + "');")
        if self.lesson_tab.rowCount() == 8:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "'), ('" + str(rowi[5]) + "');")
        if self.lesson_tab.rowCount() == 7:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "'), ('" + str(rowi[4]) + "');")
        if self.lesson_tab.rowCount() == 6:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "'), ('" + str(rowi[3]) + "');")
        if self.lesson_tab.rowCount() == 5:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "'), ('" + str(rowi[2]) + "');")
        if self.lesson_tab.rowCount() == 4:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "'), ('" + str(rowi[1]) + "');")
        if self.lesson_tab.rowCount() == 3:
            self.cursor.execute("drop table if exists subject cascade; create table subject(id_ integer generated always as identity,namee varchar(90)); insert into subject(namee) values ('" + str(rowi[0]) + "');")

        self.conn.commit()

        self._update_lesson_tab()


####################################################################################################################
    def _create_shedule_tab_week(self):

        self.monday_gbox = QGroupBox("Понедельник")
        self.tuesday_gbox = QGroupBox("Вторник")
        self.wednesday_gbox = QGroupBox("Среда")
        self.thursday_gbox = QGroupBox("Четверг")
        self.friday_gbox = QGroupBox("Пятница")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()
        self.shbox6 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)
        self.svbox.addLayout(self.shbox5)
        self.svbox.addLayout(self.shbox6)

        self.shbox1.addWidget(self.monday_gbox)
        self.shbox2.addWidget(self.tuesday_gbox)
        self.shbox3.addWidget(self.wednesday_gbox)
        self.shbox4.addWidget(self.thursday_gbox)
        self.shbox5.addWidget(self.friday_gbox)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()
        self._create_thursday_table()
        self._create_friday_table()

        self.update_shedule_button = QPushButton("Обновить")
        self.shbox6.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)


    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(8)
        self.monday_table.setHorizontalHeaderLabels(["id-Недели", "Предмет", "Время", "Кабинет", "Лектор", "", "", "Идентификатор"])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)


    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM raspisanie_week WHERE dayl='Понедельник'")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        a = len(records)

        for i, records in enumerate(records):
            changeButton = QPushButton("Изменить")
            changeButton1 = QPushButton("Изменить")
            changeButton2 = QPushButton("Изменить")
            changeButton3 = QPushButton("Изменить")
            changeButton4 = QPushButton("Изменить")
            changeButton5 = QPushButton("Изменить")
            changeButton6 = QPushButton("Изменить")
            changeButton7 = QPushButton("Изменить")
            changeButton8 = QPushButton("Изменить")
            changeButton9 = QPushButton("Изменить")

            deleteButton = QPushButton("Удалить")
            deleteButton1 = QPushButton("Удалить")
            deleteButton2 = QPushButton("Удалить")
            deleteButton3 = QPushButton("Удалить")
            deleteButton4 = QPushButton("Удалить")
            deleteButton5 = QPushButton("Удалить")
            deleteButton6 = QPushButton("Удалить")
            deleteButton7 = QPushButton("Удалить")
            deleteButton8 = QPushButton("Удалить")
            deleteButton9 = QPushButton("Удалить")

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.monday_table.setItem(i, 0, QTableWidgetItem(str(records[0])))
            self.monday_table.setItem(i, 1, QTableWidgetItem(str(records[3])))
            self.monday_table.setItem(i, 2, QTableWidgetItem(str(records[5])))
            self.monday_table.setItem(i, 3, QTableWidgetItem(str(records[4])))
            self.monday_table.setItem(i, 4, QTableWidgetItem(str(records[6])))
            self.monday_table.setItem(i, 7, QTableWidgetItem(str(records[1])))

            self.monday_table.setCellWidget(0, 5, changeButton)
            self.monday_table.setCellWidget(1, 5, changeButton1)
            self.monday_table.setCellWidget(2, 5, changeButton2)
            self.monday_table.setCellWidget(3, 5, changeButton3)
            self.monday_table.setCellWidget(4, 5, changeButton4)
            self.monday_table.setCellWidget(5, 5, changeButton5)
            self.monday_table.setCellWidget(6, 5, changeButton6)
            self.monday_table.setCellWidget(7, 5, changeButton7)
            self.monday_table.setCellWidget(8, 5, changeButton8)
            self.monday_table.setCellWidget(9, 5, changeButton9)

            self.monday_table.setCellWidget(0, 6, deleteButton)
            self.monday_table.setCellWidget(1, 6, deleteButton1)
            self.monday_table.setCellWidget(2, 6, deleteButton2)
            self.monday_table.setCellWidget(3, 6, deleteButton3)
            self.monday_table.setCellWidget(4, 6, deleteButton4)
            self.monday_table.setCellWidget(5, 6, deleteButton5)
            self.monday_table.setCellWidget(6, 6, deleteButton6)
            self.monday_table.setCellWidget(7, 6, deleteButton7)
            self.monday_table.setCellWidget(8, 6, deleteButton8)
            self.monday_table.setCellWidget(9, 6, deleteButton9)

            self.monday_table.setItem(a, 0, QTableWidgetItem(""))
            self.monday_table.setItem(a, 1, QTableWidgetItem(""))
            self.monday_table.setItem(a, 2, QTableWidgetItem(""))
            self.monday_table.setItem(a, 3, QTableWidgetItem(""))
            self.monday_table.setItem(a, 4, QTableWidgetItem(""))
            self.monday_table.setCellWidget(a, 5, NoneButton)
            self.monday_table.setCellWidget(a, 6, addButton)

            changeButton.clicked.connect(lambda num: self._change_item_from_mond(num=1))
            changeButton1.clicked.connect(lambda num: self._change_item_from_mond(num=2))
            changeButton2.clicked.connect(lambda num: self._change_item_from_mond(num=3))
            changeButton3.clicked.connect(lambda num: self._change_item_from_mond(num=4))
            changeButton4.clicked.connect(lambda num: self._change_item_from_mond(num=5))
            changeButton5.clicked.connect(lambda num: self._change_item_from_mond(num=6))
            changeButton6.clicked.connect(lambda num: self._change_item_from_mond(num=7))
            changeButton7.clicked.connect(lambda num: self._change_item_from_mond(num=8))
            changeButton8.clicked.connect(lambda num: self._change_item_from_mond(num=9))
            changeButton9.clicked.connect(lambda num: self._change_item_from_mond(num=10))

            deleteButton.clicked.connect(lambda num: self._delete_item_from_mond(num=0))
            deleteButton1.clicked.connect(lambda num: self._delete_item_from_mond(num=1))
            deleteButton2.clicked.connect(lambda num: self._delete_item_from_mond(num=2))
            deleteButton3.clicked.connect(lambda num: self._delete_item_from_mond(num=3))
            deleteButton4.clicked.connect(lambda num: self._delete_item_from_mond(num=4))
            deleteButton5.clicked.connect(lambda num: self._delete_item_from_mond(num=5))
            deleteButton6.clicked.connect(lambda num: self._delete_item_from_mond(num=6))
            deleteButton7.clicked.connect(lambda num: self._delete_item_from_mond(num=7))
            deleteButton8.clicked.connect(lambda num: self._delete_item_from_mond(num=8))
            deleteButton9.clicked.connect(lambda num: self._delete_item_from_mond(num=9))

            addButton.clicked.connect(lambda: self._add_item_to_mondaytable())

        self.monday_table.resizeRowsToContents()


    def _change_item_from_mond(self, num):

        row = list()

        row.append(self.monday_table.item(num - 1, 0).text())
        row.append(self.monday_table.item(num - 1, 1).text())
        row.append(self.monday_table.item(num - 1, 2).text())
        row.append(self.monday_table.item(num - 1, 3).text())
        row.append(self.monday_table.item(num - 1, 4).text())
        row.append(self.monday_table.item(num - 1, 6))

        #for i in range(self.monday_table.rowCount()):
        #    rowi.append(self.monday_table.item(i, 0).text())
        #    rowi.append(self.monday_table.item(i, 1).text())
        #############################################################################################################
        self.cursor.execute("select * from raspisanie_week where id_ = '" + str(row[5]) + "';")
        record = list(self.cursor.fetchall())

        if str(row[1]) == str(record[0][3]) and str(row[2]) == str(record[0][5]):
            QMessageBox.about(self, "Error!", "Измените запись.")
        else:
            if str(row[1]) != str(record[0][3]):
                self.cursor.execute("update raspisanie_week set subject = '" + str(row[1]) + "' where subject = '" + str(record[0][3]) + "' and id_week = " + str(row[0]) + ";")

            QMessageBox.about(self, "Действие", "Запись изменена.")

            self.conn.commit()

            self._update_teacher_tab()


    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(8)
        self.tuesday_table.setHorizontalHeaderLabels(["id-Недели", "Предмет", "Время", "Кабинет", "Лектор", "", "", "Идентификатор"])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)


    def _update_tuesday_table(self):
        self.cursor.execute("select * from raspisanie_week where dayl = 'Вторник'")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)

        a = len(records)

        for i, records in enumerate(records):
            changeButton = QPushButton("Изменить")
            changeButton1 = QPushButton("Изменить")
            changeButton2 = QPushButton("Изменить")
            changeButton3 = QPushButton("Изменить")
            changeButton4 = QPushButton("Изменить")
            changeButton5 = QPushButton("Изменить")
            changeButton6 = QPushButton("Изменить")
            changeButton7 = QPushButton("Изменить")
            changeButton8 = QPushButton("Изменить")
            changeButton9 = QPushButton("Изменить")

            deleteButton = QPushButton("Удалить")
            deleteButton1 = QPushButton("Удалить")
            deleteButton2 = QPushButton("Удалить")
            deleteButton3 = QPushButton("Удалить")
            deleteButton4 = QPushButton("Удалить")
            deleteButton5 = QPushButton("Удалить")
            deleteButton6 = QPushButton("Удалить")
            deleteButton7 = QPushButton("Удалить")
            deleteButton8 = QPushButton("Удалить")
            deleteButton9 = QPushButton("Удалить")

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.tuesday_table.setItem(i, 0, QTableWidgetItem(str(records[0])))
            self.tuesday_table.setItem(i, 1, QTableWidgetItem(str(records[3])))
            self.tuesday_table.setItem(i, 2, QTableWidgetItem(str(records[5])))
            self.tuesday_table.setItem(i, 3, QTableWidgetItem(str(records[4])))
            self.tuesday_table.setItem(i, 4, QTableWidgetItem(str(records[6])))
            self.tuesday_table.setItem(i, 7, QTableWidgetItem(str(records[1])))

            self.tuesday_table.setCellWidget(0, 5, changeButton)
            self.tuesday_table.setCellWidget(1, 5, changeButton1)
            self.tuesday_table.setCellWidget(2, 5, changeButton2)
            self.tuesday_table.setCellWidget(3, 5, changeButton3)
            self.tuesday_table.setCellWidget(4, 5, changeButton4)
            self.tuesday_table.setCellWidget(5, 5, changeButton5)
            self.tuesday_table.setCellWidget(6, 5, changeButton6)
            self.tuesday_table.setCellWidget(7, 5, changeButton7)
            self.tuesday_table.setCellWidget(8, 5, changeButton8)
            self.tuesday_table.setCellWidget(9, 5, changeButton9)

            self.tuesday_table.setCellWidget(0, 6, deleteButton)
            self.tuesday_table.setCellWidget(1, 6, deleteButton1)
            self.tuesday_table.setCellWidget(2, 6, deleteButton2)
            self.tuesday_table.setCellWidget(3, 6, deleteButton3)
            self.tuesday_table.setCellWidget(4, 6, deleteButton4)
            self.tuesday_table.setCellWidget(5, 6, deleteButton5)
            self.tuesday_table.setCellWidget(6, 6, deleteButton6)
            self.tuesday_table.setCellWidget(7, 6, deleteButton7)
            self.tuesday_table.setCellWidget(8, 6, deleteButton8)
            self.tuesday_table.setCellWidget(9, 6, deleteButton9)

            self.tuesday_table.setItem(a, 0, QTableWidgetItem(""))
            self.tuesday_table.setItem(a, 1, QTableWidgetItem(""))
            self.tuesday_table.setItem(a, 2, QTableWidgetItem(""))
            self.tuesday_table.setItem(a, 3, QTableWidgetItem(""))
            self.tuesday_table.setItem(a, 4, QTableWidgetItem(""))
            self.tuesday_table.setCellWidget(a, 5, NoneButton)
            self.tuesday_table.setCellWidget(a, 6, addButton)

            changeButton.clicked.connect(lambda num: self._change_item_from_mond(num=1))
            changeButton1.clicked.connect(lambda num: self._change_item_from_mond(num=2))
            changeButton2.clicked.connect(lambda num: self._change_item_from_mond(num=3))
            changeButton3.clicked.connect(lambda num: self._change_item_from_mond(num=4))
            changeButton4.clicked.connect(lambda num: self._change_item_from_mond(num=5))
            changeButton5.clicked.connect(lambda num: self._change_item_from_mond(num=6))
            changeButton6.clicked.connect(lambda num: self._change_item_from_mond(num=7))
            changeButton7.clicked.connect(lambda num: self._change_item_from_mond(num=8))
            changeButton8.clicked.connect(lambda num: self._change_item_from_mond(num=9))
            changeButton9.clicked.connect(lambda num: self._change_item_from_mond(num=10))

            deleteButton.clicked.connect(lambda num: self._delete_item_from_mond(num=0))
            deleteButton1.clicked.connect(lambda num: self._delete_item_from_mond(num=1))
            deleteButton2.clicked.connect(lambda num: self._delete_item_from_mond(num=2))
            deleteButton3.clicked.connect(lambda num: self._delete_item_from_mond(num=3))
            deleteButton4.clicked.connect(lambda num: self._delete_item_from_mond(num=4))
            deleteButton5.clicked.connect(lambda num: self._delete_item_from_mond(num=5))
            deleteButton6.clicked.connect(lambda num: self._delete_item_from_mond(num=6))
            deleteButton7.clicked.connect(lambda num: self._delete_item_from_mond(num=7))
            deleteButton8.clicked.connect(lambda num: self._delete_item_from_mond(num=8))
            deleteButton9.clicked.connect(lambda num: self._delete_item_from_mond(num=9))

            addButton.clicked.connect(lambda: self._add_item_to_mondaytable())

        self.tuesday_table.resizeRowsToContents()

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(8)
        self.wednesday_table.setHorizontalHeaderLabels(["id-Недели", "Предмет", "Время", "Кабинет", "Лектор", "", "", "Идентификатор"])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.mvbox)


    def _update_wednesday_table(self):
        self.cursor.execute("select * from raspisanie_week where dayl = 'Среда'")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)

        a = len(records)

        for i, records in enumerate(records):
            changeButton = QPushButton("Изменить")
            changeButton1 = QPushButton("Изменить")
            changeButton2 = QPushButton("Изменить")
            changeButton3 = QPushButton("Изменить")
            changeButton4 = QPushButton("Изменить")
            changeButton5 = QPushButton("Изменить")
            changeButton6 = QPushButton("Изменить")
            changeButton7 = QPushButton("Изменить")
            changeButton8 = QPushButton("Изменить")
            changeButton9 = QPushButton("Изменить")

            deleteButton = QPushButton("Удалить")
            deleteButton1 = QPushButton("Удалить")
            deleteButton2 = QPushButton("Удалить")
            deleteButton3 = QPushButton("Удалить")
            deleteButton4 = QPushButton("Удалить")
            deleteButton5 = QPushButton("Удалить")
            deleteButton6 = QPushButton("Удалить")
            deleteButton7 = QPushButton("Удалить")
            deleteButton8 = QPushButton("Удалить")
            deleteButton9 = QPushButton("Удалить")

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.wednesday_table.setItem(i, 0, QTableWidgetItem(str(records[0])))
            self.wednesday_table.setItem(i, 1, QTableWidgetItem(str(records[3])))
            self.wednesday_table.setItem(i, 2, QTableWidgetItem(str(records[5])))
            self.wednesday_table.setItem(i, 3, QTableWidgetItem(str(records[4])))
            self.wednesday_table.setItem(i, 4, QTableWidgetItem(str(records[6])))
            self.wednesday_table.setItem(i, 7, QTableWidgetItem(str(records[1])))

            self.wednesday_table.setCellWidget(0, 5, changeButton)
            self.wednesday_table.setCellWidget(1, 5, changeButton1)
            self.wednesday_table.setCellWidget(2, 5, changeButton2)
            self.wednesday_table.setCellWidget(3, 5, changeButton3)
            self.wednesday_table.setCellWidget(4, 5, changeButton4)
            self.wednesday_table.setCellWidget(5, 5, changeButton5)
            self.wednesday_table.setCellWidget(6, 5, changeButton6)
            self.wednesday_table.setCellWidget(7, 5, changeButton7)
            self.wednesday_table.setCellWidget(8, 5, changeButton8)
            self.wednesday_table.setCellWidget(9, 5, changeButton9)

            self.wednesday_table.setCellWidget(0, 6, deleteButton)
            self.wednesday_table.setCellWidget(1, 6, deleteButton1)
            self.wednesday_table.setCellWidget(2, 6, deleteButton2)
            self.wednesday_table.setCellWidget(3, 6, deleteButton3)
            self.wednesday_table.setCellWidget(4, 6, deleteButton4)
            self.wednesday_table.setCellWidget(5, 6, deleteButton5)
            self.wednesday_table.setCellWidget(6, 6, deleteButton6)
            self.wednesday_table.setCellWidget(7, 6, deleteButton7)
            self.wednesday_table.setCellWidget(8, 6, deleteButton8)
            self.wednesday_table.setCellWidget(9, 6, deleteButton9)

            self.wednesday_table.setItem(a, 0, QTableWidgetItem(""))
            self.wednesday_table.setItem(a, 1, QTableWidgetItem(""))
            self.wednesday_table.setItem(a, 2, QTableWidgetItem(""))
            self.wednesday_table.setItem(a, 3, QTableWidgetItem(""))
            self.wednesday_table.setItem(a, 4, QTableWidgetItem(""))
            self.wednesday_table.setCellWidget(a, 5, NoneButton)
            self.wednesday_table.setCellWidget(a, 6, addButton)

            changeButton.clicked.connect(lambda num: self._change_item_from_mond(num=1))
            changeButton1.clicked.connect(lambda num: self._change_item_from_mond(num=2))
            changeButton2.clicked.connect(lambda num: self._change_item_from_mond(num=3))
            changeButton3.clicked.connect(lambda num: self._change_item_from_mond(num=4))
            changeButton4.clicked.connect(lambda num: self._change_item_from_mond(num=5))
            changeButton5.clicked.connect(lambda num: self._change_item_from_mond(num=6))
            changeButton6.clicked.connect(lambda num: self._change_item_from_mond(num=7))
            changeButton7.clicked.connect(lambda num: self._change_item_from_mond(num=8))
            changeButton8.clicked.connect(lambda num: self._change_item_from_mond(num=9))
            changeButton9.clicked.connect(lambda num: self._change_item_from_mond(num=10))

            deleteButton.clicked.connect(lambda num: self._delete_item_from_mond(num=0))
            deleteButton1.clicked.connect(lambda num: self._delete_item_from_mond(num=1))
            deleteButton2.clicked.connect(lambda num: self._delete_item_from_mond(num=2))
            deleteButton3.clicked.connect(lambda num: self._delete_item_from_mond(num=3))
            deleteButton4.clicked.connect(lambda num: self._delete_item_from_mond(num=4))
            deleteButton5.clicked.connect(lambda num: self._delete_item_from_mond(num=5))
            deleteButton6.clicked.connect(lambda num: self._delete_item_from_mond(num=6))
            deleteButton7.clicked.connect(lambda num: self._delete_item_from_mond(num=7))
            deleteButton8.clicked.connect(lambda num: self._delete_item_from_mond(num=8))
            deleteButton9.clicked.connect(lambda num: self._delete_item_from_mond(num=9))

            addButton.clicked.connect(lambda: self._add_item_to_mondaytable())

        self.wednesday_table.resizeRowsToContents()

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(8)
        self.thursday_table.setHorizontalHeaderLabels(["id-Недели", "Предмет", "Время", "Кабинет", "Лектор", "", "", "Идентификатор"])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)


    def _update_thursday_table(self):
        self.cursor.execute("select * from raspisanie_week where dayl = 'Четверг'")
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records) + 1)

        a = len(records)

        for i, records in enumerate(records):
            changeButton = QPushButton("Изменить")
            changeButton1 = QPushButton("Изменить")
            changeButton2 = QPushButton("Изменить")
            changeButton3 = QPushButton("Изменить")
            changeButton4 = QPushButton("Изменить")
            changeButton5 = QPushButton("Изменить")
            changeButton6 = QPushButton("Изменить")
            changeButton7 = QPushButton("Изменить")
            changeButton8 = QPushButton("Изменить")
            changeButton9 = QPushButton("Изменить")

            deleteButton = QPushButton("Удалить")
            deleteButton1 = QPushButton("Удалить")
            deleteButton2 = QPushButton("Удалить")
            deleteButton3 = QPushButton("Удалить")
            deleteButton4 = QPushButton("Удалить")
            deleteButton5 = QPushButton("Удалить")
            deleteButton6 = QPushButton("Удалить")
            deleteButton7 = QPushButton("Удалить")
            deleteButton8 = QPushButton("Удалить")
            deleteButton9 = QPushButton("Удалить")

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.thursday_table.setItem(i, 0, QTableWidgetItem(str(records[0])))
            self.thursday_table.setItem(i, 1, QTableWidgetItem(str(records[3])))
            self.thursday_table.setItem(i, 2, QTableWidgetItem(str(records[5])))
            self.thursday_table.setItem(i, 3, QTableWidgetItem(str(records[4])))
            self.thursday_table.setItem(i, 4, QTableWidgetItem(str(records[6])))
            self.thursday_table.setItem(i, 7, QTableWidgetItem(str(records[1])))

            self.thursday_table.setCellWidget(0, 5, changeButton)
            self.thursday_table.setCellWidget(1, 5, changeButton1)
            self.thursday_table.setCellWidget(2, 5, changeButton2)
            self.thursday_table.setCellWidget(3, 5, changeButton3)
            self.thursday_table.setCellWidget(4, 5, changeButton4)
            self.thursday_table.setCellWidget(5, 5, changeButton5)
            self.thursday_table.setCellWidget(6, 5, changeButton6)
            self.thursday_table.setCellWidget(7, 5, changeButton7)
            self.thursday_table.setCellWidget(8, 5, changeButton8)
            self.thursday_table.setCellWidget(9, 5, changeButton9)

            self.thursday_table.setCellWidget(0, 6, deleteButton)
            self.thursday_table.setCellWidget(1, 6, deleteButton1)
            self.thursday_table.setCellWidget(2, 6, deleteButton2)
            self.thursday_table.setCellWidget(3, 6, deleteButton3)
            self.thursday_table.setCellWidget(4, 6, deleteButton4)
            self.thursday_table.setCellWidget(5, 6, deleteButton5)
            self.thursday_table.setCellWidget(6, 6, deleteButton6)
            self.thursday_table.setCellWidget(7, 6, deleteButton7)
            self.thursday_table.setCellWidget(8, 6, deleteButton8)
            self.thursday_table.setCellWidget(9, 6, deleteButton9)

            self.thursday_table.setItem(a, 0, QTableWidgetItem(""))
            self.thursday_table.setItem(a, 1, QTableWidgetItem(""))
            self.thursday_table.setItem(a, 2, QTableWidgetItem(""))
            self.thursday_table.setItem(a, 3, QTableWidgetItem(""))
            self.thursday_table.setItem(a, 4, QTableWidgetItem(""))
            self.thursday_table.setCellWidget(a, 5, NoneButton)
            self.thursday_table.setCellWidget(a, 6, addButton)

            changeButton.clicked.connect(lambda num: self._change_item_from_mond(num=1))
            changeButton1.clicked.connect(lambda num: self._change_item_from_mond(num=2))
            changeButton2.clicked.connect(lambda num: self._change_item_from_mond(num=3))
            changeButton3.clicked.connect(lambda num: self._change_item_from_mond(num=4))
            changeButton4.clicked.connect(lambda num: self._change_item_from_mond(num=5))
            changeButton5.clicked.connect(lambda num: self._change_item_from_mond(num=6))
            changeButton6.clicked.connect(lambda num: self._change_item_from_mond(num=7))
            changeButton7.clicked.connect(lambda num: self._change_item_from_mond(num=8))
            changeButton8.clicked.connect(lambda num: self._change_item_from_mond(num=9))
            changeButton9.clicked.connect(lambda num: self._change_item_from_mond(num=10))

            deleteButton.clicked.connect(lambda num: self._delete_item_from_mond(num=0))
            deleteButton1.clicked.connect(lambda num: self._delete_item_from_mond(num=1))
            deleteButton2.clicked.connect(lambda num: self._delete_item_from_mond(num=2))
            deleteButton3.clicked.connect(lambda num: self._delete_item_from_mond(num=3))
            deleteButton4.clicked.connect(lambda num: self._delete_item_from_mond(num=4))
            deleteButton5.clicked.connect(lambda num: self._delete_item_from_mond(num=5))
            deleteButton6.clicked.connect(lambda num: self._delete_item_from_mond(num=6))
            deleteButton7.clicked.connect(lambda num: self._delete_item_from_mond(num=7))
            deleteButton8.clicked.connect(lambda num: self._delete_item_from_mond(num=8))
            deleteButton9.clicked.connect(lambda num: self._delete_item_from_mond(num=9))

            addButton.clicked.connect(lambda: self._add_item_to_mondaytable())

        self.thursday_table.resizeRowsToContents()

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(8)
        self.friday_table.setHorizontalHeaderLabels(["id-Недели", "Предмет", "Время", "Кабинет", "Лектор", "", "", "Идентификатор"])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)


    def _update_friday_table(self):
        self.cursor.execute("SELECT * FROM raspisanie_week WHERE dayl='Пятница'")
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records) + 1)

        a = len(records)

        for i, records in enumerate(records):
            changeButton = QPushButton("Изменить")
            changeButton1 = QPushButton("Изменить")
            changeButton2 = QPushButton("Изменить")
            changeButton3 = QPushButton("Изменить")
            changeButton4 = QPushButton("Изменить")
            changeButton5 = QPushButton("Изменить")
            changeButton6 = QPushButton("Изменить")
            changeButton7 = QPushButton("Изменить")
            changeButton8 = QPushButton("Изменить")
            changeButton9 = QPushButton("Изменить")

            deleteButton = QPushButton("Удалить")
            deleteButton1 = QPushButton("Удалить")
            deleteButton2 = QPushButton("Удалить")
            deleteButton3 = QPushButton("Удалить")
            deleteButton4 = QPushButton("Удалить")
            deleteButton5 = QPushButton("Удалить")
            deleteButton6 = QPushButton("Удалить")
            deleteButton7 = QPushButton("Удалить")
            deleteButton8 = QPushButton("Удалить")
            deleteButton9 = QPushButton("Удалить")

            addButton = QPushButton("Добавить")
            NoneButton = QPushButton("☭")

            self.friday_table.setItem(i, 0, QTableWidgetItem(str(records[0])))
            self.friday_table.setItem(i, 1, QTableWidgetItem(str(records[3])))
            self.friday_table.setItem(i, 2, QTableWidgetItem(str(records[5])))
            self.friday_table.setItem(i, 3, QTableWidgetItem(str(records[4])))
            self.friday_table.setItem(i, 4, QTableWidgetItem(str(records[6])))
            self.friday_table.setItem(i, 7, QTableWidgetItem(str(records[1])))

            self.friday_table.setCellWidget(0, 5, changeButton)
            self.friday_table.setCellWidget(1, 5, changeButton1)
            self.friday_table.setCellWidget(2, 5, changeButton2)
            self.friday_table.setCellWidget(3, 5, changeButton3)
            self.friday_table.setCellWidget(4, 5, changeButton4)
            self.friday_table.setCellWidget(5, 5, changeButton5)
            self.friday_table.setCellWidget(6, 5, changeButton6)
            self.friday_table.setCellWidget(7, 5, changeButton7)
            self.friday_table.setCellWidget(8, 5, changeButton8)
            self.friday_table.setCellWidget(9, 5, changeButton9)

            self.friday_table.setCellWidget(0, 6, deleteButton)
            self.friday_table.setCellWidget(1, 6, deleteButton1)
            self.friday_table.setCellWidget(2, 6, deleteButton2)
            self.friday_table.setCellWidget(3, 6, deleteButton3)
            self.friday_table.setCellWidget(4, 6, deleteButton4)
            self.friday_table.setCellWidget(5, 6, deleteButton5)
            self.friday_table.setCellWidget(6, 6, deleteButton6)
            self.friday_table.setCellWidget(7, 6, deleteButton7)
            self.friday_table.setCellWidget(8, 6, deleteButton8)
            self.friday_table.setCellWidget(9, 6, deleteButton9)

            self.friday_table.setItem(a, 0, QTableWidgetItem(""))
            self.friday_table.setItem(a, 1, QTableWidgetItem(""))
            self.friday_table.setItem(a, 2, QTableWidgetItem(""))
            self.friday_table.setItem(a, 3, QTableWidgetItem(""))
            self.friday_table.setItem(a, 4, QTableWidgetItem(""))
            self.friday_table.setCellWidget(a, 5, NoneButton)
            self.friday_table.setCellWidget(a, 6, addButton)

            changeButton.clicked.connect(lambda num: self._change_item_from_mond(num=1))
            changeButton1.clicked.connect(lambda num: self._change_item_from_mond(num=2))
            changeButton2.clicked.connect(lambda num: self._change_item_from_mond(num=3))
            changeButton3.clicked.connect(lambda num: self._change_item_from_mond(num=4))
            changeButton4.clicked.connect(lambda num: self._change_item_from_mond(num=5))
            changeButton5.clicked.connect(lambda num: self._change_item_from_mond(num=6))
            changeButton6.clicked.connect(lambda num: self._change_item_from_mond(num=7))
            changeButton7.clicked.connect(lambda num: self._change_item_from_mond(num=8))
            changeButton8.clicked.connect(lambda num: self._change_item_from_mond(num=9))
            changeButton9.clicked.connect(lambda num: self._change_item_from_mond(num=10))

            deleteButton.clicked.connect(lambda num: self._delete_item_from_mond(num=0))
            deleteButton1.clicked.connect(lambda num: self._delete_item_from_mond(num=1))
            deleteButton2.clicked.connect(lambda num: self._delete_item_from_mond(num=2))
            deleteButton3.clicked.connect(lambda num: self._delete_item_from_mond(num=3))
            deleteButton4.clicked.connect(lambda num: self._delete_item_from_mond(num=4))
            deleteButton5.clicked.connect(lambda num: self._delete_item_from_mond(num=5))
            deleteButton6.clicked.connect(lambda num: self._delete_item_from_mond(num=6))
            deleteButton7.clicked.connect(lambda num: self._delete_item_from_mond(num=7))
            deleteButton8.clicked.connect(lambda num: self._delete_item_from_mond(num=8))
            deleteButton9.clicked.connect(lambda num: self._delete_item_from_mond(num=9))

            addButton.clicked.connect(lambda: self._add_item_to_mondaytable())

        self.friday_table.resizeRowsToContents()


    def _change_day_from_table(self, rowNum, day):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE SQL запрос на изменение одной строки в базе данных", (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _update_shedule(self):
        self._update_monday_table()


app = QApplication(sys.argv)

win = MainWindow()
win.show()

sys.exit(app.exec_())


