from time import sleep

from absl.detailed import a, b


def something():
    sleep(1)
    a.something()
    b.something()
    print('This is C')


