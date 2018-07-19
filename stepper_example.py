# a quick example to test out my 28BYJ-48 stepper motors

# my preferred RPi GPIO wrapper library
import gpiozero
import time

print "Stepper Motor Example:"

# which pins are connected to the stepper motor driver, in order 1-4
STEPPER_GPIO = (23, 22, 27, 17)

# the patterns on the pins that cause the motor to rotate
# it does not matter where the pattern starts, just how it progresses
STEPS = (
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 0, 0, 1),
    (1, 0, 0, 1)
)

print " - Initializing GPIO pins..."
# create the software drivers for the GPIO pins
STEPPER_PINS = []
for gpio_pin in range(len(STEPPER_GPIO)):
    STEPPER_PINS.append(gpiozero.OutputDevice(STEPPER_GPIO[gpio_pin]))


# write the given position tuple out to the pins
def set_position(pos):
    for i in range(len(STEPPER_PINS)):
        STEPPER_PINS[i].value = pos[i]


# don't hold the motor's current position any longer
def motor_off():
    set_position((0, 0, 0, 0))


# rotate clockwise, looking down at the motor's shaft side
def rotate_steps_clockwise(steps, delay):
    for i in range(steps):
        set_position(STEPS[i % len(STEPS)])
        time.sleep(delay)


# rotate counter-clockwise, looking down at the motor's shaft side
def rotate_steps_counterclockwise(steps, delay):
    for i in reversed(range(steps)):
        set_position(STEPS[i % len(STEPS)])
        time.sleep(delay)


# run an example of turning half a rotation and then turning back
do_steps = 2048
delay = 0.001
print " - Rotating clockwise..."
rotate_steps_clockwise(do_steps, delay)

print " - Rotating counterclockwise..."
rotate_steps_counterclockwise(do_steps, delay)

print " - Releasing motor..."
motor_off()

print "Done."
