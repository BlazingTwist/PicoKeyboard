import time
import board
import digitalio


class KeyPressInfo:
    def __init__(self, in_pin_idx, out_pin_idx):
        self.in_pin_idx = in_pin_idx
        self.out_pin_idx = out_pin_idx


def initialize_pin(pin_id: board.pin.Pin) -> digitalio.DigitalInOut:
    pin = digitalio.DigitalInOut(pin_id)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.DOWN
    return pin


led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

pinIDs = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,
    board.GP15, board.GP16, board.GP17, board.GP18, board.GP19,
    board.GP20, board.GP21, board.GP22, board.GP26, board.GP27,
    board.GP28
]
pins = [initialize_pin(pin_id) for pin_id in pinIDs]

keys = [
    "NAV_BACK", "NAV_FORWARD", "NAV_CLOSE", "NAV_REFRESH", "NAV_SEARCH", "NAV_EXPLORER", "NAV_HOME", "NAV_MAIL",
    "NAV_MUTE", "NAV_SLEEP", "NAV_VOL_DOWN", "NAV_VOL_UP", "NAV_PLAY_PAUSE", "NAV_STOP_SONG", "NAV_NEXT_SONG",
    "NAV_PREV_SONG", "NAV_MEDIA_PLAYER", "NAV_DESKTOP", "NAV_KEYBOARD",
    "ESC", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "PRINT", "ROLL", "PAUSE",
    "CIRCUMFLEX", "ALPHA_1", "ALPHA_2", "ALPHA_3", "ALPHA_4", "ALPHA_5", "ALPHA_6", "ALPHA_7", "ALPHA_8", "ALPHA_9",
    "ALPHA_0", "ESZETT", "TICK", "BACKSPACE", "INSERT", "HOME", "PAGE_UP",
    "TAB", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "UMLAUT_U", "TIMES", "ENTER", "DELETE", "END", "PAGE_DOWN",
    "CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", "UMLAUT_O", "UMLAUT_A", "HASH",
    "SHIFT_LEFT", "LESS_THAN", "Y", "X", "C", "V", "B", "N", "M", "COMMA", "DOT", "MINUS", "SHIFT_RIGHT", "ARROW_UP",
    "CONTROL_LEFT", "WINDOWS_LEFT", "ALT_LEFT", "SPACE", "ALT_RIGHT", "WINDOWS_RIGHT", "CONTEXT", "CONTROL_RIGHT",
    "ARROW_LEFT", "ARROW_DOWN", "ARROW_RIGHT",
    "NUMPAD", "NUMPAD_SLASH", "NUMPAD_TIMES", "NUMPAD_MINUS",
    "NUMPAD_7", "NUMPAD_8", "NUMPAD_9", "NUMPAD_PLUS",
    "NUMPAD_4", "NUMPAD_5", "NUMPAD_6",
    "NUMPAD_1", "NUMPAD_2", "NUMPAD_3", "NUMPAD_ENTER",
    "NUMPAD_0", "NUMPAD_COMMA"
]
keyDict = {}


def get_pressed_pins():
    pressed_pins = []
    for i in range(len(pins) - 1):
        out_pin = pins[i]
        out_pin.direction = digitalio.Direction.OUTPUT
        out_pin.value = True

        for i2 in range(i + 1, len(pins)):
            in_pin = pins[i2]
            if in_pin.value:
                pressed_pins.append(KeyPressInfo(i, i2))

        out_pin.value = False
        out_pin.direction = digitalio.Direction.INPUT
        out_pin.pull = digitalio.Pull.DOWN
    return pressed_pins


def main():
    for key in keys:
        print("press", key)
        while True:
            pressed_pins = get_pressed_pins()
            if len(pressed_pins) == 1:
                press_info = pressed_pins[0]
                print("got pin_A:", press_info.in_pin_idx, "| pin_B:", press_info.out_pin_idx)
                keyDict[key] = press_info
                break
        time.sleep(0.15)

    for key in keys:
        press_info = keyDict[key]
        print(key, press_info.in_pin_idx, press_info.out_pin_idx, sep="\t")


main()
