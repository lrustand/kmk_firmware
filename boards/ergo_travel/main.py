from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT
#split = Split(split_type=SplitType.BLE, split_side=split_side)
split = Split(split_type=SplitType.UART, split_side=split_side)

modtap = ModTap()
layers_ext = Layers()
keyboard.modules = [layers_ext, modtap, split]
keyboard.extensions = []

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.LT(1, KC.SPC)
RAISE = KC.LT(2, KC.SPC)
ADJUST = KC.MO(3)

LCTL = KC.MT(KC.ESC,KC.LCTL)
HYPER = KC.MT(KC.TAB, KC.CAPS)

keyboard.keymap = [
    [  #QWERTY
                          KC.W,    KC.E,    KC.R,    KC.T,                      KC.BSPC, KC.Y,    KC.U,    KC.I,    KC.O,
        HYPER,   KC.Q,    KC.S,    KC.D,    KC.F,    KC.G,                      KC.ENT,  KC.H,    KC.J,    KC.K,    KC.L,    KC.P,    XXXXXXX,
        KC.LSFT, KC.A,    KC.X,    KC.C,    KC.V,    KC.B,                               KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SCLN, KC.QUOT,
        LCTL,    KC.Z,                      KC.LALT, KC.LWIN, LOWER,            RAISE ,  KC.RWIN, KC.RALT,          XXXXXXX, KC.SLSH, KC.RSFT
    ],
    [  #LOWER
                           KC.AT,   KC.HASH, KC.DLR,  KC.PERC,                  KC.DEL,   KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN,
        KC.TILD, KC.EXLM,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                  XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.RPRN, XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                            XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.MINS, XXXXXXX,
        XXXXXXX, XXXXXXX,                    XXXXXXX, XXXXXXX, XXXXXXX,         ADJUST,   XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX, XXXXXXX
    ],
    [  #RAISE
                           KC.N2,   KC.N3,   KC.N4,   KC.N5,                    XXXXXXX,  KC.N6,   KC.N7,   KC.N8,   KC.N9,
        KC.GRV,  KC.N1,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                  XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.N0,   XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                            XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.UNDS, XXXXXXX,
        XXXXXXX, XXXXXXX,                    XXXXXXX, XXXXXXX, ADJUST,          XXXXXXX,  XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX, XXXXXXX
    ],
    [  #ADJUST
                           KC.F2,   KC.F3,   KC.F4,   KC.F5,                    XXXXXXX,  KC.F6,   KC.F7,   KC.F8,   KC.F9,
        XXXXXXX, KC.F1,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                  XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.F10,  XXXXXXX,
        XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                            XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX,                    XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX,  XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX, XXXXXXX
    ]
]

if __name__ == '__main__':
    keyboard.go()
