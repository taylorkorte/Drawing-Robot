# Code used to control servo motors
# Small Servos: 500 (0) - 2500 (180)
# Big Servos: 600 (0) - 2190 (180)

from PCA9685 import Driver

# import time

CHANNEL = 0
LEFT = 600
RIGHT = 2190

HAT_ADDR = 0x40 # I2C

pwm = Driver(HAT_ADDR, debug=False)
pwm.setPWMFreq(50)

def move_servo(channel, position):
    pwm.setServoPulse(channel, position)

# Code used to test servo range
# while (True):
#     pwm.setServoPulse(CHANNEL, LEFT)
#     time.sleep(2)
#     pwm.setServoPulse(CHANNEL, RIGHT)
#     time.sleep(2)