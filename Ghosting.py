from KeyStateManager import KeyStateManager


class GhostingInfo:
    def __init__(self):
        self.out_pins_bitfield = int(0)
        self.in_pins_bitfield = int(0)
        self.rowed_out_pins_bitfield = int(0)
        self.rowed_in_pins_bitfield = int(0)

    def gather_ghosting_pins(self, key_state_manager: KeyStateManager):
        for i in range(key_state_manager.out_pin_count):
            if (self.rowed_out_pins_bitfield >> i) & 0b1:
                continue  # pin already marked as row-pin
            if (self.out_pins_bitfield >> i) & 0b1 and key_state_manager.get_any_key_pressed_out(i):
                self.rowed_out_pins_bitfield |= (0b1 << i)

        for i in range(key_state_manager.in_pin_count):
            if (self.rowed_in_pins_bitfield >> i) & 0b1:
                continue  # pin already marked as row-pin
            if (self.in_pins_bitfield >> i) & 0b1 and key_state_manager.get_any_key_pressed_in(i):
                self.rowed_in_pins_bitfield |= (0b1 << i)
