import RPi.GPIO as GPIO
import time
from test import decToBinList, lightNumber


GPIO.setmode(GPIO.BCM)

leds = [10, 9, 11, 5, 6, 13, 19, 26][::-1]


def main():
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(4, GPIO.IN)
    GPIO.output(17, 1)
    GPIO.setup(leds, GPIO.OUT)
    while True:
        adc_procedure()


def dac_data(n):
    for i in range(8):
        GPIO.output(leds[i], decToBinList(n)[i])


def adc_procedure():
    for i in range(256):
        dac_data(i)
        if GPIO.input(4) == 0:
            out = leds[:(i // 30)]
            sig = [1] * (i // 30)
            print(out, sig)
            GPIO.output(out, sig)
            break
    return i


if __name__ == "__main__":
    main()