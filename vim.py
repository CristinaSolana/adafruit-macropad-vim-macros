# MACROPAD Hot"keys": VIM

from adafruit_hid.keycode import Keycode

# Colors | Find more at: https://www.color-hex.com/
black = 0x000000
white = 0x101010
red = 0xFF0000
green = 0x8CFF00
blue = 0x000040
yellow = 0xFFC100
purple = 0xBE29EC
hot_pink = 0xff1177
teal = 0x07EAA1

# Keys | API docs: https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html
key_enter = Keycode.ENTER
key_control = Keycode.CONTROL
key_command = Keycode.COMMAND

open_nvim = {"label": "open", "keys": ["nvim", key_enter]}

# Windows
split_vertically = {"label": "vsplit", "keys": [41, ":", "vsplit", key_enter]}
split_horizontally = {"label": "hsplit", "keys": [41, ":", "split", key_enter]}

# Windows:Navigate
move_to_top_window = {"label": "up", "keys": [41, key_control, "w", "k"]}
move_to_right_window = {"label": "right", "keys": [41, key_control, "w", "l"]}
move_to_bottom_window = {"label": "down", "keys": [41, key_control, "w", "j"]}
move_to_left_window = {"label": "left", "keys": [41, key_control, "w", "h"]}

# Windows:Sizing
maximize_window_vertically = {"label": "max v", "keys": [41, key_control, "w", "_"]}
maximize_window_horizontally = {"label": "max h", "keys": [41, key_control, "w", "|"]}
all_windows_same_size = {"label": "eq sz", "keys": [41, key_control, "w", "="]}

# Tabs
tab_new = {"label": "n tab", "keys": [41, ":", "tabnew", key_enter]}
tab_first = {"label": "f tab", "keys": [41, ":", "tabfirst", key_enter]}
tab_last = {"label": "l tab", "keys": [41, ":", "tablast", key_enter]}
open_files_in_tabs = {"label": "f2t", "keys": [41, ":", "tab ball", key_enter]}

# Files
open_telescope = {"label": "files", "keys": [49, "f", "f"]}
vsplit_integrated_file_explorer = {"label": "files", "keys":  [":", "Sex!", key_enter]}

# Exiting Vim. It's easy!
close = {"label": "close", "keys": [41, ":", "q", key_enter]}
write_close = {"label": "wclose", "keys": [41, ":", "wq", key_enter]}

app = {
    "name": "Vim",
    "macros": [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (green, open_nvim["label"], open_nvim["keys"]),
        (teal, split_vertically["label"], split_vertically["keys"]),
        (teal, split_horizontally["label"], split_horizontally["keys"]),
        # 2nd row ----------
        (white, close["label"], close["keys"]),
        (teal, maximize_window_vertically["label"], maximize_window_vertically["keys"]),
        (teal, maximize_window_horizontally["label"], maximize_window_horizontally["keys"]),
        # 3rd row ----------
        (yellow, write_close["label"], write_close["keys"]),
        (hot_pink, move_to_top_window["label"], move_to_top_window["keys"]),
        (hot_pink, move_to_right_window["label"], move_to_right_window["keys"]),
        # 4th row ----------
        (purple, open_telescope["label"], open_telescope["keys"]),  # Telescope
        (hot_pink, move_to_bottom_window["label"], move_to_bottom_window["keys"]),
        (hot_pink, move_to_left_window["label"], move_to_left_window["keys"]),
        # Encoder ----------
        (black, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}
