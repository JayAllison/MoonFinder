import atexit
import datetime
from gpiozero import LED
from lcd_display import lcd_display
import logging
from PIL import Image
import signal
import syslog
import traceback


_PRINT_INSTEAD_OF_SYSLOG = False
_LOG_LEVEL = logging.WARNING

_ERROR_LED = 4

_UP_BUTTON = 7
_CENTER_BUTTON = 12
_DOWN_BUTTON = 16
_LEFT_BUTTON = 20
_RIGHT_BUTTON = 21

_running = False
_error_led = None


def _log(message):

    if _PRINT_INSTEAD_OF_SYSLOG:
        print (str(datetime.datetime.now()) + " INFO: " + message)
    else:
        syslog.syslog(syslog.LOG_INFO, message)


def _log_error(message):

    if _PRINT_INSTEAD_OF_SYSLOG:
        print (str(datetime.datetime.now()) + " ERROR: " + message)
    else:
        syslog.syslog(syslog.LOG_ERR, message)


def _log_exception(message):

    if _PRINT_INSTEAD_OF_SYSLOG:
        print (str(datetime.datetime.now()) + " EXCEPTION: " + message)
    else:
        syslog.syslog(syslog.LOG_CRIT, message)
        syslog.syslog(syslog.LOG_CRIT, traceback.format_exc())


def start():
    logging.basicConfig(level=_LOG_LEVEL,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s',
                        datefmt='%Y/%m/%d %I:%M:%S%p')

    global _running
    _running = True

    global error_led
    error_led = LED(_ERROR_LED)
    error_led.off()

    logo = Image.open("Images/moon_icon.png")
    lcd_display.display(logo)


# noinspection PyUnusedLocal
def stop(signum, frame):

    global _running
    _running = False
    _log("SIGNAL received - stopping...")


def run():

    # initialize things
    start()

    # TODO: the dispatch loop...


def on_exit():

    if error_led:
        error_led.on()
    _log("--- MoonFinder exiting ---")


if __name__ == "__main__":
    _log("--- MoonFinder starting ---")
    atexit.register(on_exit)
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    run()
