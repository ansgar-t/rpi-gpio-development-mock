import pkg_resources

UNKNOWN = -1

OUT = 0
IN = 1
LOW = 0
HIGH = 1
BOARD = 10
PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22
BCM = 11

RISING = 31
FALLING = 32
BOTH = 33

SERIAL = 40
SPI=41
I2C = 42
HARD_PWM = 43

PWM = None

RPI_INFO = {
    'MANUFACTURER': 'Embest',
    'P1_REVISION': 3,
    'PROCESSOR': 'BCM2836',
    'RAM': '1024M',
    'REVISION': 'a21041',
    'TYPE': 'Pi2 Model B',
    'TESTING_INFO': 'This is only a Mock.'
}
RPI_VERSION = 3
VERSION = pkg_resources.require("RPi.GPIO")[0].version


class State(object):
    pass


def setup(*args, **xargs):
    pass


def setwarnings(*args, **kwargs):
    pass


def setmode(*args, **xargs):
    pass


def getmode(*args, **xargs):
    pass


def cleanup(*args, **xargs):
    pass


def output(*args, **xargs):
    pass


def input(*args, **kwargs):
    return ""


def set_warnings(*args, **kwargs):
    pass


def wait_for_edge(*args, **kwargs):
    pass


def add_event_detect(*args, **kwargs):
    pass


def remove_event_detect(*args, **kwargs):
    pass


def event_detected(*args, **kwargs):
    return True


def gpio_function(*args, **kwargs):
    pass


def add_event_callback(*args, **kwargs):
    pass
