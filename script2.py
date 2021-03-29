import RPi.GPIO as GPIO
import time
from test import decToBinList
from script1 import num2dac


GPIO.setmode(GPIO.BCM)

leds = [10, 9, 11, 5, 6, 13, 19, 26]


def main():
    while True:
        print("Введите число повторений: ")
        try:
            value = int(input())
        except ValueError:
            print("Некорректное значение. Попробуйте ещё раз.")
            continue
        if value == -1:
            GPIO.cleanup()
            exit()
        elif value >= 1:
            break
    repeat(value)
    print("Для продолжения нажмите Enter, для выхода -1: ")
    while input() != '-1':
        main()


def repeat(repetitionsNumber):
    for y in range(repetitionsNumber):
        for x in range(256):
            num2dac(x, slee_time=0.01)
        for x in range(255, 0, -1):
            num2dac(x, slee_time=0.01)



if __name__ == "__main__":
    main()

