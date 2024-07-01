from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP, pause

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    lcd.clear()
except:
    print("Unable to clear")

