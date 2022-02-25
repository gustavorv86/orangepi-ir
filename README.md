
# ORANGEPI-IR

## Description

Configure Orange PI infrared device in Armbian OS.

## Install

Use INSTALL script to enable all protocols.

```bash
bash$ ./INSTALL
```

To uninstall use the next command.

```bash
bash$ ./INSTALL --uninstall
```

## Bash

Test your device with the bash scripts.

```bash
bash$ ./scripts/show-udev-info.sh
bash$ ./scripts/show-protocols.sh 
bash$ ./scripts/evtest-ir.sh  
```

## Development

Install Python evdev library.

Via apt:

```bash
bash$ apt install python3-evdev
```

Via Pip3

```bash
bash$ pip3 install evdev
```

Start script example.

```bash
bash$ ./src/python/event.py
```

More information

[evdev pypi project](https://pypi.org/project/evdev/)
[evdev readthedocs](https://python-evdev.readthedocs.io/en/latest/index.html)

