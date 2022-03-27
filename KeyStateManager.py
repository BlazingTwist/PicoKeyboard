import digitalio


class KeyStateManager:
    def __init__(self, pin_ids, in_pin_indices, out_pin_indices):
        self.key_states = int(0)

        self.in_pin_count = len(in_pin_indices)
        self.out_pin_count = len(out_pin_indices)

        self.in_pins = [KeyStateManager.prepare_in_pin(pin_ids[pinIDX]) for pinIDX in in_pin_indices]
        self.out_pins = [KeyStateManager.prepare_out_pin(pin_ids[pinIDX]) for pinIDX in out_pin_indices]

    @staticmethod
    def prepare_in_pin(pin_id):
        pin = digitalio.DigitalInOut(pin_id)
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.DOWN
        return pin

    @staticmethod
    def prepare_out_pin(pin_id):
        pin = digitalio.DigitalInOut(pin_id)
        pin.direction = digitalio.Direction.INPUT
        return pin

    def get_key_status(self, key_id):
        return (self.key_states & (0b1 << key_id)) > 0

    def set_key_pressed(self, key_id):
        self.key_states |= (0b1 << key_id)

    def set_key_released(self, key_id):
        self.key_states &= ~(0b1 << key_id)

    def toggle_key_state(self, key_id):
        self.key_states ^= (0b1 << key_id)

    def pin_idx_to_key_id(self, in_pin_idx, out_pin_idx):
        return (self.in_pin_count * out_pin_idx) + in_pin_idx

    def poll_for_changes(self, callback):
        for out_pin_idx in range(self.out_pin_count):
            out_pin = self.out_pins[out_pin_idx]
            out_pin.direction = digitalio.Direction.OUTPUT
            out_pin.value = True

            for in_pin_idx in range(self.in_pin_count):
                in_pin = self.in_pins[in_pin_idx]
                is_key_pressed = in_pin.value
                if self.get_key_status(self.pin_idx_to_key_id(in_pin_idx, out_pin_idx)) is not is_key_pressed:
                    callback(in_pin_idx, out_pin_idx, is_key_pressed)

            out_pin.value = False
            out_pin.direction = digitalio.Direction.INPUT

    def get_any_key_pressed_out(self, out_pin: int) -> bool:
        # return true, if any key involving this outPinIndex is pressed
        out_pin_shift_amount = out_pin * self.in_pin_count
        in_pin_bitmask = (1 << self.in_pin_count) - 1  # e.g. for pin_count == 3 -> (1<<3)-1 = 0b111
        return ((self.key_states >> out_pin_shift_amount) & in_pin_bitmask) > 0

    def get_any_key_pressed_in(self, in_pin: int) -> bool:
        # return true, if any key involving this inPinIndex is pressed
        for out_idx in range(self.out_pin_count):
            shift_amount = (out_idx * self.in_pin_count) + in_pin
            if (self.key_states >> shift_amount) & 0b1:
                return True
        return False
