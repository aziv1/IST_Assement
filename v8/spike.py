from hub import port
import color_sensor
import color
import runloop
import motor_pair

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.C)
    while True:
        if color_sensor.color(port.E) is color.RED:
            print("Seen Red")
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 160, 0)
        elif color_sensor.color(port.E) is color.BLUE:
            print("Seen Blue")
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, -160, 0)
        else:
            motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
