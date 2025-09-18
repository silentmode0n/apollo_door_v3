from icecream import ic
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QFormLayout,
    QLineEdit,
    QDateEdit,
    QComboBox,
    QTextEdit,
    QPushButton,
    QCheckBox,
    QFileDialog,
)
from PySide6.QtCore import (
    QDate,
)
from PySide6.QtGui import (
    QIntValidator,
    QIcon,
)
from .config import (
    HOMEDIR,
    ICO_FILE,
    TITLE,
)
from .options import (
    Batten,
    Bump,
    Closer,
    Filling,
    Flexible,
    InFasade,
    Open,
    Side,
    Bridge,
    Box,
    Step,
    Paint,
    Handle,
    Lock,
    Sticker,
)
from .door import Door


class AQLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_text(self, text):
        self.setText(text)


class AQComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def text(self):
        return self.currentText()

    def set_text(self, text):
        self.setCurrentText(text)


class AQTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def text(self):
        return self.toPlainText()

    def set_text(self, text):
        self.setText(text)


class AQCheckBox(QCheckBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def text(self):
        return self.isChecked()


class DictMixin():
    def get_data(self):
        # module = sys.modules[__name__]
        # for validator in [v for k, v in module.__dict__.items() if k.startswith('validate_of_')]:
        #     errors += validator(data)
        # return errors
        data = {k[2:]: v.text() for k, v in self.__dict__.items() if k.startswith('d_')}
        return data

    def set_data(self, data):
        for k, v in self.__dict__.items():
            if k.startswith('d_') and k[2:] in data:
                self.__dict__[k].set_text(data[k[2:]])


class OrderGroup(QGroupBox, DictMixin):
    def __init__(self):
        super().__init__('Информация о заказе')

        self.d_order = AQLineEdit()
        self.d_customer = AQLineEdit()
        self.d_date = QDateEdit(date=QDate.currentDate(), minimumDate=QDate.currentDate())
        self.d_engeener = AQLineEdit()

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        form_left = QFormLayout()
        col_left = QWidget()
        col_left.setLayout(form_left)
        form_left.addRow("№ Заказа", self.d_order)
        form_left.addRow("Заказчик", self.d_customer)

        form_right = QFormLayout()
        col_right = QWidget()
        col_right.setLayout(form_right)
        form_right.addRow("Дата готовности", self.d_date)
        form_right.addRow("Инженер", self.d_engeener)

        layout.addWidget(col_left)
        layout.addWidget(col_right)


class DoorGroup(QGroupBox, DictMixin):
    def __init__(self):
        super().__init__('Параметры калитки')

        self.d_width = AQLineEdit()
        self.d_width.setValidator(QIntValidator())
        self.d_height = AQLineEdit()
        self.d_height.setValidator(QIntValidator())
        self.d_open = AQComboBox()
        self.d_open.addItems(Open)
        self.d_side = AQComboBox()
        self.d_side.addItems(Side)
        self.d_bridge = AQComboBox()
        self.d_bridge.addItems(Bridge)
        self.d_bridge.currentTextChanged.connect(self.bridge_handler)
        self.d_step = AQComboBox()
        self.d_step.addItems(Step)
        self.d_box = AQComboBox()
        self.d_box.addItems(Box)
        self.d_cliarance = AQLineEdit()
        self.d_cliarance.setValidator(QIntValidator())
        self.d_bridge_h = AQLineEdit()
        self.d_bridge_h.setValidator(QIntValidator())
        self.d_frame_color = AQLineEdit()
        self.d_frame_paint = AQComboBox()
        self.d_frame_paint.addItems(Paint)
        self.d_filling = AQComboBox()
        self.d_filling.addItems(Filling)
        self.d_filling_color_in = AQLineEdit()
        self.d_filling_color_out = AQLineEdit()
        self.d_lock = AQComboBox()
        self.d_lock.addItems(Lock)
        self.d_handle_in = AQComboBox()
        self.d_handle_in.addItems(Handle)
        self.d_handle_out = AQComboBox()
        self.d_handle_out.addItems(Handle)
        self.d_flexible = AQComboBox()
        self.d_flexible.addItems(Flexible)
        self.d_closer = AQComboBox()
        self.d_closer.addItems(Closer)
        self.d_batten = AQComboBox()
        self.d_batten.addItems(Batten)
        self.d_batten_len = AQLineEdit()
        self.d_batten_len.setValidator(QIntValidator())
        self.d_batten_num = AQLineEdit()
        self.d_batten_num.setValidator(QIntValidator())
        self.d_stiker = AQComboBox()
        self.d_stiker.addItems(Sticker)
        self.d_in_fasade = AQComboBox()
        self.d_in_fasade.addItems(InFasade)
        self.d_bump = AQComboBox()
        self.d_bump.addItems(Bump)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        form_left = QFormLayout()
        col_left = QWidget()
        col_left.setLayout(form_left)
        form_left.addRow("Ширина калитки, мм", self.d_width)
        form_left.addRow("Высота калитки, мм", self.d_height)
        form_left.addRow("Открытие", self.d_open)
        form_left.addRow("Петли (вид со двора)", self.d_side)
        form_left.addRow("Перемычка", self.d_bridge)
        form_left.addRow("Высота ФП, мм", self.d_bridge_h)
        form_left.addRow("Порог", self.d_step)
        form_left.addRow("Просвет, мм", self.d_cliarance)
        form_left.addRow("Тип рамы", self.d_box)
        form_left.addRow("Цвет рамы", self.d_frame_color)
        form_left.addRow("Тип покраски", self.d_frame_paint)

        form_right = QFormLayout()
        col_right = QWidget()
        col_right.setLayout(form_right)
        form_right.addRow("Наполнение", self.d_filling)
        form_right.addRow("Цвет наполнения снаружи", self.d_filling_color_out)
        form_right.addRow("Цвет наполнения изнутри", self.d_filling_color_in)
        form_right.addRow("Замок", self.d_lock)
        form_right.addRow("Ручка снаружи", self.d_handle_out)
        form_right.addRow("Ручка изнутри", self.d_handle_in)
        form_right.addRow("Гибкий переход", self.d_flexible)
        form_right.addRow("Доводчик", self.d_closer)
        form_right.addRow("Нащельник", self.d_batten)
        form_right.addRow("Длина нащельника, мм", self.d_batten_len)
        form_right.addRow("Кол-во нащельников, шт", self.d_batten_num)
        form_right.addRow("В фасаде с воротами", self.d_in_fasade)
        form_right.addRow("Стикер Аполло", self.d_stiker)
        form_right.addRow("Ограничитель RS0301", self.d_bump)

        layout.addWidget(col_left)
        layout.addWidget(col_right)

    def bridge_handler(self, value):
        if Bridge.by_value(value) != Bridge.PANEL:
            self.d_bridge_h.setText('0')
            self.d_bridge_h.setReadOnly(True)
        else:
            self.d_bridge_h.setReadOnly(False)


class CommentGroup(QGroupBox, DictMixin):
    def __init__(self):
        super().__init__('Комментарий')

        self.d_comments = AQTextEdit()

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        layout.addWidget(self.d_comments)


class ButtonGroup(QGroupBox, DictMixin):
    def __init__(self):
        super().__init__('Подготовка чертежа')

        self.submit = QPushButton('Чертеж')
        self.d_for_client = QCheckBox('Для клиента')
        self.d_for_client.setChecked(True)
        self.d_for_manufacture = QCheckBox('Для производства')
        self.d_for_manufacture.setChecked(True)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        layout.addWidget(self.submit)
        layout.addWidget(self.d_for_client)
        layout.addWidget(self.d_for_manufacture)
        layout.addStretch()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(TITLE)
        icon = QIcon(ICO_FILE)
        self.setWindowIcon(icon)

        main_layout = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.order_group = OrderGroup()
        self.door_group = DoorGroup()
        self.comments_group = CommentGroup()
        self.button_group = ButtonGroup()
        self.button_group.submit.clicked.connect(self.submit_handler)

        main_layout.addWidget(self.order_group)
        main_layout.addWidget(self.door_group)
        main_layout.addWidget(self.comments_group)
        main_layout.addWidget(self.button_group)

    def get_save_as_filename(self) -> str:
        filename, _ = QFileDialog.getSaveFileName(
            caption='Сохранить как',
            dir=HOMEDIR,
            filter=('PDF files (*.pdf)')
        )
        return filename

    def get_data(self) -> dict:
        data = {}
        for gr in [self.order_group, self.door_group, self.comments_group, self.button_group]:
            data.update(gr.get_data())
        return data

    def set_data(self, data: dict):
        for gr in [self.order_group, self.door_group, self.comments_group, self.button_group]:
            gr.set_data(data)

    def submit_handler(self):
        """MAIN HANDLER"""
        filepath = self.get_save_as_filename()
        if filepath:
            data = self.get_data()
            data['filepath_to_save'] = filepath
            door = Door(data)
            door.update_data()
            ic(data)