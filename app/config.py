import os
from .options import (
    Box,
    Filling,
    Open,
    Side,
    Bridge,
    FrameType,
)
from .models import (
    ModelBridgeY,
    ModelBridgeN,
    ModelBridgeP,
    ModelBridgeYS,
    )
from .components import Tube


VERSION = "v-3.0.0-a"

TITLE = f'Калитка Аполло    {VERSION}'

# текущий каталог
CWD = os.getcwd()

# каталог статики
STATIC = os.path.join(CWD, 'app', 'static')

# домашняя папка пользователя
HOMEDIR = os.path.expanduser('~')

# файлы
LOG_FILE = os.path.join(CWD, 'logging.log')
ICO_FILE = os.path.join(STATIC, 'ico', 'logo.ico')

# файлы вида рамы
BOX_IMG_MAPS = {
    Box.DIRECT: 'direct.png',
    Box.CORNER: 'angel.png',
}

# файлы вида открытия
OPEN_IMG_MAPS = {
    Side.LEFT + Open.IN: 'left_in.png',
    Side.LEFT + Open.OUT: 'left_out.png',
    Side.RIGHT + Open.IN: 'right_in.png',
    Side.RIGHT + Open.OUT: 'right_out.png',
}

# файлы общего вида
BACK_IMG_MAPS = {
    Bridge.NO + Side.LEFT: 'bridge_n_left_direct.png',
    Bridge.NO + Side.RIGHT: 'bridge_n_right_direct.png',
    Bridge.YES + Side.LEFT: 'bridge_y_left_direct.png',
    Bridge.YES + Side.RIGHT: 'bridge_y_right_direct.png',
    Bridge.YES_S + Side.LEFT: 'bridge_ys_left_direct.png',
    Bridge.YES_S + Side.RIGHT: 'bridge_ys_right_direct.png',
    Bridge.PANEL + Side.LEFT: 'bridge_t_left_direct.png',
    Bridge.PANEL + Side.RIGHT: 'bridge_t_right_direct.png',
}

#TODO: Fill FRAMETYPE_MAPS
FRAMETYPE_MAPS = {
    Filling.CUSTOMER: FrameType.F20, 
}

MODEL_MAPS = {
    Bridge.NO: ModelBridgeN,
    Bridge.YES: ModelBridgeY,
    Bridge.YES_S: ModelBridgeYS,
    Bridge.PANEL: ModelBridgeP,
}

