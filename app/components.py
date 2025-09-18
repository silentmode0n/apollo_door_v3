from .config import (
    BACK_IMG_MAPS,
    BLUEPRINT_MAPS,
    BOX_IMG_MAPS,
    MODEL_MAPS,
    FRAMETYPE_MAPS,
    SETUP_FOR_MODEL_MAPS,
    OPEN_IMG_MAPS,
)


class Tube():
    def __init__(self, a: int, b: int, c: int|None=None):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        if self.c:
            return f'{self.a}x{self.b}x{self.c}'
        else:
            return f'{self.a}x{self.b}'


class Door():
    def __init__(self, data: dict):
        self._data = data

    def get_setup(self):
        frametype = self.get_frametype()
        return SETUP_FOR_MODEL_MAPS.get(frametype + self._data['open'])

    def get_model(self):
        return MODEL_MAPS.get(self._data['bridge'])

    def get_filename_open_view(self):
        return OPEN_IMG_MAPS.get(self._data['side'] + self._data['open'])

    def get_filename_back_view(self):
        return BACK_IMG_MAPS.get(self._data['bridge'] + self._data['side'])

    def get_filename_box_view(self):
        return BOX_IMG_MAPS.get(self._data['box'])

    def get_frametype(self):
        return FRAMETYPE_MAPS.get(self._data['filling'])

    def get_filename_blueprint(self):
        frametype = self.get_frametype()
        return BLUEPRINT_MAPS.get(
            frametype + self._data['bridge'] + self._data['open'] + self._data['side']
            )

    def get_data_from_model(self): #TODO: write method get_data_from_model()
        setup = self.get_setup()
        Model = self.get_model()
        return Model(**self._data, **setup).get_data()

    def update_data(self):
        self._data['filename_open_view'] = self.get_filename_open_view()
        self._data['filename_back_view'] = self.get_filename_back_view()
        self._data['filename_box_view'] = self.get_filename_box_view()
        self._data['filename_blueprint'] = self.get_filename_blueprint()
        self._data.update(self.get_data_from_model())