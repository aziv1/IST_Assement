import gpiod
import time

def set_pin_val(chip_name, pin_off, pin_val):
    try:
        with gpiod.Chip(chip_name) as chip:
            line = chip.get_line(pin_off)
            line.request(consumer="gpio_test_script", type=gpiod.LINE_REQ_DIR_OUT)

            line.set_value(pin_val)
            print(f"Written Pin {pin_off} to {pin_val}")
            line.release()
    except Exception as e:
        print("Error:", e)

#GPIO DATA
chip_name = "/dev/gpiochip4"
pin_off = 19
pin_val = 0

set_pin_val(chip_name, pin_off, pin_val)
time.sleep(1)