from .components import Tube


class ModelBase:
    def __init__(
        self,
        width: int | str,
        height:  int | str,
        cliarance:  int | str,
        bridge_h:  int | str,
        tube_frame_v: Tube,
        tube_frame_h: Tube,
        tube_door_lock: Tube,
        tube_door_hinge: Tube,
        tube_door_h: Tube,
        gap: int = 10,
        fill_gap: int = 5,
    ):
        self._data = {}
        self.width = int(width)
        self.height = int(height)
        self.cliarance = int(cliarance)
        self.bridge_h = int(bridge_h) #FIXME: add test is_digits or replace '' on 0 in gui.py
        self.tube_frame_v = tube_frame_v
        self.tube_frame_h = tube_frame_h  # (y, x)
        self.tube_door_lock = tube_door_lock  # (y, x)
        self.tube_door_hinge = tube_door_hinge  # (y, x)
        self.tube_door_h = tube_door_h
        self.gap = gap
        self.fill_gap = fill_gap

    def get_data(self) -> dict[str,str]:
        self._update()
        return self._data

    def _update(self):
        self._data['width'] = str(self.width)
        self._data['height'] = str(self.height)
        self._data['cliarance'] = str(self.get_cliarance())
        self._data['bridge_h'] = str(self.bridge_h)
        self._data['door_width'] = str(self.get_door_width())
        self._data['door_height'] = str(self.get_door_height())
        self._data['door_fill_width'] = str(self.get_door_fill_width())
        self._data['door_fill_height'] = str(self.get_door_fill_height())
        self._data['bridge_fill_width'] = str(self.get_bridge_fill_width())
        self._data['bridge_fill_height'] = str(self.get_bridge_fill_height())

    def get_cliarance(self) -> int:
        return self.cliarance

    def get_door_width(self) -> int:
        return self.width - self.tube_frame_v.a * 2 - self.gap * 2

    def get_door_height(self) -> int:
        return self.height - self.get_cliarance() - self.tube_frame_h.a - self.gap

    def get_door_fill_width(self) -> int:
        return self.get_door_width() - self.tube_door_lock.a - self.tube_door_hinge.a - self.fill_gap

    def get_door_fill_height(self) -> int:
        return self.get_door_height() - self.tube_door_h.a * 2 - self.fill_gap

    def get_bridge_fill_width(self) -> int:
        return 0

    def get_bridge_fill_height(self) -> int:
        return 0


class ModelBridgeY(ModelBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ModelBridgeN(ModelBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_door_height(self):
        return self.height - self.get_cliarance()


class ModelBridgeYS(ModelBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_cliarance(self):
        return max(self.cliarance, self.tube_frame_h.a + self.gap)


class ModelBridgeP(ModelBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_door_height(self):
        return self.height - self.get_cliarance() - self.bridge_h - self.gap

    def get_bridge_fill_width(self):
        return self.width - self.tube_frame_v.a * 2 - self.fill_gap

    def get_bridge_fill_height(self):
        return self.bridge_h - self.tube_frame_h.a * 2 - self.fill_gap
