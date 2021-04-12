import RPi.GPIO as GPIO
import time
from test import decToBinList


GPIO.setmode(GPIO.BCM)

leds = [10, 9, 11, 5, 6, 13, 19, 26][::-1]


def main():
    GPIO.setup(leds + [17], GPIO.OUT)
    GPIO.output(17, 1)
    try:
        while True:
            print("Введите значение от 0 до 255(-1 для выхода): ")
            value = create_value()
            if value == -1:
                GPIO.cleanup()
                exit()
            GPIO.output(leds, [0] * 8)
            num2dac(value)
    finally:
        GPIO.cleanup()

def create_value():
    while True:
        value = input()
        if value.isdigit() or (value[0] == "-" and value[1:].isdigit()):
            value = int(value)
        else:
            print("Некорректное значение. Попробуйте ещё раз.")
            continue
        if value == -1:
            return -1
        elif 0 <= value <= 255:
            return value
        else:
            print("Некорректное значение. Попробуйте ещё раз.")
            continue
    

def num2dac(value, slee_time = 1):
    dac = [leds[x] for x in range(8) if decToBinList(value)[x] == 1]
    print(f"Напряжение в вольтах: {round(value / 255 * 3.3, 1)}V\n")
    GPIO.setup(dac, GPIO.OUT)
    GPIO.output(dac, 1)
    #time.sleep(slee_time)
    #GPIO.output(dac, 0)


if __name__ == "__main__":
    main()