#TODO: fill BLUEPRINT_MAPS
BLUEPRINT_MAPS = {
    #F20
    FrameType.F20+Bridge.YES+Open.OUT+Side.LEFT: '',
    FrameType.F20+Bridge.YES+Open.OUT+Side.RIGHT: '',
    FrameType.F20+Bridge.YES+Open.IN+Side.LEFT: '',
    FrameType.F20+Bridge.YES+Open.IN+Side.RIGHT: '',
    FrameType.F20+Bridge.YES_S+Open.OUT+Side.LEFT: '',
    FrameType.F20+Bridge.YES_S+Open.OUT+Side.RIGHT: '',
    FrameType.F20+Bridge.YES_S+Open.IN+Side.LEFT: '',
    FrameType.F20+Bridge.YES_S+Open.IN+Side.RIGHT: '',
    FrameType.F20+Bridge.NO+Open.OUT+Side.LEFT: '',
    FrameType.F20+Bridge.NO+Open.OUT+Side.RIGHT: '',
    FrameType.F20+Bridge.NO+Open.IN+Side.LEFT: '',
    FrameType.F20+Bridge.NO+Open.IN+Side.RIGHT: '',
    FrameType.F20+Bridge.PANEL+Open.OUT+Side.LEFT: '',
    FrameType.F20+Bridge.PANEL+Open.OUT+Side.RIGHT: '',
    FrameType.F20+Bridge.PANEL+Open.IN+Side.LEFT: '',
    FrameType.F20+Bridge.PANEL+Open.IN+Side.RIGHT: '',
    # F2020
    FrameType.F2020+Bridge.YES+Open.OUT+Side.LEFT: '',
    FrameType.F2020+Bridge.YES+Open.OUT+Side.RIGHT: '',
    FrameType.F2020+Bridge.YES+Open.IN+Side.LEFT: '',
    FrameType.F2020+Bridge.YES+Open.IN+Side.RIGHT: '',
    FrameType.F2020+Bridge.YES_S+Open.OUT+Side.LEFT: '',
    FrameType.F2020+Bridge.YES_S+Open.OUT+Side.RIGHT: '',
    FrameType.F2020+Bridge.YES_S+Open.IN+Side.LEFT: '',
    FrameType.F2020+Bridge.YES_S+Open.IN+Side.RIGHT: '',
    FrameType.F2020+Bridge.NO+Open.OUT+Side.LEFT: '',
    FrameType.F2020+Bridge.NO+Open.OUT+Side.RIGHT: '',
    FrameType.F2020+Bridge.NO+Open.IN+Side.LEFT: '',
    FrameType.F2020+Bridge.NO+Open.IN+Side.RIGHT: '',
    FrameType.F2020+Bridge.PANEL+Open.OUT+Side.LEFT: '',
    FrameType.F2020+Bridge.PANEL+Open.OUT+Side.RIGHT: '',
    FrameType.F2020+Bridge.PANEL+Open.IN+Side.LEFT: '',
    FrameType.F2020+Bridge.PANEL+Open.IN+Side.RIGHT: '',
    # F40
    FrameType.F40+Bridge.YES+Open.OUT+Side.LEFT: '',
    FrameType.F40+Bridge.YES+Open.OUT+Side.RIGHT: '',
    FrameType.F40+Bridge.YES+Open.IN+Side.LEFT: '',
    FrameType.F40+Bridge.YES+Open.IN+Side.RIGHT: '',
    FrameType.F40+Bridge.YES_S+Open.OUT+Side.LEFT: '',
    FrameType.F40+Bridge.YES_S+Open.OUT+Side.RIGHT: '',
    FrameType.F40+Bridge.YES_S+Open.IN+Side.LEFT: '',
    FrameType.F40+Bridge.YES_S+Open.IN+Side.RIGHT: '',
    FrameType.F40+Bridge.NO+Open.OUT+Side.LEFT: '',
    FrameType.F40+Bridge.NO+Open.OUT+Side.RIGHT: '',
    FrameType.F40+Bridge.NO+Open.IN+Side.LEFT: '',
    FrameType.F40+Bridge.NO+Open.IN+Side.RIGHT: '',
    FrameType.F40+Bridge.PANEL+Open.OUT+Side.LEFT: '',
    FrameType.F40+Bridge.PANEL+Open.OUT+Side.RIGHT: '',
    FrameType.F40+Bridge.PANEL+Open.IN+Side.LEFT: '',
    FrameType.F40+Bridge.PANEL+Open.IN+Side.RIGHT: '',
    # F60
    FrameType.F60+Bridge.YES+Open.OUT+Side.LEFT: '',
    FrameType.F60+Bridge.YES+Open.OUT+Side.RIGHT: '',
    FrameType.F60+Bridge.YES+Open.IN+Side.LEFT: '',
    FrameType.F60+Bridge.YES+Open.IN+Side.RIGHT: '',
    FrameType.F60+Bridge.YES_S+Open.OUT+Side.LEFT: '',
    FrameType.F60+Bridge.YES_S+Open.OUT+Side.RIGHT: '',
    FrameType.F60+Bridge.YES_S+Open.IN+Side.LEFT: '',
    FrameType.F60+Bridge.YES_S+Open.IN+Side.RIGHT: '',
    FrameType.F60+Bridge.NO+Open.OUT+Side.LEFT: '',
    FrameType.F60+Bridge.NO+Open.OUT+Side.RIGHT: '',
    FrameType.F60+Bridge.NO+Open.IN+Side.LEFT: '',
    FrameType.F60+Bridge.NO+Open.IN+Side.RIGHT: '',
    FrameType.F60+Bridge.PANEL+Open.OUT+Side.LEFT: '',
    FrameType.F60+Bridge.PANEL+Open.OUT+Side.RIGHT: '',
    FrameType.F60+Bridge.PANEL+Open.IN+Side.LEFT: '',
    FrameType.F60+Bridge.PANEL+Open.IN+Side.RIGHT: '',
    # FGR
    FrameType.FGR+Bridge.YES+Open.OUT+Side.LEFT: '',
    FrameType.FGR+Bridge.YES+Open.OUT+Side.RIGHT: '',
    FrameType.FGR+Bridge.YES+Open.IN+Side.LEFT: '',
    FrameType.FGR+Bridge.YES+Open.IN+Side.RIGHT: '',
    FrameType.FGR+Bridge.YES_S+Open.OUT+Side.LEFT: '',
    FrameType.FGR+Bridge.YES_S+Open.OUT+Side.RIGHT: '',
    FrameType.FGR+Bridge.YES_S+Open.IN+Side.LEFT: '',
    FrameType.FGR+Bridge.YES_S+Open.IN+Side.RIGHT: '',
    FrameType.FGR+Bridge.NO+Open.OUT+Side.LEFT: '',
    FrameType.FGR+Bridge.NO+Open.OUT+Side.RIGHT: '',
    FrameType.FGR+Bridge.NO+Open.IN+Side.LEFT: '',
    FrameType.FGR+Bridge.NO+Open.IN+Side.RIGHT: '',
    FrameType.FGR+Bridge.PANEL+Open.OUT+Side.LEFT: '',
    FrameType.FGR+Bridge.PANEL+Open.OUT+Side.RIGHT: '',
    FrameType.FGR+Bridge.PANEL+Open.IN+Side.LEFT: '',
    FrameType.FGR+Bridge.PANEL+Open.IN+Side.RIGHT: '',
}

