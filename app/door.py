from .options import FrameType
from .models import ModelBase
from .config import (
    BACK_IMG_MAPS,
    BLUEPRINT_MAPS,
    BOX_IMG_MAPS,
    MODEL_MAPS,
    FRAMETYPE_MAPS,
    SETUP_FOR_MODEL_MAPS,
    OPEN_IMG_MAPS,
)


class Door:
    def __init__(self, data: dict[str, str]):
        self._data = data

    def get_setup(self) -> dict[str, str]:
        frametype = self.get_frametype()
        return SETUP_FOR_MODEL_MAPS.get(frametype + self._data['open'])

    def get_model(self) -> ModelBase | None:
        return MODEL_MAPS.get(self._data['bridge'])

    def get_filename_open_view(self) -> str:
        return OPEN_IMG_MAPS.get(self._data['side'] + self._data['open'])

    def get_filename_back_view(self) -> str:
        return BACK_IMG_MAPS.get(self._data['bridge'] + self._data['side'])

    def get_filename_box_view(self) -> str:
        return BOX_IMG_MAPS.get(self._data['box'])

    def get_frametype(self) -> FrameType:
        return FRAMETYPE_MAPS.get(self._data['filling'])

    def get_filename_blueprint(self):
        frametype = self.get_frametype()
        return BLUEPRINT_MAPS.get(
            frametype + self._data['bridge'] + self._data['open'] + self._data['side']
        )

    def get_data_from_model(self):  # TODO: write method get_data_from_model()
        s = self.get_setup()
        d = self._data
        Model = self.get_model()
        return Model(
            width=d['width'],
            height=d['height'],
            cliarance=d['cliarance'],
            bridge_h=d['bridge_h'],
            tube_frame_v=s['tube_frame_v'],
            tube_frame_h=s['tube_frame_h'],
            tube_door_lock=s['tube_door_lock'],
            tube_door_hinge=s['tube_door_hinge'],
            tube_door_h=s['tube_door_h'],
            gap=s['gap'],
            fill_gap=s['fill_gap'],
        ).get_data()

    def update_data(self):
        self._data['filename_open_view'] = self.get_filename_open_view()
        self._data['filename_back_view'] = self.get_filename_back_view()
        self._data['filename_box_view'] = self.get_filename_box_view()
        self._data['filename_blueprint'] = self.get_filename_blueprint()
        self._data.update(self.get_data_from_model())
