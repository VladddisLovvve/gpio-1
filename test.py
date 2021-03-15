import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    global led_dict
    led_dict = {7: 21, 6: 20, 5: 16, 4: 12, 3: 7, 2: 8, 1: 25, 0: 24}
    lightUP(2, 2)
    blink(5, 3, 0.4)
    runningLight(1, 0.3)
    runningDark(1, 0.3)
    print(decToBinList(-1))
    lightNumber(3)
    GPIO.cleanup()


def lightUP(ledNumber, period, mode = 1):
    ledNumber = led_dict[ledNumber % 8]
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, mode)
    time.sleep(period)
    GPIO.output(ledNumber, not mode)


def blink(ledNumber, blinkCount, blinkPeriod):
    for _ in range(blinkCount):
        lightUP(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)


def runningLight(count, period, mode = 1):
    for _ in range(count):
        for ledNumber in list(led_dict.keys())[::-1]:
            lightUP(ledNumber, period, mode)


def runningDark(count, period):
    GPIO.setup(list(led_dict.values()), GPIO.OUT)
    GPIO.output(list(led_dict.values()), 1)
    runningLight(count, period, mode = 0)


def decToBinList(decNumber):
    return [int(x) for x in format(decNumber % 256, "b").zfill(8)]


def lightNumber(number):
    d = list(led_dict.values())
    d = [d[x] for x in range(len(d)) if decToBinList(number)[x] != 0]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)
    time.sleep(2)


if __name__ == "__main__":
    main()