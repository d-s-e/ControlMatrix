#!/usr/bin/env python
from multiprocessing import Process

from services.twitch.main import main as twitch
from services.dmx.main import main as dmx
from services.midi.main import main as midi


if __name__ == '__main__':
    processes = [
        Process(target=dmx),
        Process(target=twitch),
        Process(target=midi),
    ]

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()