SETUP_FOR_MODEL_MAPS = {
    FrameType.F20+Open.OUT: {
        'tube_frame_v': Tube(40, 40),
        'tube_frame_h': Tube(40, 40),
        'tube_door_lock': Tube(40, 40),
        'tube_door_hinge': Tube(20, 40),
        'tube_door_h': Tube(20, 40),
        'tube_inner': Tube(20, 20),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F20+Open.IN: {
        'tube_frame_v': Tube(50, 50),
        'tube_frame_h': Tube(25, 50),
        'tube_door_lock': Tube(40, 40),
        'tube_door_hinge': Tube(20, 40),
        'tube_door_h': Tube(20, 40),
        'tube_inner': Tube(20, 20),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F2020+Open.OUT: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': Tube(20, 20),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F2020+Open.IN: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': Tube(20, 20),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F40+Open.OUT: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': Tube(20, 20),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F40+Open.IN: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': Tube(20, 20),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F45+Open.OUT: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': Tube(15, 15),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F45+Open.IN: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': Tube(15, 15),
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F60+Open.OUT: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': None,
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.F60+Open.IN: {
        'tube_frame_v': Tube(40, 60),
        'tube_frame_h': Tube(40, 60),
        'tube_door_lock': Tube(40, 60),
        'tube_door_hinge': Tube(40, 60),
        'tube_door_h': Tube(40, 60),
        'tube_inner': None,
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.FGR+Open.OUT: {
        'tube_frame_v': Tube(40, 40),
        'tube_frame_h': Tube(40, 40),
        'tube_door_lock': Tube(40, 40),
        'tube_door_hinge': Tube(20, 40),
        'tube_door_h': Tube(20, 40),
        'tube_inner': None,
        'gap': 10,
        'fill_gap': 5,
    },
    FrameType.FGR+Open.IN: {
        'tube_frame_v': Tube(50, 50),
        'tube_frame_h': Tube(25, 50),
        'tube_door_lock': Tube(40, 40),
        'tube_door_hinge': Tube(20, 40),
        'tube_door_h': Tube(20, 40),
        'tube_inner': None,
        'gap': 10,
        'fill_gap': 5,
    },
    }
