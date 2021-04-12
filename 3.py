import RPi.GPIO as GPIO
import time
from test import decToBinList


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
    
        if GPIO.input(4) == 0:
            print(f"Цифровое значение: {i}, Аналоговое значение: {round(i / 255 * 3.3, 1)}V")
            break
    return i


def binary_search (range((), value, descending=False):
    left = 0
    right = len(sorted_values)
    while left < right:
        if sorted_values[left] == value:
            return (True, left)
        middle = left + (right - left) // 2
        if sorted_values[middle] == value:
            if middle == left + 1:
                return (True, middle)
            right = middle + 1
        if (sorted_values[middle] < value) == descending:
            right = middle
        else:
            left = middle + 1
    return (False, left)


if __name__ == "__main__":
    main()