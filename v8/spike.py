from hub import port
from motor import absolute_position
import motor
import runloop
import motor_pair
import color_sensor
import color
async def main():
     motor_pair.pair(motor_pair.PAIR_1, port.A, port.C)
     while True:
        if color_sensor.color(port.E) is color.RED:
            print("seen red")
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 270, 0)
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, -270, 0)
        elif color_sensor.color(port.E) is color.BLUE:
            print("seen blue")
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, -270, 0)
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 270, 0)
        else:
            motor_pair.stop(motor_pair.PAIR_1)
runloop.run(main())
