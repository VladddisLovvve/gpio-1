import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import RPi.GPIO as GPIO
from script1 import num2dac


GPIO.setmode(GPIO.BCM)

leds = [10, 9, 11, 5, 6, 13, 19, 26][::-1]


def dac_sin(time, frequency):
    time = np.arange(0, time, 1 / frequency)
    y = 255 * np.sin(time)
    amplitude = [int(x) for x in y]
    plt.plot(time, amplitude)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()
    for value in amplitude:
        num2dac(value, slee_time = 1 / frequency)


if __name__ == "__main__":
    dac_sin(20, 20000)
