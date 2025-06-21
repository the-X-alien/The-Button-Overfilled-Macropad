import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.OLED import OLED
from adafruit_display_text import label
import terminalio

keyboard = KMKKeyboard()
keyboard.matrix = MatrixScanner(
    column_pins=(board.GP26, board.GP27, board.GP28, board.GP29),
    row_pins=(board.GP8, board.GP9, board.GP10, board.GP11),
    columns_to_anodes=False
)

macros = Macros()
keyboard.modules.append(macros)

keyboard.keymap = [[
    KC.N7, KC.N8, KC.N9, KC.SLSH,
    KC.N4, KC.N5, KC.N6, KC.ASTR,
    KC.N1, KC.N2, KC.N3, KC.EQL,
    KC.MACRO('dhiaandave@outlook.com'), KC.MACRO("dd104162@student.musd"), KC.MACRO("This is a filler for my password"), KC.MACRO('1470 Los Buellis Way')
]]

def show(_):
    return [label.Label(terminalio.FONT, text='Dhiaan', x=0, y=8)]

keyboard.extensions.append(
    OLED(
        oled_handler=show,
        i2c=board.I2C(),
        width=128,
        height=32,
        address=0x3C
    )
)

if __name__ == '__main__':
    keyboard.go()
