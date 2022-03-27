import time
import board
import digitalio
import KeyMapper
import KeyStateManager
from Ghosting import GhostingInfo


class KeyPressInfo:
    def __init__(self, in_pin_idx, out_pin_idx):
        self.in_pin_idx = in_pin_idx
        self.out_pin_idx = out_pin_idx


led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

pinIDs = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16,
    board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,
    board.GP22, board.GP26, board.GP27, board.GP28
]
inPinIDXs = [0, 1, 2, 3, 4, 23, 24, 25]
outPinIDXs = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

keyStateManager = KeyStateManager.KeyStateManager(pinIDs, inPinIDXs, outPinIDXs)
keyMapper = KeyMapper.KeyMapper()

justPressedKeys = []


def poll_callback(in_pin_idx, out_pin_idx, is_key_pressed):
    if is_key_pressed:
        justPressedKeys.append(KeyPressInfo(in_pin_idx, out_pin_idx))
    else:
        pin_code = keyStateManager.pin_idx_to_key_id(in_pin_idx, out_pin_idx)
        keyStateManager.set_key_released(pin_code)
        keyMapper.handle_key_change(pin_code, False)


def main():
    print("program started!")
    led.value = True
    time.sleep(0.25)
    led.value = False

    while True:
        keyStateManager.poll_for_changes(poll_callback)

        if len(justPressedKeys) > 0:
            ghost_info = GhostingInfo()
            # gather ghosting info
            for key_info in justPressedKeys:
                if (ghost_info.out_pins_bitfield >> key_info.out_pin_idx) & 0b1:
                    ghost_info.rowed_out_pins_bitfield |= (0b1 << key_info.out_pin_idx)
                else:
                    ghost_info.out_pins_bitfield |= (0b1 << key_info.out_pin_idx)

                if (ghost_info.in_pins_bitfield >> key_info.in_pin_idx) & 0b1:
                    ghost_info.rowed_in_pins_bitfield |= (0b1 << key_info.in_pin_idx)
                else:
                    ghost_info.in_pins_bitfield |= (0b1 << key_info.in_pin_idx)
            ghost_info.gather_ghosting_pins(keyStateManager)

            # handle pressed keys that are not ghosted
            for key_info in justPressedKeys:
                if not ((ghost_info.rowed_out_pins_bitfield >> key_info.out_pin_idx) & 0b1) \
                        or not ((ghost_info.rowed_in_pins_bitfield >> key_info.in_pin_idx) & 0b1):
                    pin_code = keyStateManager.pin_idx_to_key_id(key_info.in_pin_idx, key_info.out_pin_idx)
                    keyStateManager.set_key_pressed(pin_code)
                    keyMapper.handle_key_change(pin_code, True)

            justPressedKeys.clear()

        time.sleep(0.01)


main()
