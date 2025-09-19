from enum import StrEnum


class BaseOptions(StrEnum):

    @classmethod
    def values(cls) -> list[str]:
        return [item.value for item in cls]

    @classmethod
    def by_value(cls, value: str):
        # value = value.lower()
        # for item in cls:
        #     if item.value.lower() == value:
        #         return item
        try:
            return cls(value)
        except ValueError:
            return None


class FrameType(BaseOptions):
    F20 = '20'
    F2020 = '2020'
    F40 = '40'
    F45 = '45'
    F60 = '60'
    FGR = 'GR'


class Filling(BaseOptions):
    CUSTOMER20 = 'заказчика (20мм)'
    CUSTOMER2020 = 'заказчика (20+20мм)'
    CUSTOMER40 = 'заказчика (40мм)'
    CUSTOMER60 = 'заказчика (60мм)'
    CC10 = 'профлист СС10 шагрень 1ст'
    CC10_X2 = 'Профлист 2ст'
    SANDVICH_DH = 'сэндвич S-гофр DoorHan'
    Z110 = 'жалюзи Аполло Z110'
    AG77 = 'профиль AG/77'
    PD77 = 'профиль PD/77'
    AER55S = 'профиль AER55/S'
    AER55mS = 'профиль AER55m/S'
    TECHNO_L = 'Техно L'
    TECHNO_M = 'Техно M'
    GRID_3D = 'сетка сварная 3D'
    GRID_20X20 = 'обрешетка из трубы 20х20'
    GRID_30X30 = 'обрешетка из трубы 30х30'
    SIDING = 'металлосайдинг с 2 сторон'
    SIDING_KVADRO = 'металлосайдинг квадро-брус'
    PICKET_FENCE = 'штакетник шагрень 1ст'
    PICKET_FENCE_X2 = 'штакетник шагрень 2ст'


class Open(BaseOptions):
    OUT = 'на улицу'
    IN = 'во двор'


class Side(BaseOptions):
    LEFT = 'слева'
    RIGHT = 'справа'


class Bridge(BaseOptions):
    YES = 'с перемычкой'
    YES_S = 'с перемычкой и порогом'
    NO = 'без перемычки'
    PANEL = 'с фальш-панелью'


class Step(BaseOptions):
    NO = 'без порога'
    YES = 'с порогом'


class Box(BaseOptions):
    DIRECT = 'торцевая'
    CORNER = 'угловая'


class Paint(BaseOptions):
    SHAGREEN = 'шагрень'
    MATTE = 'матовый'
    GLOSS = 'глянец'
    MOIRE = 'муар'


class Batten(BaseOptions):
    NO = 'НЕТ'
    STEEL = '30х30 сталь'
    ALUM = 'AES 30x20 алюминий'


class Flexible(BaseOptions):
    NO = 'НЕТ'
    YES = 'ДА'


class Closer(BaseOptions):
    NO = 'НЕТ'
    YES = 'ДА'


class Sticker(BaseOptions):
    YES = 'ДА'
    NO = 'НЕТ'


class InFasade(BaseOptions):
    NO = 'НЕТ'
    YES = 'ДА'


class Bump(BaseOptions):
    NO = 'НЕТ'
    YES = 'ДА'


class Handle(BaseOptions):
    NO = 'НЕТ'
    MUSHROOM = 'грибок'
    BRACKET = 'скоба'
    PURE_3548V = 'Dorma Pure (шар)'
    PURE_8100 = 'Dorma Pure нажимная (изогнутая)'
    PURE_8906 = 'Dorma Pure нажимная (прямая)'


class Lock(BaseOptions):
    NO = 'НЕТ'
    ISEO = 'врезной эл.механический'
    LATCH = 'электрозащелка'