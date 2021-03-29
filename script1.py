import RPi.GPIO as GPIO
import time
from test import decToBinList


GPIO.setmode(GPIO.BCM)

leds = [10, 9, 11, 5, 6, 13, 19, 26]


def main():
    while True:
        print("Введите значение от 0 до 255(-1 для выхода): ")
        try:
            value = int(input())
        except ValueError:
            print("Некорректное значение. Попробуйте ещё раз.")
            continue
        if value == -1:
            GPIO.cleanup()
            exit()
        elif 0 <= value <= 255:
            break
    num2dac(value)
    print("Для продолжения нажмите Enter, для выхода -1: ")
    while input() != '-1':
        main()
    

def num2dac(value, slee_time = 20):
    dac = [leds[x] for x in range(8) if decToBinList(value)[x] == 1]
    GPIO.setup(dac, GPIO.OUT)
    GPIO.output(dac, 1)
    time.sleep(slee_time)
    GPIO.output(dac, 0)


if __name__ == "__main__":
    main()
