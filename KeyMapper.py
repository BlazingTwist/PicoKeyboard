import usb_hid
from lib.adafruit_hid.keyboard import Keyboard
from lib.keycode_win_de import Keycode
from lib.keyboard_layout_win_de import KeyboardLayout
from lib.adafruit_hid.consumer_control import ConsumerControl
from lib.adafruit_hid.consumer_control_code import ConsumerControlCode
import time


class KeyMapper:
    def press_or_release(self, key, is_pressed):
        self.keyboard.press(key) if is_pressed else self.keyboard.release(key)

    def nav_back(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.LEFT_ALT)
            self.keyboard.press(Keycode.LEFT_ARROW)
            self.keyboard.release(Keycode.LEFT_ARROW)
            self.keyboard.release(Keycode.LEFT_ALT)

    def nav_forward(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.LEFT_ALT)
            self.keyboard.press(Keycode.RIGHT_ARROW)
            self.keyboard.release(Keycode.RIGHT_ARROW)
            self.keyboard.release(Keycode.LEFT_ALT)

    def nav_close(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.LEFT_CONTROL)
            self.keyboard.press(Keycode.W)
            self.keyboard.release(Keycode.W)
            self.keyboard.release(Keycode.LEFT_CONTROL)

    def nav_refresh(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.LEFT_CONTROL)
            self.keyboard.press(Keycode.R)
            self.keyboard.release(Keycode.R)
            self.keyboard.release(Keycode.LEFT_CONTROL)

    def nav_search(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.LEFT_CONTROL)
            self.keyboard.press(Keycode.F)
            self.keyboard.release(Keycode.F)
            self.keyboard.release(Keycode.LEFT_CONTROL)

    def nav_explorer(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.WINDOWS)
            self.keyboard.press(Keycode.E)
            self.keyboard.release(Keycode.E)
            self.keyboard.release(Keycode.WINDOWS)

    def nav_home(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.WINDOWS)
            self.keyboard.press(Keycode.X)
            self.keyboard.release(Keycode.X)
            self.keyboard.release(Keycode.WINDOWS)
            time.sleep(0.01)
            self.keyboard.press(Keycode.Y)
            self.keyboard.release(Keycode.Y)

    def nav_mail(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.WINDOWS)
            self.keyboard.press(Keycode.X)
            self.keyboard.release(Keycode.X)
            self.keyboard.release(Keycode.WINDOWS)
            time.sleep(0.01)
            self.keyboard.press(Keycode.N)
            self.keyboard.release(Keycode.N)

    def nav_mute(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.MUTE)

    def nav_sleep(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.WINDOWS)
            self.keyboard.press(Keycode.X)
            self.keyboard.release(Keycode.X)
            self.keyboard.release(Keycode.WINDOWS)
            time.sleep(0.01)
            self.keyboard.press(Keycode.U)
            self.keyboard.release(Keycode.U)
            time.sleep(0.01)
            self.keyboard.press(Keycode.S)
            self.keyboard.release(Keycode.S)

    def nav_vol_down(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)

    def nav_vol_up(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)

    def nav_play_pause(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.PLAY_PAUSE)

    def nav_stop_song(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.STOP)

    def nav_next_song(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)

    def nav_prev_song(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.SCAN_NEXT_TRACK)

    def nav_media_player(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.LEFT_ALT)
            self.keyboard.press(Keycode.KEYPAD_FIVE)
            self.keyboard.release(Keycode.KEYPAD_FIVE)
            self.keyboard.release(Keycode.LEFT_ALT)

    def nav_desktop(self, is_pressed):
        if is_pressed:
            self.keyboard.press(Keycode.WINDOWS)
            self.keyboard.press(Keycode.M)
            self.keyboard.release(Keycode.M)
            self.keyboard.release(Keycode.WINDOWS)

    def nav_keyboard(self, is_pressed):
        if is_pressed:
            self.consumer_control.send(ConsumerControlCode.RECORD)

    def esc(self, is_pressed):
        self.press_or_release(Keycode.ESCAPE, is_pressed)

    def f1(self, is_pressed):
        self.press_or_release(Keycode.F1, is_pressed)

    def f2(self, is_pressed):
        self.press_or_release(Keycode.F2, is_pressed)

    def f3(self, is_pressed):
        self.press_or_release(Keycode.F3, is_pressed)

    def f4(self, is_pressed):
        self.press_or_release(Keycode.F4, is_pressed)

    def f5(self, is_pressed):
        self.press_or_release(Keycode.F5, is_pressed)

    def f6(self, is_pressed):
        self.press_or_release(Keycode.F6, is_pressed)

    def f7(self, is_pressed):
        self.press_or_release(Keycode.F7, is_pressed)

    def f8(self, is_pressed):
        self.press_or_release(Keycode.F8, is_pressed)

    def f9(self, is_pressed):
        self.press_or_release(Keycode.F9, is_pressed)

    def f10(self, is_pressed):
        self.press_or_release(Keycode.F10, is_pressed)

    def f11(self, is_pressed):
        self.press_or_release(Keycode.F11, is_pressed)

    def f12(self, is_pressed):
        self.press_or_release(Keycode.F12, is_pressed)

    def print(self, is_pressed):
        self.press_or_release(Keycode.PRINT_SCREEN, is_pressed)

    def roll(self, is_pressed):
        self.press_or_release(Keycode.SCROLL_LOCK, is_pressed)

    def pause(self, is_pressed):
        self.press_or_release(Keycode.PAUSE, is_pressed)

    def circumflex(self, is_pressed):
        self.press_or_release(Keycode.ZIRKUMFLEX, is_pressed)

    def alpha_1(self, is_pressed):
        self.press_or_release(Keycode.ONE, is_pressed)

    def alpha_2(self, is_pressed):
        self.press_or_release(Keycode.TWO, is_pressed)

    def alpha_3(self, is_pressed):
        self.press_or_release(Keycode.THREE, is_pressed)

    def alpha_4(self, is_pressed):
        self.press_or_release(Keycode.FOUR, is_pressed)

    def alpha_5(self, is_pressed):
        self.press_or_release(Keycode.FIVE, is_pressed)

    def alpha_6(self, is_pressed):
        self.press_or_release(Keycode.SIX, is_pressed)

    def alpha_7(self, is_pressed):
        self.press_or_release(Keycode.SEVEN, is_pressed)

    def alpha_8(self, is_pressed):
        self.press_or_release(Keycode.EIGHT, is_pressed)

    def alpha_9(self, is_pressed):
        self.press_or_release(Keycode.NINE, is_pressed)

    def alpha_0(self, is_pressed):
        self.press_or_release(Keycode.ZERO, is_pressed)

    def eszett(self, is_pressed):
        self.press_or_release(Keycode.ESZETT, is_pressed)

    def tick(self, is_pressed):
        self.press_or_release(Keycode.AKUT, is_pressed)

    def backspace(self, is_pressed):
        self.press_or_release(Keycode.BACKSPACE, is_pressed)

    def insert(self, is_pressed):
        self.press_or_release(Keycode.INSERT, is_pressed)

    def home(self, is_pressed):
        self.press_or_release(Keycode.HOME, is_pressed)

    def page_up(self, is_pressed):
        self.press_or_release(Keycode.PAGE_UP, is_pressed)

    def tab(self, is_pressed):
        self.press_or_release(Keycode.TAB, is_pressed)

    def q(self, is_pressed):
        self.press_or_release(Keycode.Q, is_pressed)

    def w(self, is_pressed):
        self.press_or_release(Keycode.W, is_pressed)

    def e(self, is_pressed):
        self.press_or_release(Keycode.E, is_pressed)

    def r(self, is_pressed):
        self.press_or_release(Keycode.R, is_pressed)

    def t(self, is_pressed):
        self.press_or_release(Keycode.T, is_pressed)

    def z(self, is_pressed):
        self.press_or_release(Keycode.Z, is_pressed)

    def u(self, is_pressed):
        self.press_or_release(Keycode.U, is_pressed)

    def i(self, is_pressed):
        self.press_or_release(Keycode.I, is_pressed)

    def o(self, is_pressed):
        self.press_or_release(Keycode.O, is_pressed)

    def p(self, is_pressed):
        self.press_or_release(Keycode.P, is_pressed)

    def umlaut_u(self, is_pressed):
        self.press_or_release(Keycode.SEMICOLON, is_pressed)

    def times(self, is_pressed):
        self.press_or_release(Keycode.EQUALS, is_pressed)

    def enter(self, is_pressed):
        self.press_or_release(Keycode.RETURN, is_pressed)

    def delete(self, is_pressed):
        self.press_or_release(Keycode.DELETE, is_pressed)

    def end(self, is_pressed):
        self.press_or_release(Keycode.END, is_pressed)

    def page_down(self, is_pressed):
        self.press_or_release(Keycode.PAGE_DOWN, is_pressed)

    def caps(self, is_pressed):
        self.press_or_release(Keycode.CAPS_LOCK, is_pressed)

    def a(self, is_pressed):
        self.press_or_release(Keycode.A, is_pressed)

    def s(self, is_pressed):
        self.press_or_release(Keycode.S, is_pressed)

    def d(self, is_pressed):
        self.press_or_release(Keycode.D, is_pressed)

    def f(self, is_pressed):
        self.press_or_release(Keycode.F, is_pressed)

    def g(self, is_pressed):
        self.press_or_release(Keycode.G, is_pressed)

    def h(self, is_pressed):
        self.press_or_release(Keycode.H, is_pressed)

    def j(self, is_pressed):
        self.press_or_release(Keycode.J, is_pressed)

    def k(self, is_pressed):
        self.press_or_release(Keycode.K, is_pressed)

    def l(self, is_pressed):
        self.press_or_release(Keycode.L, is_pressed)

    def umlaut_o(self, is_pressed):
        self.press_or_release(Keycode.GRAVE_ACCENT, is_pressed)

    def umlaut_a(self, is_pressed):
        self.press_or_release(Keycode.QUOTE, is_pressed)

    def hash(self, is_pressed):
        self.press_or_release(Keycode.FORWARD_SLASH, is_pressed)

    def shift_left(self, is_pressed):
        self.press_or_release(Keycode.LEFT_SHIFT, is_pressed)

    def less_than(self, is_pressed):
        self.press_or_release(Keycode.OEM_102, is_pressed)

    def y(self, is_pressed):
        self.press_or_release(Keycode.Y, is_pressed)

    def x(self, is_pressed):
        self.press_or_release(Keycode.X, is_pressed)

    def c(self, is_pressed):
        self.press_or_release(Keycode.C, is_pressed)

    def v(self, is_pressed):
        self.press_or_release(Keycode.V, is_pressed)

    def b(self, is_pressed):
        self.press_or_release(Keycode.B, is_pressed)

    def n(self, is_pressed):
        self.press_or_release(Keycode.N, is_pressed)

    def m(self, is_pressed):
        self.press_or_release(Keycode.M, is_pressed)

    def comma(self, is_pressed):
        self.press_or_release(Keycode.COMMA, is_pressed)

    def dot(self, is_pressed):
        self.press_or_release(Keycode.PERIOD, is_pressed)

    def minus(self, is_pressed):
        self.press_or_release(Keycode.MINUS, is_pressed)

    def shift_right(self, is_pressed):
        self.press_or_release(Keycode.RIGHT_SHIFT, is_pressed)

    def arrow_up(self, is_pressed):
        self.press_or_release(Keycode.UP_ARROW, is_pressed)

    def control_left(self, is_pressed):
        self.press_or_release(Keycode.LEFT_CONTROL, is_pressed)

    def windows_left(self, is_pressed):
        self.press_or_release(Keycode.WINDOWS, is_pressed)

    def alt_left(self, is_pressed):
        self.press_or_release(Keycode.ALT, is_pressed)

    def space(self, is_pressed):
        self.press_or_release(Keycode.SPACEBAR, is_pressed)

    def alt_right(self, is_pressed):
        self.press_or_release(Keycode.ALTGR, is_pressed)

    def windows_right(self, is_pressed):
        self.press_or_release(Keycode.WINDOWS, is_pressed)

    def context(self, is_pressed):
        self.press_or_release(Keycode.APPLICATION, is_pressed)

    def control_right(self, is_pressed):
        self.press_or_release(Keycode.RIGHT_CONTROL, is_pressed)

    def arrow_left(self, is_pressed):
        self.press_or_release(Keycode.LEFT_ARROW, is_pressed)

    def arrow_down(self, is_pressed):
        self.press_or_release(Keycode.DOWN_ARROW, is_pressed)

    def arrow_right(self, is_pressed):
        self.press_or_release(Keycode.RIGHT_ARROW, is_pressed)

    def numpad(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_NUMLOCK, is_pressed)

    def numpad_slash(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_FORWARD_SLASH, is_pressed)

    def numpad_times(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_ASTERISK, is_pressed)

    def numpad_minus(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_MINUS, is_pressed)

    def numpad_7(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_SEVEN, is_pressed)

    def numpad_8(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_EIGHT, is_pressed)

    def numpad_9(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_NINE, is_pressed)

    def numpad_plus(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_PLUS, is_pressed)

    def numpad_4(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_FOUR, is_pressed)

    def numpad_5(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_FIVE, is_pressed)

    def numpad_6(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_SIX, is_pressed)

    def numpad_1(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_ONE, is_pressed)

    def numpad_2(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_TWO, is_pressed)

    def numpad_3(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_THREE, is_pressed)

    def numpad_enter(self, is_pressed):
        self.press_or_release(Keycode.ENTER, is_pressed)

    def numpad_0(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_ZERO, is_pressed)

    def numpad_comma(self, is_pressed):
        self.press_or_release(Keycode.KEYPAD_PERIOD, is_pressed)

    def handle_key_change(self, key, is_pressed):
        self.key_map[key](is_pressed)

    def __init__(self):
        self.keyboard = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayout(self.keyboard)
        self.consumer_control = ConsumerControl(usb_hid.devices)
        self.counter = 70

        # contains a mapping of pin_code to named function
        self.key_map = {
            137: self.nav_back,
            50: self.nav_forward,
            54: self.nav_close,
            53: self.nav_refresh,
            132: self.nav_search,
            141: self.nav_explorer,
            136: self.nav_home,
            131: self.nav_mail,
            127: self.nav_mute,
            119: self.nav_sleep,
            130: self.nav_vol_down,
            123: self.nav_vol_up,
            52: self.nav_play_pause,
            143: self.nav_stop_song,
            116: self.nav_next_song,
            139: self.nav_prev_song,
            140: self.nav_media_player,
            122: self.nav_desktop,
            128: self.nav_keyboard,
            57: self.esc,
            19: self.f1,
            20: self.f2,
            23: self.f3,
            22: self.f4,
            21: self.f5,
            8: self.f6,
            9: self.f7,
            10: self.f8,
            11: self.f9,
            12: self.f10,
            95: self.f11,
            94: self.f12,
            93: self.print,
            14: self.roll,
            100: self.pause,
            33: self.circumflex,
            58: self.alpha_1,
            59: self.alpha_2,
            60: self.alpha_3,
            63: self.alpha_4,
            62: self.alpha_5,
            61: self.alpha_6,
            64: self.alpha_7,
            65: self.alpha_8,
            66: self.alpha_9,
            67: self.alpha_0,
            68: self.eszett,
            71: self.tick,
            70: self.backspace,
            101: self.insert,
            97: self.home,
            99: self.page_up,
            69: self.tab,
            72: self.q,
            73: self.w,
            74: self.e,
            75: self.r,
            76: self.t,
            79: self.z,
            78: self.u,
            77: self.i,
            80: self.o,
            81: self.p,
            82: self.umlaut_u,
            83: self.times,
            84: self.enter,
            30: self.delete,
            34: self.end,
            18: self.page_down,
            16: self.caps,
            86: self.a,
            85: self.s,
            40: self.d,
            41: self.f,
            42: self.g,
            43: self.h,
            44: self.j,
            47: self.k,
            46: self.l,
            45: self.umlaut_o,
            32: self.umlaut_a,
            35: self.hash,
            120: self.shift_left,
            56: self.less_than,
            36: self.y,
            39: self.x,
            38: self.c,
            37: self.v,
            24: self.b,
            25: self.n,
            26: self.m,
            27: self.comma,
            28: self.dot,
            31: self.minus,
            124: self.shift_right,
            98: self.arrow_up,
            106: self.control_left,
            113: self.windows_left,
            135: self.alt_left,
            17: self.space,
            134: self.alt_right,
            142: self.windows_right,
            125: self.context,
            107: self.control_right,
            103: self.arrow_left,
            87: self.arrow_down,
            102: self.arrow_right,
            15: self.numpad,
            109: self.numpad_slash,
            29: self.numpad_times,
            2: self.numpad_minus,
            13: self.numpad_7,
            0: self.numpad_8,
            1: self.numpad_9,
            6: self.numpad_plus,
            3: self.numpad_4,
            4: self.numpad_5,
            7: self.numpad_6,
            5: self.numpad_1,
            88: self.numpad_2,
            89: self.numpad_3,
            92: self.numpad_enter,
            90: self.numpad_0,
            91: self.numpad_comma,
        }
