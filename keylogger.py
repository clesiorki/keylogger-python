#!/usr/bin/env python

import evdev

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)


teclado = evdev.InputDevice('/dev/input/event0')
print(teclado)
for event in teclado.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(teclado.active_keys(verbose=True))
