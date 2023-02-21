import time
import math

def animate():
    position = 0
    while True:

        x = round(40 * math.cos(position / 10) + 40)

        print('\033[10;{}H💩'.format(x))
        time.sleep(0.1)

        print('\033[10;{}H\033[K'.format(x), end='')

        position += 1

if __name__ == '__main__':
    animate()
