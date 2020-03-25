from time import sleep

from absl.detailed import a


def something():
    sleep(1)
    a.something()
    print('This is B')