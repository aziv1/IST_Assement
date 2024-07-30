from gpiozero import LED

eight = LED(19)
four = LED(16)
two = LED(26)
one = LED(20)

gpio_pins = [LED(19), LED(16), LED(26), LED(20)]

while True:
    number = int(input("Enter Number: "))
    if number >= 16 or number < 0:
        print("Invalid Number Entered")
    else:
        binary_string = format(number, '04b') #Convert to 4bit binary string

        for i, bit in enumerate(binary_string):
            if bit == '1':
                gpio_pins[i].on()
                print(f"Set {gpio_pins[i]} to 1")
            else:
                gpio_pins[i].off()
                print(f"Set {gpio_pins[i]} to 0")
        print(f"Exported Number {number}")