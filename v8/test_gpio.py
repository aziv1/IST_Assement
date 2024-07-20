import gpiozero as gp

eight = gp.LED(19)
four = gp.LED(16)
two = gp.LED(26)
one = gp.LED(20)

try:
    eight.on()
    four.on()
    two.on()
    one.on()
    print("Eight, Four, Two, One ON")
    eight.off()
    four.off()
    two.off()
    one.off()
    print("Eight, Four, Two, One OFF")
except Exception as e:
    print("Error:", e)
    gp.close()