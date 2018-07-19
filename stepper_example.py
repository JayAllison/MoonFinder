# a quick example to test out my 28BYJ-48 stepper motors

# my preferred RPi GPIO wrapper library
import gpiozero
import time

# which pins are connected to the stepper motor driver, in order 1-4
STEPPER_GPIO = (23, 22, 27, 17)

# the patterns on the pins that cause the motor to rotate
# it does not matter where the pattern starts, just how it progresses
STEPS = (
    (0, 1, 0, 0),
    (0, 1, 0, 1),
    (0, 0, 0, 1),
    (1, 0, 0, 1),
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (0, 0, 1, 0),
    (0, 1, 1, 0)
)

# create the software drivers for the GPIO pins
STEPPER_PINS = []
for gpio_pin in range(len(STEPPER_GPIO)):
    STEPPER_PINS.append(gpiozero.OutputDevice(STEPPER_GPIO[gpio_pin]))


# write the given position tuple out to the pins
def set_position(pos):
    if len(pos) != len(STEPPER_PINS):
        raise Exception("position length mismatch")
    for i in range(len(STEPPER_PINS)):
        STEPPER_PINS[i].value = pos[i]


def motor_off():
    set_position((0, 0, 0, 0))


def rotate_steps_clockwise(steps, delay):
    for i in range(steps):
        set_position(STEPS[i % len(STEPS)])
        time.sleep(delay)


def rotate_steps_counterclockwise(steps, delay):
    for i in reversed(range(steps)):
        set_position(STEPS[i % len(STEPS)])
        time.sleep(delay)


rotate_steps_clockwise(1024, 0.010)
