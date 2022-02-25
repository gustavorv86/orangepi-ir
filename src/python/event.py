#!/usr/bin/env python3

import evdev

INPUT_DEVICE = "/dev/input/event1"

if __name__ == "__main__":
    device = evdev.InputDevice(INPUT_DEVICE)

    for event in device.read_loop():
        print(event)
        
        if event.type == 4 and event.code == 4 and event.value == 12160:
            break

        if event.type == 4 and event.code == 4 and event.value == 130828:
            break

    
    print("Poweroff")
    device.close()

